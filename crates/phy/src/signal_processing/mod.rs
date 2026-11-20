/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Single Rust numerical authority for modulation, transforms and waveform stages.
mod cyclic_extension;
mod demapping;
mod estimation;
mod pre_eq;
mod qam;
mod qam_tables;
mod transform;
mod transmit_window;
pub use cyclic_extension::cyclic_extension;
pub use demapping::max_log;
pub use estimation::{equalize, estimate};
pub use pre_eq::PreEqBank;
pub use qam::{map_symbol, reference_energy};
pub use transform::Transform;
pub use transmit_window::transmit_window;
