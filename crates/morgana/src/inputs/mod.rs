/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Bounded configuration and separately verified observation format adapters.
mod rxmer;
mod synthetic;
mod ucd;
mod us_configuration;
pub use rxmer::{RxmerCapture, RxmerHeader};
pub use synthetic::{
    BankDocument, EventDocument, PreEqDocument, ProbeDocument, RxmerDocument,
    RxmerSelectionDocument, UpdateDocument,
};
pub use ucd::{UcdBurst, UcdCapture, UcdHeader, UcdTlv};
pub use us_configuration::{ConfigurationDocument, ConfigurationPreset, RunSettings};
