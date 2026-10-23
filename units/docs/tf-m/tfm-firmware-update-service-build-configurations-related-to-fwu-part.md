---
id: "tfm-firmware-update-service-build-configurations-related-to-fwu-part"
type: "concept"
domain: "security"
title: "Firmware Update Service: Build configurations related to FWU partition"
summary: "In this design, component ID ranges from 0 to FWU_COMPONENT_NUMBER - 1. - FWU_SUPPORT_TRIAL_STATE Whether TRIAL component state is supported. - TEST_NS_FWU FWU nonsecure tests switch. - TEST_S_FWU FWU secure tests switch."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#build-configurations-related-to-fwu-partition"
license: "BSD-3-Clause"
mode: "V"
---

- `TFM_PARTITION_FIRMWARE_UPDATE` Controls whether FWU partition is enabled or not.
- `TFM_FWU_BOOTLOADER_LIB` Bootloader configure file for FWU partition.
- `TFM_CONFIG_FWU_MAX_WRITE_SIZE` The maximum permitted size for block in psa_fwu_write, in bytes.
- `TFM_FWU_BUF_SIZE` Size of the FWU internal data transfer buffer (defaults to
  TFM_CONFIG_FWU_MAX_WRITE_SIZE if not set).
- `FWU_STACK_SIZE` The stack size of FWU Partition.
- `FWU_DEVICE_CONFIG_FILE` The device configuration file for FWU partition. The default value is
  the configuration file generated for MCUboot. The following macros should be defined in the
  configuration file:

  - `FWU_COMPONENT_NUMBER` The number of components on the device.


In this design, component ID ranges from 0 to `FWU_COMPONENT_NUMBER` - 1.
  - `FWU_SUPPORT_TRIAL_STATE` Whether TRIAL component state is supported.
- `TEST_NS_FWU` FWU nonsecure tests switch.
- `TEST_S_FWU` FWU secure tests switch.


The running image which supports revert mechanism should be confirmed before initiating a
firmware update process. For example, if the running image is built with
`-DMCUBOOT_UPGRADE_STRATEGY=SWAP_USING_MOVE`, the image should be confirmed either by
adding `-DMCUBOOT_CONFIRM_IMAGE=ON` build option or by calling `psa_fwu_accept()` API
before initiating a firmware update process. Otherwise, `PSA_ERROR_BAD_STATE` will be
returned by `psa_fwu_start()`.
