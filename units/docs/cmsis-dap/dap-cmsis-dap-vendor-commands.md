---
id: "dap-cmsis-dap-vendor-commands"
type: "concept"
domain: "debug"
title: "CMSIS-DAP Vendor Commands"
summary: "Extend CMSIS-DAP firmware with commands."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Vendor_gr.html"
license: "Apache-2.0"
mode: "V"
---

Extend CMSIS-DAP firmware with commands.


The CMSIS-DAP firmware may be extended with commands that are specific to a debug unit.

Vendor Commands may implement additional functionality such as interfaces to serial printf-style communication.
The RDDI-DAP interface offers the function `CMSIS_DAP_Commands` to exchange information with vendor-specific commands.
