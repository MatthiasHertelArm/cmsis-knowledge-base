---
id: "tfm-ff-m-isolation-example-region-numbers-under-isolation-l"
type: "concept"
domain: "security"
title: "FF-M Isolation: Reference Implementation / Example Region Numbers under Isolation Level 3"
summary: "The following table lists the required regions to comply with the rules for implementing isolation level 3. The level 1 and level 2 can be exported by simplifying the items in level 3 table."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#example-region-numbers-under-isolation-level-3"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Reference Implementation_

The following table lists the required regions to comply with the rules for
implementing isolation level 3. The level 1 and level 2 can be exported by
simplifying the items in level 3 table.


**Important:** The table described below is trying to be shared between all supported platforms in Trusted Firmware-M. It is obvious that some platforms have special characteristics. In that case, the specific layout table for a particular platform can be totally redesigned but need to fulfil the isolation level requirements.

- Only the running partition's assets are covered since the inactive partitions
  do not need regions.
- `X` indicates the existence of this region can't comply with the rule.
- An `ATTR + n` represent extra `n` regions are necessary.
- The table assumes each rule is in addition to the rules in previous columns
  (but the FF-M permits any combination of optional rules).

The following table lists the required regions to comply with the rules:

+-------------------+-------------+-------------+-------------+-------------+
| Region Purpose    | I1 I2 I3 I7 | I4          | I5          | I6          |
+===================+=============+=============+=============+=============+
| PRoT SPM Code     | A_RO        | P_RO        | P_RO        | P_RO        |
+-------------------+             |             |             +-------------+
| PRoT Service Code |             |             |             | A_ROPXN     |
+-------------------+             +-------------+-------------+             |
| Active Partition  |             | A_RO        | A_ROPXN     |             |
| Code              |             |             |             |             |
+-------------------+             +-------------+-------------+-------------+
| SPRTL Code        |             | A_RO        | A_RO        | `X`       |
+-------------------+-------------+-------------+-------------+-------------+
| PRoT SPM RO       | A_ROXN      | P_ROXN      | P_ROXN      | P_ROXN      |
+-------------------+             |             |             +-------------+
| PRoT Service RO   |             |             |             | A_ROXN      |
+-------------------+             +-------------+-------------+             |
| Active Partition  |             | A_ROXN      | A_ROXN      |             |
| RO                |             |             |             |             |
+-------------------+             +-------------+-------------+-------------+
| SPRTL RO          |             | A_ROXN      | A_ROXN      | `X`       |
+-------------------+-------------+-------------+-------------+-------------+
| PRoT SPM RW       | P_RWXN      | P_RWXN      | P_RWXN      | P_RWXN      |
+-------------------+             |             |             +-------------+
| PRoT Service RW   |             |             |             | A_RWXN      |
+-------------------+-------------+-------------+-------------+             |
| Active Partition  | A_RWXN      | A_RWXN      | A_RWXN      |             |
| RW                |             |             |             |             |
+-------------------+-------------+-------------+-------------+-------------+
| SPRTL RW [5]      | A_RWXN + 1  | A_RWXN + 1  | A_RWXN + 1  | `X`       |
+-------------------+-------------+-------------+-------------+-------------+
| Partition Periph  | A_RWXN + n  | A_RWXN + n  | A_RWXN + n  | A_RWXN + n  |
+-------------------+-------------+-------------+-------------+-------------+
| Total Numbers     | [1]         | [2]         | [3]         | [4]         |
+-------------------+-------------+-------------+-------------+-------------+


**Note:** 1. Total number = A_RO + A_ROXN + P_RWXN + (2 + n)A_RWXN = `5 + n`, where `n` is the maximum number of peripherals needed by one partition. 2. Total number = [1] + P_RO + A_RO + P_ROXN + A_ROXN = `9 + n` (or `6 + n` without SPRTL). 3. Total number = [2] = `9 + n`, and Armv8.1-M PXN is required. 4. Total number = P_RO + A_ROPXN + P_ROXN + A_ROXN + P_RWXN + (1 + n)A_RWXN = `6 + n`, but SPRTL cannot be used, and Armv8.1-M PXN is required. To comply with this rule, the PSA RoT Services need to be implemented as Secure Partitions. 5. This data belongs to SPRTL RW but it is set as Read-Only and only SPM can update this region with the active partition's metadata for implementing functions with owner SP's context, such as heap functions. This region can be skipped if there is no metadata required (such as no heap functionalities required). The memory-mapped regions for peripherals have different memory access attributes in general, they are standalone regions in the MPU even though their attributes covers 'A_RWXN'.

TF-M provides the reference linker scripts `tfm_isolation_s.sct.template`,
`tfm_isolation_s.ld.template`, and `tfm_isolation_s.icf.template` for the
Armclang, GCC, and IAR compilers in the `platform/ext/common` directory. These
linker scripts arrange the SPE's memory by attribute to aid the implementation
of the isolation rules.

The reference isolation HAL for Armv8-M and Armv8.1-M platforms in
`platform/ext/common/tfm_hal_isolation_v8m.c` uses the memory position tags
defined by the linker scripts to set up the MPU region base and limit addresses.
It implements isolation rules I1, I2, I3 and I7 for isolation levels 1 to 3. It
partially implements rule I4 by statically partitioning code into privileged and
unprivileged read-only regions but collecting all constant data into a single
unprivileged, read-only, execute-never region, which provides a good level
of protection against ROP attacks by limiting the amount of executable memory.
On Armv8.1-M targets, it statically configures all Application RoT Partition
code as PXN, which is sufficient to satisfy rule I5 in isolation level 2, but
not in isolation level 3, where it would require dynamically mapping only the
active partition's code region.

TF-M platforms may replace the reference linker scripts and/or isolation HAL
with a customized implementation, but it must meet at least isolation rules I1,
I2 and I3 to comply with the PSA security model.
