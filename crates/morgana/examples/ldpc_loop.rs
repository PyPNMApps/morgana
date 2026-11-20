/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Minimal Rust facade example: configured upstream LDPC only, no waveform.
use morgana::{DocsisLdpcCode, LdpcSettings, Morgana};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let settings = LdpcSettings::new(DocsisLdpcCode::UpstreamShort, 420, 25)?;
    let mut experiment = Morgana::new(settings)?;
    let information: Vec<_> = (0..420).map(|index| u8::from(index % 3 == 0)).collect();
    let report = experiment.run_ldpc(&information)?;
    println!("{}", report.to_json()?);
    Ok(())
}
