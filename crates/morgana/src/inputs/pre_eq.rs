/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! CM-OSSI I27 Tables 77/78 immutable applied-bank and last-update observations.
use crate::api::{bounded_json, ApiError, ApiResult, CaptureFailure, Iq};
use serde::Serialize;
use sha2::{Digest, Sha256};
use std::sync::Arc;

const HEADER_BYTES: usize = 34;
const MAX_BYTES: usize = HEADER_BYTES + 4096 * 4;

/// Source file kind determines scale, never the missing RNG-RSP operation.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize)]
pub enum PreEqCaptureKind {
    /// Applied coefficients: signed two's-complement s2.13.
    Applied,
    /// Most recent update: s1.14, requires explicit Set/Adjust and probe context.
    LastUpdate,
}
/// Exact source header, independent of simulation association and activation time.
#[derive(Debug, Clone, PartialEq, Eq, Serialize)]
pub struct PreEqHeader {
    /// Source major version, exactly one in this adapter profile.
    pub major_version: u8,
    /// Opaque vendor revision, not a guessed extension indicator.
    pub minor_version: u8,
    /// Original Unix epoch seconds.
    pub capture_time_epoch_seconds: u32,
    /// Original upstream channel ID, not an interface index.
    pub upstream_channel_id: u8,
    /// Original measured CM identity.
    pub cm_mac: [u8; 6],
    /// Downstream MAC receiving MAPs/UCDs, not an invented CCAP ID.
    pub cmts_mac: [u8; 6],
    /// Physical bin-zero frequency in hertz.
    pub subcarrier_zero_hz: u32,
    /// First physical index in the retained contiguous extent.
    pub first_active_subcarrier: u16,
    /// Exactly 25 or 50 kHz in this profile.
    pub subcarrier_spacing_khz: u8,
    /// Exact declared data bytes, a multiple of four.
    pub data_length_bytes: u32,
}
/// Immutable lossless capture; coefficients never imply injected channel truth.
#[derive(Debug, Clone, PartialEq)]
pub struct PreEqCapture {
    original: Arc<[u8]>,
    kind: PreEqCaptureKind,
    header: PreEqHeader,
    coefficients: Vec<Iq>,
}
fn failure(category: CaptureFailure, field: &'static str, offset: usize) -> ApiError {
    ApiError::Capture {
        category,
        field,
        offset,
    }
}
fn invalid(field: &'static str, offset: usize) -> ApiError {
    failure(CaptureFailure::InvalidInput, field, offset)
}
fn u32_at(bytes: &[u8], offset: usize) -> u32 {
    u32::from_be_bytes([
        bytes[offset],
        bytes[offset + 1],
        bytes[offset + 2],
        bytes[offset + 3],
    ])
}
impl PreEqCapture {
    /// Decodes one exact major1 bank/update in the explicit MS-octet-first profile.
    ///
    /// Returns immutable originals/header/IQ. Input is at most 16418 bytes and
    /// 4096 complex coefficients; wrong type/version/spacing returns Unsupported,
    /// malformed lengths/grids retain byte offsets. Empty files stay inspectable.
    pub fn from_pnm(bytes: &[u8]) -> ApiResult<Self> {
        if bytes.len() > MAX_BYTES {
            return Err(failure(CaptureFailure::ResourceLimit, "pre_eq.bytes", 0));
        }
        if bytes.len() < HEADER_BYTES {
            return Err(invalid("pre_eq.header", bytes.len()));
        }
        let kind = match bytes[..4] {
            [0x50, 0x4e, 0x4e, 6] => PreEqCaptureKind::Applied,
            [0x50, 0x4e, 0x4e, 7] => PreEqCaptureKind::LastUpdate,
            _ => return Err(failure(CaptureFailure::Unsupported, "pre_eq.file_type", 0)),
        };
        if bytes[4] != 1 {
            return Err(failure(
                CaptureFailure::Unsupported,
                "pre_eq.major_version",
                4,
            ));
        }
        let n = match bytes[29] {
            25 => 4096,
            50 => 2048,
            _ => return Err(failure(CaptureFailure::Unsupported, "pre_eq.spacing", 29)),
        };
        let length = u32_at(bytes, 30);
        if length > 4096 * 4 || length % 4 != 0 || HEADER_BYTES + length as usize != bytes.len() {
            return Err(invalid("pre_eq.data_length", 30));
        }
        let first = u16::from_be_bytes([bytes[27], bytes[28]]);
        if usize::from(first) >= n || usize::from(first) + length as usize / 4 > n {
            return Err(invalid("pre_eq.subcarrier_grid", 27));
        }
        let divisor = match kind {
            PreEqCaptureKind::Applied => 8192.0,
            PreEqCaptureKind::LastUpdate => 16384.0,
        };
        let coefficients = bytes[HEADER_BYTES..]
            .chunks_exact(4)
            .map(|pair| Iq {
                re: f64::from(i16::from_be_bytes([pair[0], pair[1]])) / divisor,
                im: f64::from(i16::from_be_bytes([pair[2], pair[3]])) / divisor,
            })
            .collect();
        Ok(Self {
            original: Arc::from(bytes),
            kind,
            coefficients,
            header: PreEqHeader {
                major_version: bytes[4],
                minor_version: bytes[5],
                capture_time_epoch_seconds: u32_at(bytes, 6),
                upstream_channel_id: bytes[10],
                cm_mac: bytes[11..17]
                    .try_into()
                    .map_err(|_| invalid("pre_eq.cm_mac", 11))?,
                cmts_mac: bytes[17..23]
                    .try_into()
                    .map_err(|_| invalid("pre_eq.cmts_mac", 17))?,
                subcarrier_zero_hz: u32_at(bytes, 23),
                first_active_subcarrier: first,
                subcarrier_spacing_khz: bytes[29],
                data_length_bytes: length,
            },
        })
    }
    /// Borrows exact source bytes for this immutable capture's lifetime.
    ///
    /// Includes opaque vendor metadata and original signed coefficient encodings.
    pub fn original_bytes(&self) -> &[u8] {
        &self.original
    }
    /// Hashes exact originals into owned lowercase SHA-256 text.
    ///
    /// Exporting or cloning never modifies the source bytes.
    pub fn original_sha256(&self) -> String {
        format!("{:x}", Sha256::digest(&self.original))
    }
    /// Returns source kind and therefore its fixed-point scale.
    ///
    /// LastUpdate does not determine initialization versus adjustment.
    pub fn kind(&self) -> PreEqCaptureKind {
        self.kind
    }
    /// Borrows source metadata without synthesizing missing control context.
    ///
    /// All original times and identities retain their separate meanings.
    pub fn header(&self) -> &PreEqHeader {
        &self.header
    }
    /// Borrows exact scaled I/Q pairs in physical subgrid order.
    ///
    /// No normalization, inverse channel inference or gap filling occurs here.
    pub fn coefficients(&self) -> &[Iq] {
        &self.coefficients
    }
    /// Exports bounded schema1 observation JSON, independent of configurations.
    ///
    /// Returns owned text; original bytes remain separately available.
    pub fn to_json(&self) -> ApiResult<String> {
        bounded_json(
            &serde_json::json!({
                "format":"morgana.pre-eq-capture", "schema_version":1,
                "semantics":"decoded-observation-only", "numeric_encoding":"explicit-most-significant-octet-first-profile",
                "kind":self.kind, "header":self.header, "coefficients":self.coefficients,
                "original_byte_count":self.original.len(), "original_sha256":self.original_sha256(),
            }),
            1024 * 1024,
        )
    }
}
