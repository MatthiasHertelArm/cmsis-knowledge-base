---
id: "dap-dap-hoststatus"
type: "concept"
domain: "debug"
title: "DAP_HostStatus"
summary: "Sent status information of the debugger to Debug Unit."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_HostStatus.html"
license: "Apache-2.0"
mode: "V"
---

Sent status information of the debugger to Debug Unit.

The **DAP_HostStatus Command** is used to sent the status information about the debugger to the Debug Unit.
This status information may be displayed on the Debug Unit. Therefore a Debug Unit may provide optional Status LEDs:
 - Connect LED: is active when the DAP hardware is connected to a debugger.
 - Running LED: is active when the debugger has put the target device into running state.

**DAP_HostStatus Command:**
```
| BYTE | BYTE **| BYTE **|
> 0x01 | Type   | Status |
|******|********|********|
```
- **Type:** specifies the type of the information that is sent in **Status:**
  - **0** = Connect: Status indicates that the debugger is connected to the Debug Unit.
  - **1** = Running: Status indicates that the target hardware is executing application code.
- **Status:** contains the actual status information:
  - **0** = False: may be used to turn off a status LED (Connect or Running) on the Debug Unit.
  - **1** = True: may be used to turn on a status LED (Connect or Running) on the Debug Unit.

**DAP_HostStatus Response:**
```
| BYTE | BYTE **|
< 0x01 | 0x00   |
|******|********|
```
