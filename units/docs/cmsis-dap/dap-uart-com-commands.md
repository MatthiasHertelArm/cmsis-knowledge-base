---
id: "dap-uart-com-commands"
type: "concept"
domain: "debug"
title: "UART COM Commands"
summary: "CMSIS-DAP debug unit can be extended to support a separate UART port that connects to the target. Such a UART communication is typically used for printf-style debugging, but the usage is not limited to that."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_uart_gr.html"
license: "Apache-2.0"
mode: "V"
---

Target communication via extra UART.

CMSIS-DAP debug unit can be extended to support a separate UART port that connects to the target. Such a UART communication
is typically used for printf-style debugging, but the usage is not limited to that.  CMSIS-DAP supports UART communication via:
  - dedicated CMSIS-DAP commands: connects seamlessly to (Cloud) IDEs that integrate a printf viewer.
  - via standard USB COM port (optional): for any data communication, i.e. to transmit training data sets for machine learning.

The following CMSIS-DAP commands are added to support UART communication:
 - DAP_UART_Transport :  DAP_UART_Transport
 - DAP_UART_Configure :  DAP_UART_Configure
 - DAP_UART_Control :  DAP_UART_Control
 - DAP_UART_Status :  DAP_UART_Status
 - DAP_UART_Transfer :  DAP_UART_Transfer
