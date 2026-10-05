---
id: "dap-cmsis-dap-firmware-create-firmware-project"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Firmware: Create firmware project"
summary: "To create CMSIS-DAP firmware that can be used on a different debug unit copy an existing firmware adaptation to a new folder. For example, copy the folder  Firmware/Examples/MCU-LINK to a folder called /Firmware/MyDebugUnit."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/dap_firmware.md"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/dap_firmware.html"
license: "Apache-2.0"
mode: "V"
---

To create CMSIS-DAP firmware that can be used on a different debug unit copy an existing firmware adaptation to a new folder. For example, copy the folder ` Firmware/Examples/MCU-LINK` to a folder called `/Firmware/MyDebugUnit`.

Following steps describe the adaptation of the CMSIS-DAP firmware to a new debug unit:
 1. dap_config_mcu :  Select the microcontroller and replace the CMSIS-Core (Cortex-M) files.
 2. dap_config_io : Adapt the I/O ports and specify other parameters for the debug unit.
 3. dap_usart_swo : Optionally, you may add a CMSIS-Driver USART to interface to SWO.
 4. dap_usart_com : Optionally, you may add a CMSIS-Driver USART to interface to UART communication port.
 5. dap_config_usb : Adapt the USB peripheral to the microcontroller.
 6. DAP_Vendor_gr : Optionally, you may add vendor specific commands to the debug unit.
 7. dap_config_flash : Program the adapted firmware to the Flash ROM of the new debug unit.
 8. dap_validate : Validate the CMSIS-DAP firmware of the new debug unit.
