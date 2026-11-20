/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Versioned scientific results with convergence separated from source truth.
use crate::{DecodeResult, LdpcSettings};
use serde::Serialize;

/// Truth comparison for one complete source/codeword trial.
#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct FecMetrics {
    /// Number of original retained information bits transmitted.
    pub payload_bits_transmitted: usize,
    /// Number of retained information decisions, including failed decoder decisions.
    pub payload_bits_recovered: usize,
    /// Independent Hamming distance against the original information bits.
    pub bit_errors: usize,
    /// Bit errors divided by original retained information length.
    pub ber: f64,
    /// Exactly one completed codeword trial in the current facade.
    pub codewords_transmitted: usize,
    /// Count whose decoder convergence, syndrome and shortened-zero checks all pass.
    pub accepted_codewords: usize,
    /// Count failing one or more decoder checks; source errors are measured separately.
    pub failed_codewords: usize,
    /// Actual measured decoder iteration count for each completed trial.
    pub ldpc_iterations: Vec<usize>,
}

/// Owned schema-1 report for a noiseless standalone upstream FEC experiment.
#[derive(Debug, Clone, PartialEq, Serialize)]
pub struct FecReport {
    /// Export schema version; not a DOCSIS revision or workbench version.
    pub schema_version: u32,
    /// Explicit support label preventing FEC trials from being called waveform runs.
    pub experiment: &'static str,
    /// Controlling normative revision and section.
    pub phy_evidence: &'static str,
    /// Exact selected code, shortening and iteration budget.
    pub settings: LdpcSettings,
    /// Independent payload metrics and decoder accounting.
    pub fec: FecMetrics,
    /// Actual final decisions, convergence, syndrome and shortening consistency.
    pub decoded: DecodeResult,
    /// Unavailable until a waveform receiver supplies a meaningful measurement.
    pub rxmer_db: Option<f64>,
}

impl FecReport {
    pub(crate) fn from_decoded(
        settings: LdpcSettings,
        information: &[u8],
        decoded: DecodeResult,
    ) -> Self {
        let bit_errors = information
            .iter()
            .zip(&decoded.information_bits)
            .filter(|(original, recovered)| original != recovered)
            .count();
        let accepted =
            usize::from(decoded.converged && decoded.parity_valid && decoded.shortened_zeros_valid);
        Self {
            schema_version: 1,
            experiment: "standalone_upstream_ldpc_noiseless",
            phy_evidence: "CM-SP-PHYv3.1-I20-230419 section 7.4.3",
            settings,
            fec: FecMetrics {
                payload_bits_transmitted: information.len(),
                payload_bits_recovered: decoded.information_bits.len(),
                bit_errors,
                ber: bit_errors as f64 / information.len() as f64,
                codewords_transmitted: 1,
                accepted_codewords: accepted,
                failed_codewords: 1 - accepted,
                ldpc_iterations: vec![decoded.iterations],
            },
            decoded,
            rxmer_db: None,
        }
    }

    /// Serializes an owned result without selecting or overwriting a destination.
    ///
    /// # Returns
    /// Pretty-printed schema-1 JSON; absent waveform RxMER remains null.
    /// # Errors
    /// Propagates serialization failures; no filesystem state is changed.
    pub fn to_json(&self) -> Result<String, serde_json::Error> {
        serde_json::to_string_pretty(self)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::{DocsisLdpcCode, Morgana};

    #[test]
    fn facade_json_preserves_settings_and_owned_results() {
        let settings = LdpcSettings::new(DocsisLdpcCode::UpstreamShort, 420, 15).unwrap();
        let mut experiment = Morgana::new(settings).unwrap();
        let original = vec![1; 420];
        let first = experiment.run_ldpc(&original).unwrap();
        let _second = experiment.run_ldpc(&vec![0; 420]).unwrap();
        assert_eq!(first.decoded.information_bits, original);
        assert_eq!(first.fec.bit_errors, 0);
        assert_eq!(first.fec.accepted_codewords, 1);
        let json: serde_json::Value = serde_json::from_str(&first.to_json().unwrap()).unwrap();
        assert_eq!(json["schema_version"], 1);
        assert_eq!(json["settings"]["code"], "upstream_short");
        assert_eq!(json["settings"]["information_bits"], 420);
        assert!(json["rxmer_db"].is_null());
        assert!(experiment.run_ldpc(&[]).is_err());
    }

    #[test]
    fn accepted_wrong_word_still_reports_truth_errors() {
        let settings = LdpcSettings::new(DocsisLdpcCode::UpstreamShort, 840, 10).unwrap();
        let mut codec = morgana_ldpc::LdpcCodec::new(settings).unwrap();
        let wrong = codec.decode(&vec![20.0; 1120]).unwrap();
        let report = FecReport::from_decoded(settings, &vec![1; 840], wrong);
        assert_eq!(report.fec.accepted_codewords, 1);
        assert_eq!(report.fec.failed_codewords, 0);
        assert_eq!(report.fec.bit_errors, 840);
        assert_eq!(report.fec.ber, 1.0);
    }
}
