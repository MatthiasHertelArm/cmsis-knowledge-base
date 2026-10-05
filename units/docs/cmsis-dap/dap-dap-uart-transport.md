---
id: "dap-dap-uart-transport"
type: "concept"
domain: "debug"
title: "DAP_UART_Transport"
summary: "DAP_UART_Transport (0x1F): -------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_UART_Transport.html"
license: "Apache-2.0"
mode: "V"
---

Set UART transport mode.

DAP_UART_Transport (0x1F):
-------------------------

Sets the UART transport mode for receiving and transmitting data.

**DAP_UART_Transport Request:**
```
 | BYTE | BYTE      |
 > 0x1F | Transport |
 |******|***********|
```

- **Transport**:
  - 0 - None (default, if transport via USB COM Port is not implemented).
  - 1 - Transport data via USB COM Port (default, if implemented).
  - 2 - Transport data via DAP commands.

**Note:** By default, data is transported via the USB COM Port (if implemented). In this case,
      the UART is controlled via a terminal (for example Putty), which can configure the
      UART (data bits, party, baudrate ...) and transfer the data.

**Note:** When transport data via DAP is enabled, CMSIS-DAP takes control over the UART with commands:
      DAP_UART_Configure, DAP_UART_Control, DAP_UART_Status and DAP_UART_Transfer.

**DAP_UART_Transport Response:**
```
 | BYTE | BYTE   |
 < 0x1F | Status |
 |******|********|
```

- **Status**: DAP_Response_Status
