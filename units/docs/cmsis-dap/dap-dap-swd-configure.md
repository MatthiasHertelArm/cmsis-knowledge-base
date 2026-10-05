---
id: "dap-dap-swd-configure"
type: "concept"
domain: "debug"
title: "DAP_SWD_Configure"
summary: "The DAP_SWD_Configure Command sets the SWD protocol configuration. For more information about the SWD protocol refer to the Arm Debug Interface v5 - Interface Specification."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWD_Configure.html"
license: "Apache-2.0"
mode: "V"
---

Configure SWD Protocol

The **DAP_SWD_Configure Command** sets the SWD protocol configuration. For more information about
the SWD protocol refer to the **Arm Debug Interface v5 - Interface Specification.**

**DAP_SWD_Configure Command**:
```
| BYTE | BYTE *********|
> 0x13 | Configuration |
|******|***************|
```

- **Configuration:** Contains information about SWD specific features \n
  - Bit 1 .. 0: Turnaround clock period of the SWD device (should be identical with the WCR [Write Control Register] value of the target):
    0 = 1 clock cycle (default), 1 = 2 clock cycles, 2 = 3  clock cycles, 3 = 4 clock cycles.

  - Bit 2: DataPhase: 0 = Do not generate Data Phase on WAIT/FAULT (default), 1 = Always generate Data Phase (also on WAIT/FAULT; Required for Sticky Overrun behavior).

**DAP_SWD_Configure Response**:
```
| BYTE | BYTE **|
< 0x13 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
