/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Native conversion only; shared Rust owns bounded offline capture inspection.
use crate::{api, error};
use pyo3::{prelude::*, types::PyBytes};

#[pyclass(from_py_object, frozen, module = "morgana", name = "UcdCapture")]
#[derive(Clone)]
pub(crate) struct PyUcdCapture(api::UcdCapture);

#[pymethods]
impl PyUcdCapture {
    /// Inspects one explicit DA-through-payload message using shared Rust.
    ///
    /// Returns an owned snapshot; malformed and unsupported bytes retain fields
    /// and offsets. No Python parsing, association or simulation work occurs.
    #[staticmethod]
    fn from_mac_management(py: Python<'_>, bytes: &[u8]) -> PyResult<Self> {
        py.detach(|| api::UcdCapture::from_mac_management(bytes))
            .map(Self)
            .map_err(error)
    }

    /// Copies exact source bytes into an owned native Python bytes object.
    ///
    /// Returns immutable bytes that remain valid after this snapshot is dropped.
    fn original_bytes(&self, py: Python<'_>) -> Py<PyBytes> {
        PyBytes::new(py, self.0.original_bytes()).unbind()
    }

    /// Uses shared Rust to hash the exact retained management-message envelope.
    ///
    /// Returns lowercase SHA-256; canonical export never replaces the original.
    fn original_sha256(&self, py: Python<'_>) -> String {
        py.detach(|| self.0.original_sha256())
    }

    /// Uses shared Rust to export bounded versioned structural-inspection JSON.
    ///
    /// Returns owned text containing header/TLV/offset/provenance data only.
    fn to_json(&self, py: Python<'_>) -> PyResult<String> {
        py.detach(|| self.0.to_json()).map_err(error)
    }
}

pub(crate) fn register(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_class::<PyUcdCapture>()?;
    Ok(())
}
