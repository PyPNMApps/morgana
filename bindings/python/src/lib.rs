/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Optional native conversion/dispatch only; core builds never require Python.
mod configuration;
mod document;
mod measurements;
mod reports;
mod simulation;
use morgana::api;
use pyo3::{exceptions::PyException, prelude::*};

pyo3::create_exception!(_native,ApiError,PyException,"Shared Rust validation/dispatch failure. Read code and field; scientific failures remain reports.");

fn error(error: impl Into<api::ApiError>) -> PyErr {
    let error = error.into();
    Python::attach(|py| {
        let exception = ApiError::new_err(error.to_string());
        let _ = exception.value(py).setattr("code", error.code());
        let field = match &error {
            api::ApiError::Domain(
                morgana::api::PhyError::InvalidInput { field }
                | morgana::api::PhyError::ResourceLimit { field }
                | morgana::api::PhyError::Unsupported { field }
                | morgana::api::PhyError::Association { field },
            ) => Some(*field),
            _ => None,
        };
        let _ = exception.value(py).setattr("field", field);
        exception
    })
}

/// Registers actual native exports without importing or executing simulation.
///
/// `module` receives Rust classes and version metadata; returns import status.
#[pymodule]
fn _native(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add("__version__", env!("CARGO_PKG_VERSION"))?;
    module.add("ApiError", module.py().get_type::<ApiError>())?;
    configuration::register(module)?;
    document::register(module)?;
    simulation::register(module)?;
    reports::register(module)?;
    measurements::register(module)?;
    Ok(())
}
