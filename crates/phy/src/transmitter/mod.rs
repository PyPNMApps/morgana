/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Bounded composition of the eight upstream transmitter stages.
mod assembly;
mod framer;
mod framing;
pub use assembly::BurstAssembler;
pub use framer::{TransmittedFrame, Transmitter};
pub use framing::encode_grant;
