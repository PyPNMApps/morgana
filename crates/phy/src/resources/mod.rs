/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Single physical-resource, pilot-role and joint-address authority.
mod grid;
mod interleaving_blocks;
mod permutation;
mod pilot_patterns;
pub use grid::{Cell, CellRole, ResourcePlan};
pub use interleaving_blocks::block_sizes;
pub use permutation::addresses;
pub use pilot_patterns::role;
