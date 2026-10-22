---
id: "tfm-details-for-the-platform-ext-folde-accelerator"
type: "concept"
domain: "security"
title: "Details for the platform/ext folder: Sub-folders / accelerator"
summary: "This folder contains cmake and code files to interact cryptographic accelerators."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/source_structure/platform_ext_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_ext_folder.html#accelerator"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Sub-folders_

This folder contains cmake and code files to interact cryptographic
accelerators.

In order to use a cryptographic accelerator, a platform must set
`CRYPTO_HW_ACCELERATOR_TYPE` in preload.cmake. This option maps directly to
the subdirectories of the accelerator directory. Currently available
accelerators are : the CryptoCell `cc312`, the STMicroelectronics accelerator
`stm` .

A minimal API is exposed to interact with accelerators, the details of this api
are in `accelerator/interface/crypto_hw.h`. Implementation of the API is
inside the subdirectory of the individual accelerator.

To configure a cryptographic accelerator at build time, two cmake options can be
specified.

- `CRYPTO_HW_ACCELERATOR`
   - `ON` All possible cryptographic operations will be offloaded to
     the accelerator.
   - `OFF` The cryptographic accelerator will be ignored and software
     cryptography will be used.
