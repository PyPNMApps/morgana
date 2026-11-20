/*
 * Copyright 2026 MORGANA contributors
 * SPDX-License-Identifier: Apache-2.0
 */
//! Independent normative arithmetic, closed loops and bounded failure cases.
mod oracle;

use super::*;
use rand::{Rng, SeedableRng};
use rand_chacha::ChaCha8Rng;
use rand_distr::{Distribution, StandardNormal};

fn fixture(code: DocsisLdpcCode, information_bits: usize, iterations: usize) -> LdpcCodec {
    LdpcCodec::new(LdpcSettings::new(code, information_bits, iterations).unwrap()).unwrap()
}

fn information(length: usize) -> Vec<u8> {
    let mut rng = ChaCha8Rng::seed_from_u64(42);
    (0..length)
        .map(|_| u8::from(rng.random::<bool>()))
        .collect()
}

fn llrs(word: &[u8], magnitude: f64) -> Vec<f64> {
    word.iter()
        .map(|bit| if *bit == 0 { magnitude } else { -magnitude })
        .collect()
}

fn systematic_syndrome_and_oracle(code: DocsisLdpcCode) {
    let parameters = code.parameters();
    let codec = fixture(code, parameters.information_bits, 50);
    let original = information(parameters.information_bits);
    let encoded = codec.encode(&original).unwrap();
    assert_eq!(encoded.len(), parameters.codeword_bits);
    assert_eq!(&encoded[..original.len()], &original);
    assert!(codec.valid_syndrome(&encoded));
    assert_eq!(encoded, oracle::encode(code, &original));
    let mut one_hot = vec![0; original.len()];
    one_hot[0] = 1;
    let encoded_one_hot = codec.encode(&one_hot).unwrap();
    assert_eq!(encoded_one_hot, oracle::encode(code, &one_hot));
    // Exercise a byte's MSB-first first bit and the last systematic coordinate.
    one_hot[0] = 0;
    one_hot[original.len() - 1] = 1;
    assert_eq!(
        codec.encode(&one_hot).unwrap(),
        oracle::encode(code, &one_hot)
    );
    for position in [0, original.len() - 1, encoded.len() - 1] {
        let mut corrupted = encoded.clone();
        corrupted[position] ^= 1;
        assert!(!codec.valid_syndrome(&corrupted));
    }
}

fn noiseless(code: DocsisLdpcCode) {
    let parameters = code.parameters();
    let mut codec = fixture(code, parameters.information_bits, 50);
    let original = information(parameters.information_bits);
    let encoded = codec.encode(&original).unwrap();
    let soft = llrs(&encoded, 20.0);
    let retained = soft.clone();
    let result = codec.decode(&soft).unwrap();
    assert!(result.converged && result.parity_valid && result.shortened_zeros_valid);
    assert_eq!(result.information_bits, original);
    assert_eq!(result.mother_codeword, encoded);
    assert_eq!(result.hard_decision_changes, 0);
    assert_eq!(soft, retained);
    assert!(result.iterations <= 50);
    assert_eq!(codec.decode(&soft).unwrap(), result);
    // Finite extremes saturate before entering the decoder.
    assert_eq!(
        codec
            .decode(&llrs(&encoded, f64::MAX))
            .unwrap()
            .information_bits,
        original
    );
}

fn controlled_errors(code: DocsisLdpcCode) {
    let parameters = code.parameters();
    let mut codec = fixture(code, parameters.information_bits, 50);
    let original = information(parameters.information_bits);
    let encoded = codec.encode(&original).unwrap();
    let mut soft = llrs(&encoded, 8.0);
    for position in [
        0,
        parameters.lifting_factor + 3,
        parameters.codeword_bits - 1,
    ] {
        soft[position] *= -0.0625;
    }
    let result = codec.decode(&soft).unwrap();
    eprintln!("{code:?}: controlled iterations={}", result.iterations);
    assert!(result.converged && result.parity_valid);
    assert!(result.iterations > 0 && result.iterations <= 50);
    assert_eq!(result.information_bits, original);
    assert_eq!(result.hard_decision_changes, 3);
}

