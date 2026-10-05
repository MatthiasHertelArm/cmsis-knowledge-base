---
id: "tfm-code-sharing-between-independently-memory-footprint-reduction"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Memory footprint reduction"
summary: "Build type: MinSizeRel Platform: mps2/an521 Version: TF-Mv1.2.0 + code sharing patches MCUboot image encryption support is disabled."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#memory-footprint-reduction"
license: "BSD-3-Clause"
mode: "V"
---

Build type: MinSizeRel
Platform: mps2/an521
Version: TF-Mv1.2.0 + code sharing patches
MCUboot image encryption support is disabled.

+------------------+-------------------+-------------------+-------------------+
|                  |   ConfigDefault   |  ConfigProfile-M  |  ConfigProfile-S  |
+------------------+----------+--------+----------+--------+----------+--------+
|                  | ARMCLANG | GNUARM | ARMCLANG | GNUARM | ARMCLANG | GNUARM |
+------------------+----------+--------+----------+--------+----------+--------+
| CODE_SHARING=OFF |   122268 | 124572 |   75936  |  75996 |    50336 |  50224 |
+------------------+----------+--------+----------+--------+----------+--------+
| CODE_SHARING=ON  |   113264 | 115500 |   70400  |  70336 |    48840 |  48988 |
+------------------+----------+--------+----------+--------+----------+--------+
| Difference       |     9004 |   9072 |    5536  |   5660 |     1496 |   1236 |
+------------------+----------+--------+----------+--------+----------+--------+

If MCUboot image encryption support is enabled then saving could be up to
~13-15KB.


Code sharing on Musca-B1 was tested only with SW only crypto, so crypto
hardware acceleration must be turned off: -DCRYPTO_HW_ACCELERATOR=OFF
