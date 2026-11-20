/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Run the canonical generic JSON fixture through the public Rust API.
use morgana::api::*;
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let bytes: &[u8] = if std::env::args().nth(1).as_deref() == Some("synthetic") {
        include_bytes!("../../../examples/configuration/us-synthetic-playback.json")
    } else {
        include_bytes!("../../../examples/configuration/us-50khz.json")
    };
    let document = ConfigurationDocument::from_json(bytes)?;
    let mut session = Simulation::new(ExperimentOptions::default())?;
    session.configure_document(document)?;
    let report = session.run()?;
    if !report.reference_recovered {
        return Err("configuration experiment did not recover source".into());
    }
    println!("{}", report.to_json()?);
    Ok(())
}
