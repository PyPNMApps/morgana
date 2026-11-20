/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Configure → run → report facade; current execution scope is upstream FEC only.
#![forbid(unsafe_code)]

pub mod api;
pub mod inputs;
mod report;

use morgana_ldpc::LdpcCodec;
pub use morgana_ldpc::{DecodeResult, DocsisLdpcCode, LdpcError, LdpcSettings};
pub use report::{FecMetrics, FecReport};

/// A configured single-codeword reference experiment with reusable decoder state.
///
/// This facade does not yet generate an OFDMA waveform or estimate RxMER.
pub struct Morgana {
    settings: LdpcSettings,
    codec: LdpcCodec,
}

impl Morgana {
    /// Constructs a configured, idle upstream FEC experiment.
    ///
    /// # Arguments
    /// * `settings` - Validated selected code, retained information and work limit.
    /// # Returns
    /// Owned independent codec; construction never starts a run.
    /// # Errors
    /// Reports pinned-matrix admission or sparse-encoder construction failures.
    pub fn new(settings: LdpcSettings) -> Result<Self, LdpcError> {
        Ok(Self {
            settings,
            codec: LdpcCodec::new(settings)?,
        })
    }

    /// Runs one noiseless upstream LDPC loop with independent payload comparison.
    ///
    /// # Arguments
    /// * `information` - Exact configured binary information bits; borrowed unchanged.
    /// # Returns
    /// Owned schema-1 report, decoder outcomes and measured payload error counts.
    /// Scratch state is reused; returned snapshots remain valid across later calls.
    /// # Errors
    /// Rejects invalid input size/nonbinary elements. Nonconvergence remains a report.
    pub fn run_ldpc(&mut self, information: &[u8]) -> Result<FecReport, LdpcError> {
        let encoded = self.codec.encode(information)?;
        let llrs: Vec<_> = encoded
            .iter()
            .map(|bit| if *bit == 0 { 20.0 } else { -20.0 })
            .collect();
        let decoded = self.codec.decode(&llrs)?;
        Ok(FecReport::from_decoded(self.settings, information, decoded))
    }
}
