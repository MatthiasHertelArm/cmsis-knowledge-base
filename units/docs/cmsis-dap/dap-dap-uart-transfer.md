---
id: "dap-dap-uart-transfer"
type: "concept"
domain: "debug"
title: "DAP_UART_Transfer"
summary: "DAP_UART_Transfer (0x21): -------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_UART_Transfer.html"
license: "Apache-2.0"
mode: "V"
---

Transfer data via UART.

DAP_UART_Transfer (0x21):
-------------------------

Receive and Transmit data via target UART (only for transport via DAP).

**DAP_UART_Transfer Request:**

```
 | BYTE | SHORT    | SHORT   | BYTE          |
 > 0x21 | Rx Count | Tx Count| Transmit data |
 |******|**********|*********|+++++++++++++++|
```

- **Rx Count**: Maximum number of bytes to be read from UART receive buffer.

- **Tx Count**: Number of bytes in **Transmit data** to be transmitted.

**Note:** DAP_UART_Transfer command can be used only if transport via DAP is enabled.\n

**Note:** If only receive is required, Tx Count can be 0.\n
      If only transmit is required, Rx Count can be 0.

**DAP_UART_Transfer Response:**

```
 | BYTE | BYTE   | SHORT    | SHORT    | BYTE          |
 < 0x21 | Status | Tx Count | Rx Count | Receive data  |
 |******|********|**********|**********|+++++++++++++++|
```

- **Status**:
  - Bit 0: 1 = Receive enabled, 0 = Receive disabled
  - Bit 1: 1 = Data lost detected during receive (automatically cleared)
  - Bit 2: 1 = Framing error detected (automatically cleared)
  - Bit 3: 1 = Parity error detected (automatically cleared)
  - Bit 4: 1 = Transmit enabled, 0 = Transmit disabled
  - Bit 7..5: reserved (0)

- **Tx Count**: Number of bytes accepted from **Transmit data** and queued to UART transmit buffer.

- **Rx Count**: Number of bytes in **Receive data** read from UART receive buffer.

- **Receive data**: Bytes received from the target device via UART.
