---
id: "dap-dap-jtag-configure"
type: "concept"
domain: "debug"
title: "DAP_JTAG_Configure"
summary: "The DAP_JTAG_Configure Command sets the JTAG device chain information for communication with \\ref DAP_transfer_gr. The JTAG device chain needs to be iterated with DAP_JTAG_Sequence or manually configured by the debugger on the host computer."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_JTAG_Configure.html"
license: "Apache-2.0"
mode: "V"
---

Configure JTAG Chain

The **DAP_JTAG_Configure Command** sets the JTAG device chain information for communication with \ref
DAP_transfer_gr. The JTAG device chain needs to be iterated with DAP_JTAG_Sequence or manually
configured by the debugger on the host computer.

**DAP_JTAG_Configure Command**:
```
| BYTE | BYTE *| BYTE *****|
> 0x15 | Count | IR Length |
|******|*******|+++++++++++|
```

- **Count:** Number of devices in chain
- **IR Length**: JTAG IR register length (in bits) for each device.

**DAP_JTAG_Configure Response**:
```
| BYTE | BYTE **|
< 0x15 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
