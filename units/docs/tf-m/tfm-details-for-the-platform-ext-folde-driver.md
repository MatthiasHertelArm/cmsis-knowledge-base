---
id: "tfm-details-for-the-platform-ext-folde-driver"
type: "concept"
domain: "security"
title: "Details for the platform/ext folder: Sub-folders / driver"
summary: "This folder contains the headers with CMSIS compliant driver definitions that that TF-M project expects a target to provide."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/source_structure/platform_ext_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_ext_folder.html#driver"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Sub-folders_

This folder contains the headers with CMSIS compliant driver definitions that
that TF-M project expects a target to provide.


#### target_cfg.h

This file is expected to define the following macros respectively.

- `TFM_DRIVER_STDIO` - This macro should expand to a structure of type
  `ARM_DRIVER_USART`. TFM redirects its standard input and output to this
  instance of USART.
- `NS_DRIVER_STDIO` - This macro should expand to a structure of type
  `ARM_DRIVER_USART`. Non-Secure application redirects its standard input and
  output to this instance of USART.
