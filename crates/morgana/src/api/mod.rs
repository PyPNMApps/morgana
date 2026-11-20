/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! High-level idle configure/preview/run API; optional adapters share this engine.
mod error;
mod reports;
mod session;
pub use crate::inputs::{
    ConfigurationDocument, ConfigurationPreset, RunSettings, RxmerCapture, RxmerHeader, UcdBurst,
    UcdCapture, UcdHeader, UcdTlv,
};
pub use error::{ApiError, ApiResult, CaptureFailure};
pub use morgana_phy::channel::ChannelConfig;
pub use morgana_phy::instruments::{QamSnapshot, SpectrumSnapshot, Tap};
pub use morgana_phy::measurements::{
    PowerSnapshot, PreEqEvent, PreEqOperation, PreEqPlayback, ProbeReference, RxmerPlayback,
    RxmerPolicy, SyntheticRxmer,
};
pub use morgana_phy::PhyError;
pub use morgana_phy::{
    configuration::{
        BurstMode, Estimator, GuardIntervals, Minislot, Numerology, Profile, ReceiverConfig,
        SyntheticGrant, UsConfiguration, Waveform,
    },
    signal_processing::PreEqBank,
    simulation::{
        BatchReport, ExperimentConfig, ExperimentOptions, ExperimentPreview, GrantReport,
        ProgressSnapshot, RunControl, RunStatus,
    },
    types::Iq,
};
pub(crate) use reports::bounded_json;
pub use reports::ReportJson;
pub use session::Simulation;
