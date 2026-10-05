---
id: "dap-dap-connect"
type: "concept"
domain: "debug"
title: "DAP_Connect"
summary: "Connect to Device and selected DAP mode."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Connect.html"
license: "Apache-2.0"
mode: "V"
---

Connect to Device and selected DAP mode.

The **DAP_Connect Command** initializes the DAP I/O pins for the specified DAP mode (JTAG or
SWD). This command calls the function PORT_SWD_SETUP or PORT_JTAG_SETUP which prepares the
connection to the Target Device.

**DAP_Connect Command:**
```
| BYTE | BYTE |
> 0x02 | Port |
|******|******|
```

- **Port:** Selects the DAP port mode and configures the DAP I/O pins. The possible values are:
  - 0 = Default mode: configuration of the DAP port mode is derived from DAP_DEFAULT_PORT (zero configuration).
  - 1 = SWD mode: connect with Serial Wire Debug mode.
  - 2 = JTAG mode: connect with 4/5-pin JTAG mode.


**DAP_Connect Response:**
```
| BYTE | BYTE |
< 0x02 | Port |
|******|******|
```

- **Port:** DAP port mode initialized. The possible values are:
  - 0 = initialization failed; no mode pre-configured.
  - 1 = initialization for SWD mode.
  - 2 = initialization for JTAG mode.
