/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Passive bounded owned QAM/SA snapshots; queries never rerun science.
mod metrics;
mod observer;
pub use metrics::{MatchedMer, MerValue};
mod spectrum;
pub use observer::{ObservationStore, QamPoint, QamSnapshot, Tap};
pub use spectrum::SpectrumSnapshot;
