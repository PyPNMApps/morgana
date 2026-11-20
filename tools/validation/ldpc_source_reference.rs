/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Development-only reference for compact, independently reviewed PHY fixtures.
//!
//! Run the `ldpc-source-reference` example with one private transcription path.
//! Headers are `long 16200 14400 360`, `medium 5940 5040 180` and
//! `short 1120 840 56`, each followed by five whitespace-separated shift rows.
//! A dash denotes an absent block; comment lines start with #. Review the input
//! against original PDF p57, never obtain it from production constants.
//! Output is Rust fixture data on stdout; no destination is opened or replaced.
#![forbid(unsafe_code)]

use std::{collections::BTreeSet, error::Error, fs::File, io::Read};

const MAX_INPUT_BYTES: u64 = 16 * 1024;
const FNV_OFFSET: u64 = 0xcbf2_9ce4_8422_2325;
const FNV_PRIME: u64 = 0x100_0000_01b3;

fn main() -> Result<(), Box<dyn Error>> {
    let mut arguments = std::env::args_os().skip(1);
    let path = arguments.next().ok_or("expected one transcription path")?;
    if arguments.next().is_some() {
        return Err("expected exactly one transcription path".into());
    }
    let mut text = String::new();
    File::open(path)?
        .take(MAX_INPUT_BYTES + 1)
        .read_to_string(&mut text)?;
    if text.len() as u64 > MAX_INPUT_BYTES {
        return Err("transcription exceeds 16 KiB".into());
    }
    let lines: Vec<_> = text
        .lines()
        .map(str::trim)
        .filter(|line| !line.is_empty() && !line.starts_with('#'))
        .collect();
    if lines.len() != 18 {
        return Err("expected three headers and fifteen matrix rows".into());
    }

    let mut output = String::from(
        "/*\n * Copyright 2026 MORGANA contributors\n * SPDX-License-Identifier: Apache-2.0\n */\n\
         //! Frozen source-derived fingerprints and sparse parity, PHY I20 p57.\n\
         //! See docs/development/features/ldpc-source-audit/design.md.\n\
         //! Generated from independent original-page transcription, not production.\n\
         use super::{ImpulseFixture, SourceFixture};\nuse crate::DocsisLdpcCode;\n\n\
         pub(super) const FAMILIES: &[SourceFixture] = &[\n",
    );
    for (family, (name, variant, length, information, lift)) in [
        ("long", "UpstreamLong", 16200, 14400, 360),
        ("medium", "UpstreamMedium", 5940, 5040, 180),
        ("short", "UpstreamShort", 1120, 840, 56),
    ]
    .into_iter()
    .enumerate()
    {
        if lines[family * 6] != format!("{name} {length} {information} {lift}") {
            return Err(format!("unexpected {name} header/dimensions").into());
        }
        let rows: Vec<Vec<i16>> = lines[family * 6 + 1..family * 6 + 6]
            .iter()
            .map(|line| {
                line.split_whitespace()
                    .map(|value| {
                        if value == "-" {
                            Ok(-1)
                        } else {
                            value.parse::<i16>()
                        }
                    })
                    .collect::<Result<_, _>>()
            })
            .collect::<Result<_, _>>()?;
        if rows.iter().any(|row| {
            row.len() != length / lift
                || row.iter().any(|shift| *shift < -1 || *shift >= lift as i16)
        }) {
            return Err(format!("invalid {name} row width or shift").into());
        }
        let information_blocks = information / lift;
        for (row_index, row) in rows.iter().enumerate() {
            if row[information_blocks + row_index] < 0
                || row[information_blocks + row_index + 1..]
                    .iter()
                    .any(|shift| *shift >= 0)
            {
                return Err(format!("{name} parity is not lower triangular").into());
            }
        }

        let fingerprints: Vec<_> = rows
            .iter()
            .map(|row| fingerprint(row.iter().flat_map(|shift| shift.to_le_bytes())))
            .collect();
        let mut edges = Vec::new();
        for (check_block, row) in rows.iter().enumerate() {
            for (variable_block, &shift) in row.iter().enumerate() {
                if shift < 0 {
                    continue;
                }
                for variable_offset in 0..lift {
                    let check =
                        check_block * lift + (variable_offset + lift - shift as usize) % lift;
                    let variable = variable_block * lift + variable_offset;
                    edges.push((check as u32, variable as u32));
                }
            }
        }
        edges.sort_unstable();
        let expanded = fingerprint(edges.iter().flat_map(|(check, variable)| {
            check
                .to_le_bytes()
                .into_iter()
                .chain(variable.to_le_bytes())
        }));
        output.push_str(&format!(
            "    SourceFixture {{\n        code: DocsisLdpcCode::{variant},\n\
             codeword_bits: {length}, information_bits: {information}, lift: {lift},\n\
             row_fingerprints: {fingerprints:?},\n\
             expanded_fingerprint: {expanded}, edge_count: {},\n        impulses: &[\n",
            edges.len()
        ));
        let mut positions = vec![0, lift - 1, lift, information - 1];
        match name {
            "long" => positions.extend([20 * lift, 21 * lift, 39 * lift]),
            "medium" => positions.extend([16 * lift, 17 * lift, 18 * lift, 27 * lift]),
            _ => positions.push(14 * lift),
        }
        positions.sort_unstable();
        positions.dedup();
        for position in positions {
            let parity = impulse_parity(&rows, information_blocks, lift, position);
            output.push_str(&format!(
                "            ImpulseFixture {{ information_one: {position}, parity_ones: &{parity:?} }},\n"
            ));
        }
        output.push_str("        ],\n    },\n");
    }
    output.push_str("] ;\n");
    print!("{output}");
    Ok(())
}

fn fingerprint(bytes: impl IntoIterator<Item = u8>) -> u64 {
    bytes.into_iter().fold(FNV_OFFSET, |hash, byte| {
        (hash ^ u64::from(byte)).wrapping_mul(FNV_PRIME)
    })
}

// Operate on polynomial supports, never an expanded SparseMatrix or decoder.
// In block row j, rotate each known support by diagonal_shift - its_shift,
// XOR the supports, then solve the unit diagonal for parity block j.
fn impulse_parity(
    rows: &[Vec<i16>],
    information_blocks: usize,
    lift: usize,
    information_one: usize,
) -> Vec<usize> {
    let mut parity_blocks: Vec<BTreeSet<usize>> = Vec::new();
    for (row_index, row) in rows.iter().enumerate() {
        let diagonal = row[information_blocks + row_index] as usize;
        let mut support = BTreeSet::new();
        let shift = row[information_one / lift];
        if shift >= 0 {
            support.insert((information_one % lift + diagonal + lift - shift as usize) % lift);
        }
        for (previous, block) in parity_blocks.iter().enumerate() {
            let shift = row[information_blocks + previous];
            if shift < 0 {
                continue;
            }
            for &position in block {
                let rotated = (position + diagonal + lift - shift as usize) % lift;
                if !support.insert(rotated) {
                    support.remove(&rotated);
                }
            }
        }
        parity_blocks.push(support);
    }
    parity_blocks
        .into_iter()
        .enumerate()
        .flat_map(|(block, support)| {
            support
                .into_iter()
                .map(move |position| block * lift + position)
        })
        .collect()
}
