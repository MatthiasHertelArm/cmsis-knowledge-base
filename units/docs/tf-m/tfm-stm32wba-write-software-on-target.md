---
id: "tfm-stm32wba-write-software-on-target"
type: "concept"
domain: "security"
title: "STM32WBA: Write software on target"
summary: "Connects board to ST-Link USB, then executes the 3 scripts in following order, to program the target: postbuild.sh, regression.sh, TFM_UPDATE.sh"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/stm/stm32wba65i-dk/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/stm32wba65i-dk/.html#write-software-on-target"
license: "BSD-3-Clause"
mode: "V"
---

In build folder (api_ns):

  - `postbuild.sh`: Updates regression.sh and TFM_UPDATE.sh scripts according to flash_layout.h
  - `regression.sh`: Erases flash and configures option bytes on target
  - `TFM_UPDATE.sh`: Programs TFM secure and non-secure appli, and provisions target

Connects board to ST-Link USB, then executes the 3 scripts in following order, to program the target:
postbuild.sh, regression.sh, TFM_UPDATE.sh

The virtual com port from STLINK is used for TFM Applications log and serial port configuration should be:

  - Baud rate    = 115200
  - Data         = 8 bits
  - Parity       = none
  - Stop         = 1 bit
  - Flow control = none

In case of target power-off, the TFM_UPDATE.sh script must be run to program bl2_shared_data RAM area again.

-------------

*Copyright (c) 2026, STMicroelectronics. All rights reserved.*
*SPDX-License-Identifier: BSD-3-Clause*
