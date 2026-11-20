/*
 * Copyright 2026 DOCSIS OFDM Channel Sim contributors
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 *
 * Adapted from MERLIN crates/fec-codec/src/sparse_encoder.rs at
 * 096d5a476194d4f2e016863d723b225257bb6037.
 * Modifications: binary u8 buffers, typed errors, upstream use and private API.
 */
//! Sparse substitution plan; setup and encoding visit each recorded edge once.
use crate::LdpcError;
use ldpc_toolbox::sparse::SparseMatrix;
use std::collections::VecDeque;

struct Equation {
    pivot: usize,
    inputs: Vec<usize>,
}

pub(crate) struct SparseEncoder {
    codeword_bits: usize,
    equations: Vec<Equation>,
}

impl SparseEncoder {
    pub(crate) fn from_h(matrix: &SparseMatrix) -> Result<Self, LdpcError> {
        let parity_bits = matrix.num_rows();
        let codeword_bits = matrix.num_cols();
        if parity_bits == 0 || codeword_bits <= parity_bits {
            return Err(LdpcError::MatrixDefinition);
        }
        let information_bits = codeword_bits - parity_bits;
        let mut remaining: Vec<_> = (0..parity_bits)
            .map(|row| {
                matrix
                    .iter_row(row)
                    .filter(|column| **column >= information_bits)
                    .count()
            })
            .collect();
        let mut ready: VecDeque<_> = remaining
            .iter()
            .enumerate()
            .filter_map(|(row, degree)| (*degree == 1).then_some(row))
            .collect();
        let mut solved = vec![false; parity_bits];
        let mut equations = Vec::with_capacity(parity_bits);
        while let Some(row) = ready.pop_front() {
            if remaining[row] != 1 {
                continue;
            }
            let pivot = matrix
                .iter_row(row)
                .copied()
                .find(|column| *column >= information_bits && !solved[*column - information_bits])
                .ok_or(LdpcError::MatrixDefinition)?;
            equations.push(Equation {
                pivot,
                inputs: matrix
                    .iter_row(row)
                    .copied()
                    .filter(|column| *column != pivot)
                    .collect(),
            });
            solved[pivot - information_bits] = true;
            for &dependent in matrix.iter_col(pivot) {
                remaining[dependent] -= 1;
                if remaining[dependent] == 1 {
                    ready.push_back(dependent);
                }
            }
        }
        if equations.len() != parity_bits {
            return Err(LdpcError::MatrixDefinition);
        }
        Ok(Self {
            codeword_bits,
            equations,
        })
    }

    // The owning codec validates complete mother information and binary values.
    pub(crate) fn encode(&self, message: &[u8]) -> Vec<u8> {
        let mut word = vec![0; self.codeword_bits];
        word[..message.len()].copy_from_slice(message);
        for equation in &self.equations {
            word[equation.pivot] = equation
                .inputs
                .iter()
                .fold(0, |parity, column| parity ^ word[*column]);
        }
        word
    }
}
