/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! A bounded, explicit CLI surface for the first executable milestone.
use morgana::{DocsisLdpcCode, LdpcSettings};

pub(crate) const USAGE: &str = "Usage: morgana ldpc <long|medium|short> [information-bits] [seed]\nRuns one noiseless upstream LDPC word; JSON goes to stdout.\nOmit information-bits for the full mother code; seed defaults to 42.\nUse morgana upstream <configuration.json> for the actual bounded\nPRBS to upstream waveform to recovered source experiment.";

pub(crate) struct Arguments {
    pub settings: LdpcSettings,
    pub seed: u64,
}

impl Arguments {
    pub(crate) fn parse(arguments: &[String]) -> Result<Self, String> {
        if !(2..=4).contains(&arguments.len()) || arguments[0] != "ldpc" {
            return Err(USAGE.into());
        }
        let code = match arguments[1].as_str() {
            "long" => DocsisLdpcCode::UpstreamLong,
            "medium" => DocsisLdpcCode::UpstreamMedium,
            "short" => DocsisLdpcCode::UpstreamShort,
            _ => return Err(USAGE.into()),
        };
        let information_bits = match arguments.get(2) {
            Some(value) => value.parse().map_err(|_| "invalid information-bit count")?,
            None => code.parameters().information_bits,
        };
        let seed = match arguments.get(3) {
            Some(value) => value.parse().map_err(|_| "invalid u64 seed")?,
            None => 42,
        };
        Ok(Self {
            settings: LdpcSettings::new(code, information_bits, 50)
                .map_err(|error| error.to_string())?,
            seed,
        })
    }
}
