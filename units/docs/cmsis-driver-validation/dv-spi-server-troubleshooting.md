---
id: "dv-spi-server-troubleshooting"
type: "concept"
domain: "drivers"
title: "SPI Server: Troubleshooting"
summary: "2. Debug message \"Server Start failed!\" (build-type: Debug) - Check heap (must be > 2  SPI_SERVER_BUF_SIZE). - Verify RTOS allows >= 512 bytes allocation for the Server main thread (e.g., Global Dynamic Memory size in RTX_Config.h if RTX5)."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_server.html"
license: "Apache-2.0"
mode: "V"
---

1. **Server not responding**
   - Reset the Server.
   - Verify the correct driver instance in `SPI_Server_Config.h`.
   - Reduce bus speed used for communication with the Server (in `DV_SPI_Config.h`).

2. Debug message **"Server Start failed!"** (build-type: Debug)
   - Check heap (must be > `2 * SPI_SERVER_BUF_SIZE`).
   - Verify RTOS allows >= **512 bytes** allocation for the Server main thread (e.g., *Global Dynamic Memory size* in `RTX_Config.h` if RTX5).
   - Ensure the Server's SPI driver supports all fixed settings (Slave with hardware-monitored Slave Select, CPOL=0/CPHA=0, 8 bits, MSB to LSB).

3. **Tests report data mismatch**
   - Ensure Slave Select line has a pull-up to Vcc (3.3 V).
   - Keep **wires short and separate**; pair SCK and GND if possible.
   - Ensure the SPI driver does not drive Slave Select line while inactive.
