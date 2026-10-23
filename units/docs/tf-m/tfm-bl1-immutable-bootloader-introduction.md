---
id: "tfm-bl1-immutable-bootloader-introduction"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: Introduction"
summary: "Some devices that use TF-M will require initial boot code that is stored in ROM. There are a variety of reasons that this might happen:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

Some devices that use TF-M will require initial boot code that is stored in ROM.
There are a variety of reasons that this might happen:

- The device cannot access flash memory without a driver, so needs some setup
  to be done before main images on flash can be booted.
- The device has no on-chip secure flash, and therefore cannot otherwise
  maintain a tamper-resistant root of trust.
- The device has a security model that requires an immutable root of trust

Henceforth any bootloader stored in ROM will be referred to as BL1, as it would
necessarily be the first stage in the boot chain.

TF-M provides a reference second-stage flash bootloader BL2, in order to allow
easier integration. This bootloader implements all secure boot functionality
needed to provide a secure chain of trust.

A reference ROM bootloader BL1 has now being added with the same motivation -
allowing easier integration of TF-M for platforms that do not have their own
BL1 and require one.
