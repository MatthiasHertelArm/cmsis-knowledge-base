---
id: "dap-cmsis-dap-firmware-enabling-swo-trace"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Enabling SWO trace"
summary: "Optionally, you may add a CMSIS-Driver USART to interface to SWO."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

Optionally, you may add a CMSIS-Driver USART to interface to SWO.

A CMSIS-Driver USART can be used to capture the trace output on the SWO pin using a UART RX input on the microcontroller. UART Serial Wire Output (SWO) trace can be enabled and configured in the header `DAP_config.h`. SWO_UART is used to enable the UART SWO and SWO_UART_DRIVER is used to configure USART Driver instance number (Driver_USART#).

Refer to DAP_Config_Debug_gr for more information.
