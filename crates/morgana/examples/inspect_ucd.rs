/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Independently executed Rust consumer of the frozen source-derived fixtures.
use morgana::api::UcdCapture;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut outputs = Vec::new();
    for fixture in [
        include_str!("../../../examples/measurements/ucd/minimal.hex"),
        include_str!("../../../examples/measurements/ucd/scheduled-50khz.hex"),
    ] {
        let text: String = fixture.chars().filter(|c| !c.is_whitespace()).collect();
        let bytes = text
            .as_bytes()
            .chunks_exact(2)
            .map(|pair| {
                u8::from_str_radix(std::str::from_utf8(pair)?, 16)
                    .map_err(Box::<dyn std::error::Error>::from)
            })
            .collect::<Result<Vec<_>, _>>()?;
        let capture = UcdCapture::from_mac_management(&bytes)?;
        outputs.push(serde_json::from_str::<serde_json::Value>(
            &capture.to_json()?,
        )?);
    }
    println!("{}", serde_json::to_string(&outputs)?);
    Ok(())
}
