/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Ordered indexed transport; exact unity bypass and explicitly supported models.
mod residual;
mod stream;
pub use residual::RxmerChannel;
pub use stream::{Channel, ChannelConfig};
