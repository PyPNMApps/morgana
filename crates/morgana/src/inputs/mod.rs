/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Bounded configuration and separately verified observation format adapters.
mod synthetic;
mod us_configuration;
pub use synthetic::{
    BankDocument, EventDocument, PreEqDocument, ProbeDocument, RxmerDocument,
    RxmerSelectionDocument, UpdateDocument,
};
pub use us_configuration::{ConfigurationDocument, ConfigurationPreset, RunSettings};
