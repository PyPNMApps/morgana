# Authored Pre-EQ inspection fixtures

These invented major1 files follow CM-OSSI I27 Tables77/78 pp189–192 in the
explicit MS-octet-first adapter profile. They are not modem recordings.
`applied.hex` uses s2.13 and `last-update.hex` uses s1.14. Header offsets are
type0, major4, minor5, epoch6, UCID10, CM11, CMTS17, RF-zero23, first-bin27,
spacing29, length30, complex I/Q data34. Both have epoch0x01234567, UCID7,
invented CM02:00:00:00:00:01, CMTS02:00:00:00:00:02, origin12.8MHz,
first128, spacing50kHz and16 data bytes (four complex pairs).

Literal expected pairs: (1,0), (1.125,-.25), signed minimum/maximum, then
positive/negative one-LSB. The applied third pair is (-4,3.9998779296875);
update third pair is (-2,1.99993896484375). Missing operation/probe/base/status
is supplied explicitly by a measured experiment, never inferred from file kind.
These short files exercise inspection; they do not cover a complete channel bank.

See the [measured experiment guide](../../../docs/user/measured-experiments.md)
and [format evidence](../../../docs/development/features/remaining-delivery/validation.md).
