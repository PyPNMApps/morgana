/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Configured-timing received-only receiver; no source seed/payload/C/H input.
mod framing;
pub use framing::{DecodedWord, ReceiveBatch, Receiver};
