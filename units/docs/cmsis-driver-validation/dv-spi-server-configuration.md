---
id: "dv-spi-server-configuration"
type: "concept"
domain: "drivers"
title: "SPI Server: Configuration"
summary: "Communication settings are defined in SPI_Server_Config.h file. \"SPI_Server_Config.h configuration file in Configuration Wizard view mode\""
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_server.html"
license: "Apache-2.0"
mode: "V"
---

Communication settings are defined in **SPI_Server_Config.h** file.
 "SPI_Server_Config.h configuration file in Configuration Wizard view mode"


### Configuration settings


- **Driver_SPI#** - selects the driver instance used by the Server.
- **Communication settings** (fixed for command exchange):
  - **Mode:** Slave with **hardware-monitored Slave Select**
  - **Clock/Frame:** Clock Polarity 0/ Clock Phase 0
  - **Data Bits:** 8
  - **Bit Order:** MSB to LSB

**Note:** The SPI Server receives commands as an SPI **Slave** using the **Slave Select** line. The Server's SPI driver **must
support hardware-monitored Slave Select** functionality.
