---
id: "tfm-details-for-the-platform-folder-debug-authentication-settings"
type: "concept"
domain: "security"
title: "Details for the platform folder: Debug authentication settings"
summary: "A platform may provide the option to configure debug authentication. TF-M core calls the HAL function enum tfm_hal_status_t tfm_hal_platform_init(void) in which debug authentication is configured based on the following defines:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/source_structure/platform_folder.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/platform_folder.html#debug-authentication-settings"
license: "BSD-3-Clause"
mode: "V"
---

A platform may provide the option to configure debug authentication. TF-M core
calls the HAL function `enum tfm_hal_status_t tfm_hal_platform_init(void)`
in which debug authentication is configured based on the following defines:

  - `DAUTH_NONE`: Debugging the system is not enabled.
  - `DAUTH_NS_ONLY`: Invasive and non invasive debugging of non-secure code is
    enabled.
  - `DAUTH_FULL`: Invasive and non-invasive debugging of non-secure and secure
    code is enabled.
  - `DAUTH_CHIP_DEFAULT`: The debug authentication options are used that are set
    by the chip vendor.

The desired debug authentication configuration can be selected by setting one of
the options above to the cmake command with the
`-DDEBUG_AUTHENTICATION="<define>"` option. The default value of
`DEBUG_AUTHENTICATION` is `DAUTH_CHIP_DEFAULT`.

`enum tfm_hal_status_t tfm_hal_platform_init(void)` is called during the
TF-M core initialisation phase, before initialising secure partition. This
means that BL2 runs with the chip default setting.
