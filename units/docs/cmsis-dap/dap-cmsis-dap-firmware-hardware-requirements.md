---
id: "dap-cmsis-dap-firmware-hardware-requirements"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Hardware requirements"
summary: "The CMSIS-DAP firmware is designed for debug units that fulfill the following hardware requirements:"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-DAP firmware is designed for debug units that fulfill the following hardware requirements:

 - Cortex-M processor-based microcontroller.
 - CPU Clock: 48 MHz or higher; microcontroller must have a SYSTICK timer.
 - RAM: 8 KB or more.
 - Flash ROM: 16 KB or more.
 - Full-speed or High-speed USB Device peripheral.
 - 7 standard I/O pins for JTAG/SWD interface.
 - Optionally, 2 I/O pins for status LEDs.
 - Optionally, a UART to support SWO capturing (Rx pin connected to SWO).
 - Optionally, a UART to support an additional UART communication port (for printf debugging).

The figure below illustrates the hardware interfaces of a CMSIS-DAP debug adapter.

(figure: CMSIS-DAP debug unit Hardware)
