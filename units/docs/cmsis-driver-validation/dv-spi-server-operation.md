---
id: "dv-spi-server-operation"
type: "concept"
domain: "drivers"
title: "SPI Server: Operation"
summary: "The Server waits for a command from the SPI Client (Driver Validation), executes it, and then waits for the next one. Most commands have no additional data phase, though some do."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_server.html"
license: "Apache-2.0"
mode: "V"
---

The Server waits for a command from the SPI Client (Driver Validation), executes it, and then waits for the next one.
Most commands have no additional data phase, though some do. The Server operates as an SPI **Slave** except when a **Master**
transfer is explicitly requested; after completing it, the Server returns to **Slave** mode.
