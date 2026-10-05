---
id: "dap-cmsis-dap-firmware-selecting-target-processor"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Selecting target processor"
summary: "The CMSIS-DAP firmware is designed to execute on a debug unit that is using a Cortex-M processor-based microcontroller."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-DAP firmware is designed to execute on a debug unit that is using a Cortex-M processor-based microcontroller.

The following steps describe how to change the target microcontroller in the custom CMSIS-DAP firmware project:

 1. In the µVision IDE, open the project file `Firmware/MyDebugUnit/CMSIS_DAP.uvprojx`.
 2. Open the **Project - Options - Device** dialog and select the microcontroller of the new debug unit.
 4. Optionally, you may modify the project file **Target** name and the file **Abstract.txt** to reflect the new debug unit.

(figure: Select the microcontroller)

In Keil MDK, changing the microcontroller adds relevant software components for the new target. However, depending on the availability you may need to replace some components with custom implementations.

(figure: Replace missing software components)
