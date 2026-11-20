/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Shared pure FEC grant planning; both endpoints derive layout independently.
mod fec_selection;
mod plan;
pub use fec_selection::select;
pub use plan::{CodewordPlan, GrantPlan};
