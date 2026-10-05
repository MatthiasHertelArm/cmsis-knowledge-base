---
id: "tfm-platform-provisioning-provisioning-production-hardware"
type: "concept"
domain: "security"
title: "Platform Provisioning: Provisioning production hardware"
summary: "For provisioning of real hardware, firstly TFM_DUMMY_PROVISIONING must be disabled. Then it is required to inject the keys into RAM so they populate the assembly_and_test_prov_data and psa_rot_prov_data structs, at the beginning of the TF-M boot."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/platform_provisioning.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform_provisioning.html#provisioning-production-hardware"
license: "BSD-3-Clause"
mode: "V"
---

For provisioning of real hardware, firstly `TFM_DUMMY_PROVISIONING` must be
disabled. Then it is required to inject the keys into RAM so they populate the
`assembly_and_test_prov_data` and `psa_rot_prov_data` structs, at the
beginning of the TF-M boot. These structs each require a magic value to be set
to be accepted by the provisioning code, which is detailed in
`platform/ext/common/provisioning.c`. Two suggestions for how to do this are:

- Attach a debugger, and inject the values into RAM.
- Flash an image that contains the required data. Care must be taken with this
  approach that the keys are not left in RAM after provisioning, so a different
  image (without provisioning data embedded) must be flashed afterwards, without
  erasing the OTP flash area.


### Provisioning on CryptoCell-312 enabled platforms


On boards that have a CC312 accelerator, and that have the default flash-backed
OTP disabled by setting `PLATFORM_DEFAULT_OTP=OFF` in cmake, the CC312 OTP
will be used as a backing for the OTP HAL.

Due to the CC312 requiring a power-cycle to transition LCS, you will be prompted
to manually power-cycle the board between provisioning stages.

Boards with real OTP memory cannot be reprovisioned - care should be taken that
the data being provisioned is the desired data.


### Platform-specific OTP backing


If a platform has a medium that is suitable for storing data with OTP semantics
(Where a bit cannot transition from a 1 to a 0), such as physical OTP memory,
then it can provide a backing for the OTP HAL by implementing the methods
described in `tfm_plat_otp.h`.

--------------

.. [1] For the definitions of these lifecycle states, please refer to the
       Platform Security Model
       https://developer.arm.com/documentation/den0128/0100/

--------------

*Copyright (c) 2020-2022, Arm Limited. All rights reserved.*
