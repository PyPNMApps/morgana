/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Executable startup; argument validation and experiments have separate owners.
#![forbid(unsafe_code)]
mod args;
mod command;
mod json_io;

fn main() -> std::process::ExitCode {
    match command::run(std::env::args().skip(1).collect()) {
        Ok(()) => std::process::ExitCode::SUCCESS,
        Err(error) => {
            eprintln!("morgana: {error}");
            std::process::ExitCode::FAILURE
        }
    }
}
