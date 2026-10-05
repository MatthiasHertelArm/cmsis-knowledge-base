---
id: "dv-configuration-configuration-settings-6"
type: "concept"
domain: "drivers"
title: "Configuration: Configuration settings"
summary: "Configuration: Configuration settings"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_config.html"
license: "Apache-2.0"
mode: "V"
---

**Driver_SPI#** selects the driver instance to be tested.  
Example: to test `Driver_SPI2`, set this value to `2`.

**Configuration** contains settings for **Test Mode**, **SPI Server**, and **Tests**:

- **Test Mode**: **Loopback** or **SPI Server**.  
  - *Loopback* is recommended for initial validation of **Master** functionality. It requires MOSI and MISO to be
    connected together to verify basic operation.  
  - For *full* CMSIS-Driver SPI compliance, use **SPI Server** mode.

- **SPI Server** (applies only when *Test Mode: SPI Server* is selected):  
  Defines communication settings between Driver Validation and the SPI Server and **must match** the Server.  
  - Fixed parameters:  
    - **Clock/Frame:** CPOL=0, CPHA=0  
    - **Data Bits:** 8  
    - **Bit Order:** MSB to LSB
  - Configurable parameters:  
    - **Slave Select** - **Software Controlled** (driver toggles SS using `ARM_SPI_CONTROL_SS`) or **Hardware Controlled**.  
    - **Bus Speed** - nominal bus speed for reliable command exchange with the Server.

- **Tests**: configuration for test execution.  
  - **Default settings** - defaults for data exchange tests (see spi_tests_data_xchg).  
  - **Bus Speed** - minimum/maximum speeds used by SPI_Bus_Speed_Min and SPI_Bus_Speed_Max.  
  - **Number of Items** - item counts (including odd/unusual) used by SPI_Number_Of_Items to verify conformance.

**Tests** section - enable/disable test groups (and individual tests):  
- **Driver Management** - see spi_tests_drv_mgmt.  
- **Data Exchange** - see spi_tests_data_xchg.  
- **Event** - see spi_tests_evt.
