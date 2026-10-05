---
id: "dap-response-status"
type: "concept"
domain: "debug"
title: "Response Status"
summary: "The Response data of a command frequently include a Status that indicates correct execution or command failures."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Response_Status.html"
license: "Apache-2.0"
mode: "V"
---

Status Information in Response Data


The Response data of a command frequently include a Status that indicates correct execution or
command failures.  Currently the following Status codes are returned:
- 0x00 = DAP_OK: Command has been successfully executed
- 0xFF = DAP_ERROR: Command did not execute due to communication failure with the device.
