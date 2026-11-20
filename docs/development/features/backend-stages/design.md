# Backend stage implementation

The user authorized continuing through the backend stages in dependency order.
The [official checklist](../../checklist.md) owns completion. The
[architecture](../../../architecture.md#planned-code-layout) owns concrete
Add/Edit/Reuse paths; the existing 59 [requirements](../../../requirements.md)
remain mandatory. The staged LDPC checkpoint is retained without index changes.

## First shared contracts and independent cases

DEV-CORE-01 adds the planned `crates/phy` member, typed errors, I/Q, bit/sample
ranges and immutable run/configuration identities. US-CONFIG-01 adds validated
2K/4K waveform geometry, scheduled-data burst admission, profile inventory,
loading/pilot assignments, exclusions and synthetic grant projections. Rust owns
admission; receiver projections contain no source bits, injected channel or C.
No copied reference implementation or new numerical dependency is required for
these foundational value types.

Before implementation: PHY I20 Table 7 p48 fixes fs=102.4 MHz, N=2048/4096,
spacing=50/25 kHz, active-bin maxima 1900/3800 and channel bandwidth bounds.
Tables 9/10 pp67–68 fix CP={96,128,160,192,224,256,288,320,384,512,640} and
RP={0,32,64,96,128,160,192,224}; scheduled data requires RP<CP.
Table 51/§8.2.3.2.1 fixes minimum K=6 and bandwidth-dependent maxima as recorded
in TX-05. Figures 39–42 pp103–105 define physical minislot masks. Each specific
mask and QAM order is enabled only after its source case is recorded and tested.
Raw order/pattern recognition is separate from implemented execution support.

Independent checks precede use: exact table boundaries; K maxima at 48/72 MHz;
NaN/infinite/overflow and duplicate IDs; crossing excluded intervals; IUC selects
a retained profile rather than a hardcoded order; rejected admission preserves
accepted state and source position. Synthetic configuration is not a UCD parser.

## Concrete application budget decision

Reference operation caps: 256 profiles, 1,048,576 loaded/coded bits per grant,
4,096 codewords, 256 grants per job, 16,777,216 cumulative emitted samples,
1,048,576 expanded resource cells and 65,536 retained observation samples.
Default runtime is 30 seconds with a hard maximum of 300 seconds, measured with
a monotonic clock excluding explicitly paused time after pause is implemented.
Caller limits can lower these maxima. Checked arithmetic and aggregate admission
precede allocations/source progress. The frame/codec boundary is the initial
cooperative cancellation quantum; each job preserves completed grants and records
unfinished/unstarted work. No process-wide scheduler or implicit execution.

These are application policy, not DOCSIS conformance limits. The core stays safe
Rust and independent of Python/Qt. Every subsequent stage adds source-checked
expected values here or in a linked validation record before its implementation.

## Source/resource/transform cases recorded before integration

TX-01 capacities 700,1401,3421,6221,11881,16481 independently select respectively
short I=420; short I=420+421; medium I=2521; medium I=4620 + short I=421;
long I=10081; long I=13980 + short I=421. Source count is the total retained
information rounded down to whole bytes; residual bits are ones before FEC.
PRBS seed 1 starts with one, fourteen zeros, then fifteen ones. The full period
is 32767. Figure 7 seed 0x020000 produces mask-one positions
0,5,18,28,36,41,46,51,54 in its first 64 bits.

Figures 11/12 were rendered and inspected for current-counter rejection and the
unreversed diagonal assignment. K=6,L=8 starts
(0,0),(4,4),(2,2),(1,6),(5,1),(3,5),(0,3),(4,7), then (4,0).
Figures 39–42 were inspected for all fourteen edge/body masks, K=6/7 variants,
fixed late complementary positions, and the same-symbol boost exception.
Normal pattern 1 edge K=6 has P at (t,k)=(0,0),(2,0),(0,7),(2,7) and
CP at (3,0),(5,0),(3,7),(5,7). Pattern 8 uses the same times on k=0/15.

QAM lookup will reuse only the applicable preserved Apache PyPNM raw resources
from the inspected reference revision, with original LICENSE/NOTICE and exact
source hashes. No reference crate/runtime dependency is introduced. Raw BPSK
and QPSK rows require label permutations [1,0] and [1,3,0,2]. Original PHY I20
Annex A pp197–198 were rendered: BPSK label0=+1; QPSK labels0..3 are
(1,1),(1,-1),(-1,1),(-1,-1). 8-QAM and cross 32-QAM are separately transcribed
from Figures 101/103; they are absent from the downstream resource inventory.
High orders exclude 8192/16384 upstream. Reference mean energies are fixed by
Table 54 and are tested independently of geometry/observed finite-grant energy.

TX-07/RX-03 reuse the Apache safe Rust radix-2 organization with upstream N.
Before use, an impulse in physical bin N/2 produces constant 1/sqrt(N); bin
N/2+1 produces positive-phase TX exp(j*2*pi*i/N)/sqrt(N). A time impulse gives
constant FFT magnitude 1/sqrt(N). Selected direct sums and Parseval check sign,
centering and unitary scaling independently of a transform round trip.
TX-08 uses literal cyclic suffix from x[0..R], prefix from x[N-C..N] and the
half-sample taper; adjacent symbols start at stride N+C, terminal tail R once.

## Channel extension cases before implementation

Synthetic causal FIR [1,2] applied to real [1,2,3] yields [1,4,7,6], with the
last value emitted only during terminal drain. Integer delay D=2 gives
[0,0,1,2,3] and exactly T+D samples. A phase of pi/2 maps 2+j3 to -3+j2.
Positive CFO rotates toward +j on the emitted sample clock, including leading
delay zeros and final drain. Order is FIR → sample AWGN → integer delay/phase.
Explicit zero impairment settings use a bit-preserving path with no RNG draws.
Sample AWGN uses existing pinned Rust ChaCha8/StandardNormal, real variance v/2
per component and exactly two normal draws per response-output sample. Missing
measurement formats do not enable an RxMER-derived model or inferred inverse C.


## Later adapter gate

The typed high-level Rust reference loop has passed both numerologies, repeated
finite grants, source-contiguous comparison, passive observations and cancellation
before native adapter work. The optional Python adapter will live separately at
`bindings/python/` and retain an independent lock; `crates/morgana` continues to
build/test without Python. Use PyO3 =0.30.1 as in the inspected reference, with
native classes that convert/call the same Rust constructors and operations.
Rust owns all calculations, errors and scientific reports; Python releases the
interpreter while running and exposes Busy through a short-held session slot.
Matching runtime `.pyi` declarations and actual Python/Rust parity are required.

## Measurement and pause extension cases (before implementation)

Pause is cooperative at existing safe boundaries. Acknowledged pause retains the
worker stack and all PRBS, mask, resource, coefficient, RNG, overlap and FIR state.
Monotonic execution budgets exclude acknowledged paused time. Stop wakes a paused
worker. Test uninterrupted versus paused noisy FIR decisions and actual received
support; pre-start pause consumes no source. Native tests exercise real polling,
resume and cancellation, including an actual process SIGINT.

Typed synthetic measurement records precede binary capture import. They retain
explicit synthetic source identities and exact accepted baseband grids, and do
not claim a measured endpoint, epoch or binary decoder. A 10/20 dB pair gives
rho 0.1/0.01 and equal-power average 0.055. At symbol 5 in a 0/10 interpolation
schedule, weights are 0.5/0.5, with hold-last after 10. Missing active readings,
duplicates, wrong grids, bad schedules and incompatible models reject atomically.

Synthetic Pre-EQ replay admits complete snapshots and explicit initialization/
adjustment records. An adjustment naming an older probe base uses that bank,
not the latest applied bank. Independent complex examples use an all-j initial
bank, replacements, and sparse multiplicative updates; whole-bank normalization
is tested separately. Symbol offsets select the complete bank before IFFT and
preserve overlap. Preflight every effective bank before a residual-mode run.

Restricted RxMER synthesis uses rho as absolute normalized per-active-bin error
power, including boosted pilots, and takes two pinned normal draws for every
physical bin before masking. Its own shared IFFT/assembly produces actual noise
samples added once to TX. Identity H, unity C at every event, zero sample AWGN,
and disabled delay/phase are mandatory. Chunking, observers and pause cannot
change the stream. Independent statistics check power and pilot-boost reference;
normal RX receives no target powers, expected grid or channel truth.

## Loader design after accepted Rust/native synthetic loop

The generic US configuration document has its own `morgana.us-configuration`
format and schema 1. Normative `presets[].channel` UCD fields, per-CM assignment
and represented MAP/probe controls are separate from `simulation` settings.
Required fields have no guessed defaults; optional control fields retain omission.
Unknown fields/versions reject, explicit null is permitted only for optional
controls, and old standalone FEC/experiment reports are never configurations.
Parsing/loading remains idle and commits both configuration/options atomically.
Limits are 16 MiB/document, 256 presets, 126 groups/profile, at most 237 minislots,
490 MAP IEs and 128 probe IEs. These are source or application limits as mapped in
the field coverage record. Ranging/probe/testing controls remain inspectable;
execution is scheduled PRBS data only and rejects such a selected mode explicitly.

Implementation owners: Add `crates/phy/src/configuration/ucd/` for source-derived
UCD/domain/projection and applicable control models; Add
`crates/morgana/src/inputs/us_configuration.rs` for bounded versioned document
admission; Edit `crates/morgana/src/api/session.rs` for atomic idle document load;
Edit `bindings/python/src/simulation.rs` and `.pyi` for native dispatch; Edit CLI
adapters for bounded JSON request files. Add independent configuration fixtures,
field/boundary tests and paired Rust/native load/run cases. Keep exhaustive
source-field coverage distinct from waveform execution support.

## Source preservation and scientific wheel review

Generic JSON retains exact original bytes and SHA-256 separately from its resolved
same-schema export, including through native/owned report lifetimes. Hashing uses
pinned RustCrypto sha2 0.10.9 in the facade; no numerical dependency is added to
PHY science. Input schema/output versions remain independent.

Local optimized Linux wheels are tested as actual artifacts, with exact typing,
exports, native parity and full host-reachable dependency license/notice inventory.
Maturin1.8.3 resolves mixed-project include globs relative to the Python source
directory; generated notices are staged there under an explicit ignored path.
The package inventory gate detects missing attribution assets rather than treating
source files as proof of wheel content. A missing proc-macro archive notice is
resolved only against its pinned peer with matching repository, SPDX expression
and exact source VCS commit; no generic substitute notice is fabricated.
