---
id: "dap-cmsis-dap-firmware-programming-into-debug-unit"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Programming into debug unit"
summary: "Once the CMSIS-DAP firmware is configured and built, it needs to be programmed into the Flash ROM of the new debug unit."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

Once the CMSIS-DAP firmware is configured and built, it needs to be programmed into the Flash ROM of the new debug unit.

Keil MDK provides Flash algorithms for many Cortex-M based microcontrollers and therefore you may use the Flash programming facilities that are provide in µVision. Once Flash programming is configured, you may use the µVision menu item **Flash - Download**.

(figure: Download CMSIS-DAP firmware to new debug unit using MDK)
