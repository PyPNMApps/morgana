/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 * Embedded larger tables retain preserved PyPNM Apache LICENSE/NOTICE under
 * resources/qam-table; see provenance.json for upstream source/hashes.
 */
//! Integer source coordinates, indexed by the MSB-first cell-word label.
include!(concat!(env!("OUT_DIR"), "/qam_tables.rs"));

// Independently transcribed PHY I20 Figure 101, p198 (not rectangular Gray QAM).
const QAM8: [[i16; 2]; 8] = [
    [1, -3],
    [-1, -1],
    [3, -1],
    [1, 1],
    [-3, -3],
    [-3, 1],
    [3, 3],
    [-1, 3],
];

// Independently transcribed Figure 103, p198, including the four missing corners.
const QAM32: [[i16; 2]; 32] = [
    [3, 5],
    [5, 3],
    [1, 5],
    [5, 1],
    [1, 3],
    [3, 3],
    [1, 1],
    [3, 1],
    [3, -5],
    [5, -3],
    [1, -5],
    [5, -1],
    [1, -3],
    [3, -3],
    [1, -1],
    [3, -1],
    [-3, 5],
    [-5, 3],
    [-1, 5],
    [-5, 1],
    [-1, 3],
    [-3, 3],
    [-1, 1],
    [-3, 1],
    [-3, -5],
    [-5, -3],
    [-1, -5],
    [-5, -1],
    [-1, -3],
    [-3, -3],
    [-1, -1],
    [-3, -1],
];

pub(super) fn coordinates(bits: u8) -> Option<&'static [[i16; 2]]> {
    match bits {
        3 => Some(&QAM8),
        5 => Some(&QAM32),
        _ => TABLES
            .iter()
            .find(|(loading, _)| *loading == bits)
            .map(|(_, points)| *points),
    }
}
