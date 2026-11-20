/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Bounded frozen requests, lifecycle and source comparison outside normal RX.
mod control;
mod report;
mod request;
mod run;
pub use control::{ProgressSnapshot, RunControl, RunStatus};
pub use report::{BatchReport, GrantReport, RunFailure};
pub use request::{preview, ExperimentConfig, ExperimentOptions, ExperimentPreview};
pub use run::run;
