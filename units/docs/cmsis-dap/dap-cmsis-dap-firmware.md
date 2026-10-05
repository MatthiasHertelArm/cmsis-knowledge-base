---
id: "dap-cmsis-dap-firmware"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware"
summary: "The CMSIS-DAP firmware implements the CMSIS-DAP concept. The firmware is provided in a source code in CMSIS-DAP GitHub repository with several reference implementations for popular debug units. The table below explains the directory structure."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-DAP firmware implements the CMSIS-DAP concept. The firmware is provided in a source code in [**CMSIS-DAP GitHub repository**](https://github.com/ARM-software/CMSIS-DAP) with several reference implementations for popular debug units. The table below explains the directory structure.

Folders and Files                     | Description
:-------------------------------------|:-----------------------------------------------------------------------
📂 Firmware                           | Folder with CMSIS-DAP Firmware.
 ┣ 📄 Config/DAP_config.h             | CMSIS-DAP firmware configuration file. See dap_config_io.
 ┣ 📂 Examples                        | CMSIS-DAP firmware adapted to various debug units. See dap_fw_examples.
 ┣ 📂 Include                         | CMSIS-DAP firmware header file.
 ┣ 📂 Source                          | CMSIS-DAP firmware source code.
 ┣ 📂 Template                        | Interface templates for Keil MDK-Middleware.
 ┗ 📂 Validation                      | Validation project. See dap_validate.

The implementation is composed of the following components:

 - CMSIS-DAP firmware that interfaces to JTAG or SWD pins using standard I/O pins of the Cortex-M device.
 - CMSIS-Driver USART that connects:
   - the UART of the Cortex-M device to the SWO output from the target.
   - an additional UART of the Cortex-M device to the UART from the target.
 - USB stack that interfaces to the USB port of the host computer using:
   - a custom class (for USB bulk endpoints),
   - the CDC ACM class to export USB COM Port.
 - The USB Device middleware may require CMSIS-RTOS and a CMSIS-Driver USB.