fn awgn(code: DocsisLdpcCode) {
    let parameters = code.parameters();
    let mut codec = fixture(code, parameters.information_bits, 50);
    let original = information(parameters.information_bits);
    let encoded = codec.encode(&original).unwrap();
    let mut rng = ChaCha8Rng::seed_from_u64(0x4147_4e4c);
    // Real BPSK unit amplitude with real noise variance sigma²=0.16.
    // Natural LLR log(P(0)/P(1)) = 2*y/sigma², not a QAM/Waveform claim.
    let variance: f64 = 0.16;
    let soft: Vec<_> = encoded
        .iter()
        .map(|bit| {
            let sample: f64 = StandardNormal.sample(&mut rng);
            let signal = 1.0 - 2.0 * f64::from(*bit);
            2.0 * (signal + variance.sqrt() * sample) / variance
        })
        .collect();
    let before = encoded
        .iter()
        .zip(&soft)
        .filter(|(bit, llr)| **bit != u8::from(**llr < 0.0))
        .count();
    let result = codec.decode(&soft).unwrap();
    eprintln!(
        "{code:?}: AWGN hard errors={before}, iterations={}",
        result.iterations
    );
    assert!(before > 0);
    assert!(result.converged && result.parity_valid);
    assert_eq!(result.information_bits, original);
    assert!(result.iterations > 0 && result.iterations <= 50);
    assert_eq!(codec.decode(&soft).unwrap(), result);
}

fn failure(code: DocsisLdpcCode) {
    let parameters = code.parameters();
    let mut codec = fixture(code, parameters.information_bits, 1);
    let soft = llrs(&information(parameters.codeword_bits), 1.0);
    let result = codec.decode(&soft).unwrap();
    assert!(!result.converged);
    assert!(!result.parity_valid);
    assert_eq!(result.iterations, 1);
    assert_eq!(result.mother_codeword.len(), parameters.codeword_bits);
    assert_eq!(result.information_bits.len(), parameters.information_bits);
    assert!(result.mother_codeword.iter().all(|bit| *bit <= 1));
}

fn shortening(code: DocsisLdpcCode) {
    let parameters = code.parameters();
    for retained in [
        1,
        420,
        parameters.information_bits - 1,
        parameters.information_bits,
    ] {
        let mut codec = fixture(code, retained, 50);
        let original = information(retained);
        let encoded = codec.encode(&original).unwrap();
        let mut mother_input = original.clone();
        mother_input.resize(parameters.information_bits, 0);
        let mother_word = oracle::encode(code, &mother_input);
        let expected: Vec<_> = mother_word[..retained]
            .iter()
            .chain(&mother_word[parameters.information_bits..])
            .copied()
            .collect();
        assert_eq!(encoded, expected);
        assert_eq!(
            encoded.len(),
            retained + parameters.codeword_bits - parameters.information_bits
        );
        assert!(codec.valid_syndrome(&encoded));
        let result = codec.decode(&llrs(&encoded, 20.0)).unwrap();
        assert!(result.converged && result.parity_valid && result.shortened_zeros_valid);
        assert_eq!(result.information_bits, original);
        assert_eq!(result.mother_codeword, mother_word);
    }
    assert_eq!(
        LdpcSettings::new(code, 0, 1),
        Err(LdpcError::InformationLength)
    );
    assert_eq!(
        LdpcSettings::new(code, parameters.information_bits + 1, 1),
        Err(LdpcError::InformationLength)
    );
}

macro_rules! code_cases {
    ($module:ident, $code:ident) => {
        mod $module {
            use super::*;
            const CODE: DocsisLdpcCode = DocsisLdpcCode::$code;
            #[test]
            fn systematic_syndrome_and_independent_reference() {
                systematic_syndrome_and_oracle(CODE);
            }
            #[test]
            fn exact_noiseless_recovery() {
                noiseless(CODE);
            }
            #[test]
            fn controlled_soft_errors() {
                controlled_errors(CODE);
            }
            #[test]
            fn deterministic_awgn_llrs() {
                awgn(CODE);
            }
            #[test]
            fn bounded_nonconvergence() {
                failure(CODE);
            }
            #[test]
            fn trailing_zero_shortening_boundaries() {
                shortening(CODE);
            }
        }
    };
}

