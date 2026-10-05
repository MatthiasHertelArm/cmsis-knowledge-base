---
id: "tfm-porting-tf-m-to-a-new-hardware-file-architecture"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: File architecture"
summary: "The platform selection when building TF-M is set via the CMake variable TFM_PLATFORM. This variable holds part of the path to the platform. When using -DTFM_PLATFORM=arm/mps2/an521 or -DTFM_PLATFORM=an521 TF-M build system will look for the platform in <TF-M ROOT>/platform/ext/target/arm/mps2/an521."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#file-architecture"
license: "BSD-3-Clause"
mode: "V"
---

The platform selection when building TF-M is set via the CMake
variable TFM_PLATFORM. This variable holds part of the path to the platform.
When using `-DTFM_PLATFORM=arm/mps2/an521` or `-DTFM_PLATFORM=an521`
TF-M build system will look for the platform in
<TF-M ROOT>/platform/ext/target/arm/mps2/an521.
Therefore all hardware dependent code for your platform should go to
<TF-M ROOT>/platform/ext/target/.


### platform/ext/target

This folder contains a first level of board vendor (such as ARM, STM, NXP,
Cypress ....), each folder will usually contain a second level for each
board. This second level is not mandatory.

    platform/ext/target/<vendor>/[<board name>/]

From now on this will be referred to as the `platform folder`.


### platform/ext/common

This folder contains files and folder commons to the platforms, such as the
shims to the CMSIS drivers. It also contains the scatter files that can be
used for the bl2, tfm_s, tfm_ns partitions.

This folder also contains another folder named template. The latter contains
example implementations that are used for platforms by default, but which can be
altered or replaced if other functionality is required.

    +------------------------------+-----------------------------------------------------------------------------+
    |    name                      |        description                                                          |
    +==============================+=============================================================================+
    |PLATFORM_DEFAULT_ATTEST_HAL   |Use the default implementation of the attestation HAL (default True)         |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_NV_COUNTERS  |Use the default implementation of the counters in NV (default True)          |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_CRYPTO_KEYS  |Use the default implementation of crypto keys (default True)                 |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_ROTPK        |Use the default implementation of the RoT Public Key (default True)          |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_IAK          |Use the default implementation of the initial attestation key (default True) |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_UART_STDOUT  |Use the default implementation of the uart for stdout output (default True)  |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_NV_SEED      |Use the default implementation of the NV seed in the RNG (default True)      |
    +------------------------------+-----------------------------------------------------------------------------+
    |PLATFORM_DEFAULT_OTP          |Use the default implementation of the OTP (default True)                     |
    +------------------------------+-----------------------------------------------------------------------------+
