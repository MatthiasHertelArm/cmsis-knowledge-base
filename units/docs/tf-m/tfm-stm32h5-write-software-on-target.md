---
id: "tfm-stm32h5-write-software-on-target"
type: "concept"
domain: "security"
title: "STM32H5: Write software on target"
summary: "Connect board to USB and Execute the 3 scripts in following order to update platform: postbuild.sh, regression.sh, TFM_UPDATE.sh"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32h573i_dk/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32h573i_dk/.html#write-software-on-target"
license: "BSD-3-Clause"
mode: "V"
---

In build folder:

  - `postbuild.sh`: Updates regression.sh and TFM_UPDATE.sh scripts according to flash_layout.h
  - `regression.sh`: Sets platform option bytes config and erase platform
  - `TFM_UPDATE.sh`: Writes bl2, secure, and non secure image in target


Connect board to USB and Execute the 3 scripts in following order to update platform:
postbuild.sh, regression.sh, TFM_UPDATE.sh

The virtual com port from STLINK is used for TFM log and serial port configuration should be:

  - Baud rate    = 115200
  - Data         = 8 bits
  - Parity       = none
  - Stop         = 1 bit
  - Flow control = none

-------------

*Copyright (c) 2023, STMicroelectronics. All rights reserved.*
*SPDX-License-Identifier: BSD-3-Clause*
