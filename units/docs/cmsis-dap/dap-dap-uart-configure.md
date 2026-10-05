---
id: "dap-dap-uart-configure"
type: "concept"
domain: "debug"
title: "DAP_UART_Configure"
summary: "DAP_UART_Configure (0x20): -------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_UART_Configure.html"
license: "Apache-2.0"
mode: "V"
---

Set UART configuration.

DAP_UART_Configure (0x20):
-------------------------

Sets the UART configuration (only for transport via DAP).

**DAP_UART_Configure Request:**
```
 | BYTE | BYTE    | WORD     |
 > 0x20 | Control | Baudrate |
 |******|*********|**********|
```

- **Control**: Parameter values are compatible with CMSIS-Driver USART Interface in asynchronous mode and
  without flow control:
  - Bit 3..0: Data bits: 5 = 5 Data bits, 6 = 6 Data bits, 7 = 7 Data bits, 0 = 8 Data bits
  - Bit 5..4: Parity: 0 = None, 1 = Even, 2 = Odd
  - Bit 7..6: Stop bits: 0 = 1 Stop bit, 1 = 2 Stop bits

- **Baudrate**: Requested baudrate

**Note:** DAP_UART_Configure command can be used only if transport via DAP is enabled.\n

**Note:** It is required to configure the UART each time transport via DAP is enabled (DAP_UART_Transport command).\n
      It is recommended to configure the UART before receive and transmit are enabled (DAP_UART_Control command).

**DAP_UART_Configure Response:**
```
 | BYTE | BYTE   | WORD     |
 > 0x20 | Status | Baudrate |
 |******|********|**********|
```

- **Status**: 0x00 = OK else ERROR:
  - Bit 0: 1 = Data bits configuration error.
  - Bit 1: 1 = Parity configuration error.
  - Bit 2: 1 = Stop bits configuration error.
  - Bit 7..3: reserved (0)

- **Baudrate**: Actual baudrate or 0 (baudrate configuration error).
    When requested baudrate is not achievable the closest configured baudrate can be returned or 0
    which indicates baudrate configuration error.
