---
id: "tfm-porting-tf-m-to-a-new-hardware-porting-flow"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: Porting flow"
summary: "In a nutshell, this should be a 6 iterative steps process:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#porting-flow"
license: "BSD-3-Clause"
mode: "V"
---

In a nutshell, this should be a 6 iterative steps process:

    #. Adding all the mandatory files and expected objects/functions declarations

    #. Booting and configuring the core(s)

        - startup(s) code and SystemInit

    #. Adding the USART drivers

        - CMSIS HAL

    #. Adding the FLASH drivers

        - CMSIS HAL

    #. Enabling/Configuring/Disabling features including templated features

        - E.G. NV Counters, attestation, crypto keys....

    #. Adding the optional platform SVC handling

        Some platforms may have their own SVC requests in addition to the TF-M built-in ones.

    #. Running the regression tests

        - See Running TF-M on Arm platforms
          as an example
