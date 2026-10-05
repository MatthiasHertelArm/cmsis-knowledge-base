---
id: "dap-dap-uart-status"
type: "concept"
domain: "debug"
title: "DAP_UART_Status"
summary: "DAP_UART_Status (0x23): -------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_UART_Status.html"
license: "Apache-2.0"
mode: "V"
---

Get UART status.

DAP_UART_Status (0x23):
-------------------------

Reads UART status (only for transport via DAP).

**DAP_UART_Status Request:**
```
 | BYTE |
 > 0x23 |
 |******|
```

**Note:** DAP_UART_Status command can be used only if transport via DAP is enabled.\n


**DAP_UART_Status Response:**
```
 | BYTE | BYTE   | WORD     | WORD     |
 > 0x23 | Status | Rx Count | Tx Count |
 |******|********|**********|**********|
```

- **Status**:
  - Bit 0: 1 = Receive enabled, 0 = Receive disabled
  - Bit 1: 1 = Data lost detected during receive (automatically cleared)
  - Bit 2: 1 = Framing error detected (automatically cleared)
  - Bit 3: 1 = Parity error detected (automatically cleared)
  - Bit 4: 1 = Transmit enabled, 0 = Transmit disabled
  - Bit 7..5: reserved (0)

- **Rx Count**: Number of bytes in UART receive buffer (not yet read)

- **Tx Count**: Number of bytes in UART transmit buffer (not yet transmitted)
