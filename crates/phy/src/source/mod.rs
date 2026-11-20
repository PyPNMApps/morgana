/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Continuous reproducible payload source and independent contiguous verifier.
mod prbs15;
mod verifier;
pub use prbs15::Prbs15;
pub use verifier::{Comparison, PrbsVerifier};
