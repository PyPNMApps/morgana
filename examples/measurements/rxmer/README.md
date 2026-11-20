# Authored upstream RxMER file fixtures

[Source and independent cases](../../../docs/development/features/rxmer-capture/design.md) ·
[Usage](../../../docs/user/rxmer-captures.md)

Copyright 2026 MORGANA contributors. SPDX-License-Identifier: Apache-2.0.
These small invented vectors were frozen before decoder implementation. They are
not device/customer captures, external interoperability evidence, copied source
code or specification pages. Hashes cover decoded hex octets, ignoring whitespace.
No production encoder/decoder generates expected fixture bytes.

| Fixture | Bytes | SHA-256 | Expected observation |
| --- | --- | --- | --- |
| [ccap-50khz.hex](ccap-50khz.hex) | 305 | `ffeadba3dcf58825fad71aa949a61dff0c24adad08f8b656d4a9c8cc552de03c` | Minor0, epoch0x01234567, ifIndex0x10203040, CCAP`ccap.example`, RPD02000000000a/port3, CM020000000001, averages291, raw PreEq1, origin12.8MHz, first128, spacing50kHz. Data005f7f80a0fdfeff gives [0,23.75,31.75,32,40,63.25,63.5,null] dB. |
| [ccap-25khz.hex](ccap-25khz.hex) | 301 | `1ee74407762af69674b866bfb5fde97eef2f45af3fa990252b64813cdd1deb84` | Minor165, epoch0xfedcba98, ifIndex7, CCAP`2001:db8::1`, zero RPD/port, CM020000000002, averages1, raw PreEq0, origin100MHz, first3800, spacing25kHz. Dataff0028fe gives [null,0,10,63.5] dB. |

Source: CCAP-OSSIv3.1-I18 §7.3.2.5 p396, §7.3.3.1/Table397 p397,
§7.3.5.5.7/Table410 pp419–420. Field offsets were manually summed from the
original table before implementation:

| Offset | Bytes | Field |
| --- | --- | --- |
| 0 | 4 | File type504e4e69, distinct from older unversioned PNM prefix. |
| 4 | 1 | Major2. |
| 5 | 1 | Vendor minor, retained verbatim. |
| 6 | 4 | Unsigned capture epoch seconds. |
| 10 | 4 | Upstream ifIndex. |
| 14 | 256 | CCAP-ID raw bytes, including NUL and padding. |
| 270 | 6 | RPD ID. |
| 276 | 1 | RPD port. |
| 277 | 6 | CM MAC. |
| 283 | 2 | Number of averages. |
| 285 | 1 | Raw PreEq flag. Optional0/1 rendering is explicitly limited. |
| 286 | 4 | Subcarrier-zero center frequency in hertz. |
| 290 | 2 | First physical subcarrier index. |
| 292 | 1 | Subcarrier spacing in kHz. |
| 293 | 4 | Exact data byte count. |
| 297 | Count | One quarter-dB byte per contiguous subcarrier, 255 unavailable. |

Multi-octet fixture values use the declared most-significant-octet-first profile.
Minor bytes do not shift the fixed header. The two NUL-terminated text values are
padded to256 bytes without changing their originals. The importer retains arbitrary
raw ID padding/flag bytes even when their semantic rendering is unavailable.

The50kHz vector deliberately exercises all two file octets of the averages field.
Its291 is beyond Table409's UnsignedByte object-model domain: the decoder retains
raw file layout and does not claim this is a valid capture-control request.
The25kHz vector uses the valid model value1. This distinction is retained for
future semantic association rather than silently narrowing the file field.

Explicit invalid/boundary mutations live in `crates/morgana/tests/rxmer_capture.rs`.
They cover every truncated prefix, appended bytes, wrong type/major, unsupported
spacing, missing terminator, counter/grid overflow, exact size limits, empty data,
all256 reading encodings, all256 vendor/flag values and original ownership.
Synthetic all-missing full-grid boundaries test allocation/geometry only; they do
not establish RF conformance or permission to simulate measured input.
