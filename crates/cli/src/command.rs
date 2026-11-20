/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! One bounded fixture experiment; scientific processing remains in Rust libraries.
use crate::args::{Arguments, USAGE};
use morgana::Morgana;
use rand::{Rng, SeedableRng};
use rand_chacha::ChaCha8Rng;

pub(crate) fn run(arguments: Vec<String>) -> Result<(), Box<dyn std::error::Error>> {
    if arguments.len() == 1 && arguments[0] == "--help" {
        println!("{USAGE}");
        return Ok(());
    }
    if arguments.len() == 1 && arguments[0] == "--version" {
        println!("MORGANA {}", env!("CARGO_PKG_VERSION"));
        return Ok(());
    }
    let arguments = Arguments::parse(&arguments)?;
    let mut rng = ChaCha8Rng::seed_from_u64(arguments.seed);
    let information: Vec<_> = (0..arguments.settings.information_bits())
        .map(|_| u8::from(rng.random::<bool>()))
        .collect();
    let mut experiment = Morgana::new(arguments.settings)?;
    let report = experiment.run_ldpc(&information)?;
    let document = serde_json::json!({
        "schema_version": 1,
        "source": {"kind": "chacha8_fixture", "seed": arguments.seed},
        "report": report,
    });
    println!("{}", serde_json::to_string_pretty(&document)?);
    if report.fec.failed_codewords != 0 || report.fec.bit_errors != 0 {
        return Err("reference loop did not recover the exact original payload".into());
    }
    Ok(())
}
