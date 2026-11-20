/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Actual measured-adapter consumer; fixtures are authored, not modem recordings.
use morgana::api::{ExperimentOptions, ReportJson, Simulation};
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut simulation = Simulation::new(ExperimentOptions::default())?;
    let bytes: &[u8] = if std::env::args().nth(1).as_deref() == Some("25") {
        include_bytes!("../../../examples/measurements/measured/capture-driven-25khz.json")
    } else {
        include_bytes!("../../../examples/measurements/measured/capture-driven.json")
    };
    simulation.configure_measured_json(bytes)?;
    println!("{}", simulation.run()?.to_json()?);
    Ok(())
}
