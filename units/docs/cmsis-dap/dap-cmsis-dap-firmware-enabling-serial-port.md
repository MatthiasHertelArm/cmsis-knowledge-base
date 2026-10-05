---
id: "dap-cmsis-dap-firmware-enabling-serial-port"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Enabling serial port"
summary: "Optionally, you may add a CMSIS-Driver USART to interface to UART communication port."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

Optionally, you may add a CMSIS-Driver USART to interface to UART communication port.

A CMSIS-Driver USART can be used to receive data from the target and transmit data to the target using UART RX and TX pins on the microcontroller. The UART communication port can be enabled and configured in the header `DAP_config.h`. DAP_UART is used to enable the UART communication port and DAP_UART_DRIVER is used to configure USART Driver instance number (Driver_USART#).

Refer to DAP_Config_Debug_gr for more information.
