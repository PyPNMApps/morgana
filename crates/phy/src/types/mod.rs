/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Units, coordinates and owned scientific buffers shared by stages.
mod bits;
mod iq;
mod samples;

pub use bits::{BitRange, Identity, SourceChunk};
pub use iq::Iq;
pub use samples::SampleBlock;
