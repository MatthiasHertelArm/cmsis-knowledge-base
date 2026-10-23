---
id: "tfm-firmware-update-service-components"
type: "concept"
domain: "security"
title: "Firmware Update Service: Components"
summary: "The structure of the TF-M Firmware Update service is listed below: +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+ | Component name | Description | Location | +=============================+===============================================================+=======================================================================================+ | Client API interface | This module exports the client API of PSA Firmware Update to | …"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#components"
license: "BSD-3-Clause"
mode: "V"
---

The structure of the TF-M Firmware Update service is listed below:
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | **Component name**          | **Description**                                               | **Location**                                                                          |
   +=============================+===============================================================+=======================================================================================+
   | Client API interface        | This module exports the client API of PSA Firmware Update to  | `./interface/src/tfm_fwu_api.c`                                                     |
   |                             | the users.                                                    |                                                                                       |
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | Manifest                    | The manifest file is a description of the service components. | `./secure_fw/partitions/firmware_update/tfm_firmware_update.yaml`                   |
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | NSPE client API interface   | This module exports the client API of PSA Firmware Update to  | `./interface/src/tfm_fwu_api.c`                                                     |
   |                             | the NSPE(i.e. to the applications).                           |                                                                                       |
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | IPC request handlers        | This module handles all the secure requests in IPC model.     | `./secure_fw/partitions/firmware_update/tfm_fwu_req_mngr.c`                         |
   |                             | It maintains the image state context and calls the image ID   |                                                                                       |
   |                             | converter to achieve the firmware update functionalities.     |                                                                                       |
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | Shim layer between FWU and  | This module provides the APIs with the functionality of       | `./secure_fw/partitions/firmware_update/bootloader/tfm_bootloader_fwu_abstraction.h`|
   | bootloader                  | operating the bootloader to cooperate with the Firmware Update|                                                                                       |
   |                             | service                                                       |                                                                                       |
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | Shim layer example based on | This module is the implementation of the shim layer between   | `./secure_fw/partitions/firmware_update/bootloader/mcuboot/tfm_mcuboot_fwu.c`       |
   | MCUboot                     | FWU and bootloader based on MCUboot.                          |                                                                                       |
   |                             |                                                               |                                                                                       |
   +-----------------------------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