code_cases!(long, UpstreamLong);
code_cases!(medium, UpstreamMedium);
code_cases!(short, UpstreamShort);

#[test]
fn normative_dimensions_shift_direction_and_selected_cells() {
    // Independently read from Table 8 p52 and the three matrix tables p57.
    for (code, expected) in [
        (
            DocsisLdpcCode::UpstreamLong,
            (16200, 14400, 360, 45, [143, 334, 72, 208, 0]),
        ),
        (
            DocsisLdpcCode::UpstreamMedium,
            (5940, 5040, 180, 33, [22, 171, 74, 8, 19]),
        ),
        (
            DocsisLdpcCode::UpstreamShort,
            (1120, 840, 56, 20, [10, 20, 39, 7, 1]),
        ),
    ] {
        let parameters = code.parameters();
        assert_eq!(
            (
                parameters.codeword_bits,
                parameters.information_bits,
                parameters.lifting_factor
            ),
            (expected.0, expected.1, expected.2)
        );
        let shifts = code.shifts();
        assert_eq!(shifts.len(), 5);
        for (row, shifts) in shifts.iter().enumerate() {
            assert_eq!(shifts.len(), expected.3);
            assert_eq!(shifts[expected.3 - 5 + row], expected.4[row]);
            assert!(shifts[expected.3 - 5 + row + 1..]
                .iter()
                .all(|value| *value == -1));
        }
    }
    let short = DocsisLdpcCode::UpstreamShort.matrix().unwrap();
    let row_zero: Vec<_> = short.iter_row(0).copied().collect();
    assert!(row_zero.contains(&5));
    assert!(row_zero.contains(&(56 + 14)));
    assert!(row_zero.contains(&(840 + 10)));
    assert!(!row_zero.contains(&(840 + 46))); // Wrong left-shift convention.
    assert!(short.iter_row(55).any(|column| *column == 849));
    // Matching N/K does not make the downstream DVB matrix an upstream matrix.
    assert_ne!(
        DocsisLdpcCode::UpstreamLong.matrix().unwrap(),
        ldpc_toolbox::codes::dvbs2::Code::R8_9short.h()
    );
}

#[test]
fn invalid_calls_preserve_reusable_decoder_and_slices() {
    let code = DocsisLdpcCode::UpstreamShort;
    for iterations in [0, 101, usize::MAX] {
        assert_eq!(
            LdpcSettings::new(code, 840, iterations),
            Err(LdpcError::IterationLimit)
        );
    }
    let mut codec = fixture(code, 420, 10);
    assert!(matches!(
        codec.encode(&[]),
        Err(LdpcError::InputLength { .. })
    ));
    assert!(matches!(
        codec.encode(&vec![0; 421]),
        Err(LdpcError::InputLength { .. })
    ));
    assert_eq!(codec.encode(&vec![2; 420]), Err(LdpcError::NonBinary));
    assert!(codec.decode(&vec![0.0; 699]).is_err());
    assert!(codec.decode(&vec![0.0; 701]).is_err());
    for invalid in [f64::NAN, f64::INFINITY, f64::NEG_INFINITY] {
        let mut soft = vec![20.0; 700];
        soft[699] = invalid;
        assert_eq!(codec.decode(&soft), Err(LdpcError::NonFiniteLlr));
    }
    assert!(!codec.valid_syndrome(&[]));
    assert!(!codec.valid_syndrome(&vec![2; 700]));
    let result = codec.decode(&vec![20.0; 700]).unwrap();
    assert!(result.converged && result.parity_valid && result.shortened_zeros_valid);
    assert_eq!(result.information_bits, vec![0; 420]);
}

#[test]
fn non_peelable_parity_is_rejected_without_dense_fallback() {
    let mut matrix = ldpc_toolbox::sparse::SparseMatrix::new(2, 3);
    matrix.insert(0, 1);
    matrix.insert(0, 2);
    matrix.insert(1, 1);
    matrix.insert(1, 2);
    assert!(matches!(
        sparse_encoder::SparseEncoder::from_h(&matrix),
        Err(LdpcError::MatrixDefinition)
    ));
}
