---
id: "tfm-rollback-protection-in-tf-m-secure-trusted-non-volatile-nv-counters"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Trusted non-volatile (NV) counters"
summary: "The Trusted Base System Architecture (TBSA-M) defines non-volatile (NV) counters or version counters as a counter with the following properties:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#trusted-non-volatile-nv-counters"
license: "BSD-3-Clause"
mode: "V"
---

The Trusted Base System Architecture (TBSA-M) defines non-volatile (NV) counters
or version counters as a counter with the following properties:

 - It must only be possible to increment a version counter through a Trusted
   access.
 - It must only be possible to increment a version counter. It must not be
   possible to decrement it.
 - When a version counter reaches its maximum value, it must not roll over,
   and no further changes must be possible.
 - A version counter must be non-volatile, and the stored value must survive
   a power down period up to the lifetime of the device.

Trusted non-volatile counters can be used to store the value of security
counters per updatable software image. Ideally all independently updatable
software images should have a separate security counter. In current TF-M
implementation the BL2 is not updatable and the secure and non-secure images
are updated together as a single binary. Therefore, one counter is enough to
implement rollback protection. In future the secure and non-secure binaries
will be handled independently; at that time the introduction of a second
counter will be necessary.

Currently the NV counters can be manipulated through the interface described
in `tfm_plat_nv_counters.h`.
