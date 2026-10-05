---
id: "dap-dap-uart-control"
type: "concept"
domain: "debug"
title: "DAP_UART_Control"
summary: "DAP_UART_Control (0x22): -------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_UART_Control.html"
license: "Apache-2.0"
mode: "V"
---

Control UART data receive and transmit.

DAP_UART_Control (0x22):
-------------------------

Enables and disables UART receive and transmit (only for transport via DAP).

**DAP_UART_Control Request:**
```
 | BYTE | BYTE    |
 > 0x22 | Control |
 |******|*********|
```

- **Control**:
  - Bit 0: 1 = Receive Enable, 0 = no operation
  - Bit 1: 1 = Receive Disable, 0 = no operation
  - Bit 2: 1 = Receive Buffer Flush, 0 = no operation
  - Bit 3: reserved (0)
  - Bit 4: 1 = Transmit Enable, 0 = no operation
  - Bit 5: 1 = Transmit Disable, 0 = no operation
  - Bit 6: 1 = Transmit Buffer Flush, 0 = no operation
  - Bit 7: reserved (0)

**Note:** DAP_UART_Control command can be used only if transport via DAP is enabled.\n
      Receive/Transmit enable bit can be set only if DAP UART is already configured (DAP_UART_Configure).\n

**Note:** When enable and disable bits are set at the same time, only disable is executed.\n
      Receive/Transmit enable also automatically flushes any existing data in Receive/Transmit buffer.

**DAP_UART_Control Response:**
```
 | BYTE | BYTE   |
 > 0x22 | Status |
 |******|********|
```

- **Status**: DAP_Response_Status
