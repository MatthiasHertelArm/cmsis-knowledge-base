---
id: "dv-spi-server"
type: "concept"
domain: "drivers"
title: "SPI Server"
summary: "The SPI Server application provides features used by the CMSIS-Driver Validation suite to test physical operation of the SPI driver."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_server.html"
license: "Apache-2.0"
mode: "V"
---

The **SPI Server** application provides features used by the CMSIS-Driver Validation suite to test physical operation of
the SPI driver.

It is available for the STMicroelectronics **STM32F429I-DISC1** board and as a template for **any board**
with available **Board Layer** and configured **CMSIS compliant SPI driver**.

**Note:** STM32F429I-DISC1 was selected because its SPI driver is stable and supports all required features.
**Note:** For running on STM32F429I-DISC1 board, see spi_server_disc1.
**Note:** For running on other hardware, see spi_server_template.
