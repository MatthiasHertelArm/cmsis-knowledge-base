---
id: "tfm-stm32l5-write-software-on-target"
type: "concept"
domain: "security"
title: "STM32L5: Write software on target"
summary: "In secure build folder directory api_ns:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/stm/nucleo_l552ze_q/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/stm/nucleo_l552ze_q/.html#write-software-on-target"
license: "BSD-3-Clause"
mode: "V"
---

In secure build folder directory api_ns:

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

*Copyright (c) 2021-2025, Arm Limited. All rights reserved.*
*Copyright (c) 2019, STMicroelectronics. All rights reserved.*
*SPDX-License-Identifier: BSD-3-Clause*
