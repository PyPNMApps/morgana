/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Shared synthetic settings only; independent expectations stay in each suite.
use morgana_phy::configuration::*;

/// Constructs explicit bounded synthetic data settings for independent tests.
///
/// Arguments select geometry/loading/pattern, finite frames and physical slots;
/// no expected samples, pilot values, source bits or recovery results are built.
pub fn configuration(
    mode: Numerology,
    loading: u8,
    pattern: u8,
    frames: usize,
    slots: usize,
) -> UsConfiguration {
    let width = mode.carriers_per_minislot();
    let profile = Profile::new(
        224,
        5,
        0x7f_ffff,
        (0..slots)
            .map(|i| Minislot {
                first_carrier: 128 + i * width,
                loading,
                pilot_pattern: pattern,
            })
            .collect(),
    )
    .unwrap();
    let grant = SyntheticGrant {
        id: 7,
        profile_id: 224,
        epoch_sample: 73,
        first_frame: 3,
        frames,
        minislots: (0..slots).collect(),
    };
    UsConfiguration::new(
        Waveform::new(mode, 192, 64, 6, 20_000_000).unwrap(),
        vec![profile],
        grant,
        vec![0, 1],
    )
    .unwrap()
}
