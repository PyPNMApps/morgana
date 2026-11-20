/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Independent PHY mask and physical-bin pilot sequence, never payload PRBS.
mod pilot_sequence;
mod randomizer;
pub use pilot_sequence::pilot_reference;
pub use randomizer::Randomizer23;
