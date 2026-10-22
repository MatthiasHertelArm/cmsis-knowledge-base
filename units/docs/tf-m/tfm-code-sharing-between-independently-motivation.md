---
id: "tfm-code-sharing-between-independently-motivation"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Motivation"
summary: "Cortex-M devices are usually constrained in terms of flash and RAM. Therefore, it is often challenging to fit bigger projects in the available memory."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#motivation"
license: "BSD-3-Clause"
mode: "V"
---

Cortex-M devices are usually constrained in terms of flash and RAM. Therefore,
it is often challenging to fit bigger projects in the available memory. The PSA
specifications require a device to both have a secure boot process in place at
device boot-up time, and to have a partition in the SPE which provides
cryptographic services at runtime. These two entities have some overlapping
functionality. Some cryptographic primitives (e.g. hash calculation and digital
signature verification) are required both in the bootloader and the runtime
environment. In the current TF-M code base, both firmware components use the
mbed-crypto library to implement these requirements. During the build process,
the mbed-crpyto library is built twice, with different configurations (the
bootloader requires less functionality) and then linked to the corresponding
firmware component. As a result of this workflow, the same code is placed in the
flash twice. For example, the code for the SHA-256 algorithm is included in
MCUboot, but the exact same code is duplicated in the SPE cryptography
partition. In most cases, there is no memory isolation between the bootloader
and the SPE, because both are part of the PRoT code and run in the secure
domain. So, in theory, the code of the common cryptographic algorithms could be
reused among these firmware components. This could result in a big reduction in
code footprint, because the cryptographic algorithms are usually flash hungry.
Code size reduction can be a good opportunity for very constrained devices,
which might need to use TF-M Profile Small anyway.
