---
id: "tfm-porting-tf-m-to-a-new-hardware-prerequisites"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: Prerequisites"
summary: "Make sure you have a working build environment and that you can build TF-M on AN521 following the Build instructions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#prerequisites"
license: "BSD-3-Clause"
mode: "V"
---

### Building environment


Make sure you have a working build environment and that you can build
TF-M on AN521 following the
Build instructions.


### Toolchains and software requirements


Please follow the Getting started guide.


### CMSIS Drivers


The TF-M stack requires at least two CMSIS HAL implementations:

    - [USART](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usart__interface__gr.html)
    - [FLASH](https://arm-software.github.io/CMSIS_6/latest/Driver/group__flash__interface__gr.html)
