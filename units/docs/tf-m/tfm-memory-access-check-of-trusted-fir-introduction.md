---
id: "tfm-memory-access-check-of-trusted-fir-introduction"
type: "concept"
domain: "security"
title: "Memory Access Check of Trusted Firmware-M in Multi-Core Topology: Introduction"
summary: "On Armv8-M platforms with TrustZone, the platform's TF-M isolation HAL implementation usually relies on the Armv8-M Security Extension (CMSE) intrinsic cmse_check_address_range() to check memory access permissions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/tfm_multi_core_access_check.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/tfm_multi_core_access_check.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

On Armv8-M platforms with TrustZone, the platform's TF-M isolation HAL implementation usually relies
on the Armv8-M Security Extension (CMSE) intrinsic `cmse_check_address_range()` to check memory
access permissions. However, on multi-core platforms, the secure core may be an Armv6-M or Armv7-M
core that does not implement CMSE. Even if CMSE is implemented on a multi-core platform, additional
checks on system-level security and memory access management units may be required since CMSE
intrinsics and TT instructions are only aware of MPU/SAU/IDAU inside the secure core.

As a result, TF-M provides a common platform memory access check API and an implementation that
works without CMSE support. Multi-core topology platforms may use the memory check API
`tfm_has_access_to_region()`, which checks whether an access has proper permission to read or
write the target memory region, as a substitute for `cmse_check_address_range()` when implementing
the TF-M isolation HAL.

The memory check API is defined in `platform/ext/common/mem_check_v6m_v7m.h` and the common
implementation is provided in `platform/ext/common/mem_check_v6m_v7m.c`. The HAL defined in
`platform/ext/common/mem_check_v6m_v7m_hal.h` must be implemented by each platform that uses the
common implementation. This document discusses the design of the memory access check API and
implementation.
