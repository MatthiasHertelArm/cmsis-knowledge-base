---
id: "dv-usart-server-troubleshooting"
type: "concept"
domain: "drivers"
title: "USART Server: Troubleshooting"
summary: "2. Debug message \"Server Start failed!\" (build-type: Debug) - Check heap (must be > 2  USART_SERVER_BUF_SIZE). - Verify RTOS allows >= 512 bytes allocation for the Server main thread (e.g., Global Dynamic Memory size in RTX_Config.h if RTX5)."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_server.html"
license: "Apache-2.0"
mode: "V"
---

1. **Server not responding**
   - Reset the Server.
   - Verify the correct driver instance in `USART_Server_Config.h`.
   - Ensure communication settings (mode) match between Server and Driver Validation; if changed, rebuild and reflash.

2. Debug message **"Server Start failed!"** (build-type: Debug)
   - Check heap (must be > `2 * USART_SERVER_BUF_SIZE`).
   - Verify RTOS allows >= **512 bytes** allocation for the Server main thread (e.g., *Global Dynamic Memory size* in `RTX_Config.h` if RTX5).
   - Ensure the Server's USART driver supports all fixed settings:
     - Baudrate 115200, 8-N-1, Flow Control None.
