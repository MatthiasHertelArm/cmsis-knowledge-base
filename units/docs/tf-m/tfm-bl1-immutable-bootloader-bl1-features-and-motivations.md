---
id: "tfm-bl1-immutable-bootloader-bl1-features-and-motivations"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: BL1 Features and Motivations"
summary: "The reference ROM bootloader provides the following features:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#bl1-features-and-motivations"
license: "BSD-3-Clause"
mode: "V"
---

The reference ROM bootloader provides the following features:

- A split between code being stored in ROM and in other non-volatile memory.

  - This can allow significant cost reduction in fixing bugs compared to
    ROM-only bootloaders.

- A secure boot mechanism that allows upgrading the next boot stage (which
  would usually be BL2).

  - This allows for the fixing of any bugs in the BL2 image.
  - Alternately, this could allow the removal of BL2 in some devices that are
    constrained in flash space but have ROM.

- A post-quantum resistant asymmetric signature scheme for verifying the next
  boot stage image.

  - This can allow devices to be securely updated even if attacks
    involving quantum computers become viable. This could extend the lifespans
    of devices that might be deployed in the field for many years.

- A mechanism for passing boot measurements to the TF-M runtime so that they
  can be attested.
- Tooling to create and sign images.
- Fault Injection (FI) and Differential Power Analysis (DPA) mitigations.
