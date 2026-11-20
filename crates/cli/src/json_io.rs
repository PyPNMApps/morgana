/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Bounded file adapter; no output path, overwrite or scientific implementation.
use std::{fs::File, io::Read, path::Path};
pub(crate) fn read_configuration(path: &Path) -> Result<Vec<u8>, Box<dyn std::error::Error>> {
    let input = File::open(path)?;
    if !input.metadata()?.is_file() {
        return Err("configuration input must be a regular file".into());
    }
    let mut bytes = Vec::new();
    input.take(16 * 1024 * 1024 + 1).read_to_end(&mut bytes)?;
    if bytes.len() > 16 * 1024 * 1024 {
        return Err("configuration exceeds 16 MiB".into());
    }
    Ok(bytes)
}
