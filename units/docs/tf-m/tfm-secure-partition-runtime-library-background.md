---
id: "tfm-secure-partition-runtime-library-background"
type: "concept"
domain: "security"
title: "Secure Partition Runtime Library: Background"
summary: "Trusted Firmware - M (TF-M) uses a toolchain provided runtime library and supervisor calls to easily implement the PSA Firmware Framework (PSA FF) API. This working model works well under isolation level 1 since there are no data isolation requirements."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/secure_partition_runtime_library.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_runtime_library.html#background"
license: "BSD-3-Clause"
mode: "V"
---

Trusted Firmware - M (TF-M) uses a toolchain provided runtime library and
supervisor calls to easily implement the PSA Firmware Framework (PSA FF) API.
This working model works well under isolation level 1 since there are no data
isolation requirements. While TF-M is evolving, this model is not suitable
because:

  - The high-level isolation requires isolating data but some toolchain library
    interfaces have their own global data which cannot be shared between the
    Secure Partitions.
  - The toolchain libraries are designed without taking security as a core
    design principle.

A TF-M specific runtime library is needed for the following reasons:

  - Easier evaluation or certification by security standards.
  - Source code transparency.
  - Sharing code to save ROM and RAM space for TF-M.

PSA FF specification also describes the requirements of C runtime API for Secure
Partitions.

This runtime library is named the `Secure Partition Runtime Library`, and the
abbreviation is `SPRTL`.
