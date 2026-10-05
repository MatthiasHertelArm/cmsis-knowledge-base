---
id: "dv-configuration-configuration-settings-7"
type: "concept"
domain: "drivers"
title: "Configuration: Configuration settings"
summary: "Configuration: Configuration settings"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_config.html"
license: "Apache-2.0"
mode: "V"
---

**Driver_USART#** selects the driver instance to be tested.  
Example: to test `Driver_USART2`, set this value to `2`.

**Configuration** contains settings for **Test Mode**, **USART Server**, and **Tests**:

- **Test Mode**: **Loopback** or **USART Server**.  
  - *Loopback* is recommended for initial validation. It requires Tx and Rx pins to be connected together so that
    basic functionality can be verified.  
  - For *full* compliance with the CMSIS-Driver USART specification, use **USART Server** mode.

- **USART Server** (applies only when *Test Mode: USART Server* is selected):  
  Communication parameters at which Driver Validation communicates with the USART Server. These **must match** the
  settings on the USART Server.  
  - Fixed (non-configurable) parameters:  
    - **Baudrate:** 115200  
    - **Data Bits:** 8  
    - **Parity:** None  
    - **Stop Bits:** 1  
    - **Flow Control:** None
  - Configurable parameter:  
    - **Mode** - communication mode with the USART Server. Different modes require different physical connections and the
      USART Server must be configured accordingly. For details, see USART Server connection.

- **Tests**: configuration for test execution.  
  - **Default settings** - default parameters for data exchange tests. Typically, a single feature is varied while all
    other parameters use defaults. For defaults used by each function, see usart_tests_data_xchg.  
  - **Baudrate** - minimum and maximum bus speeds used by USART_Baudrate_Min and USART_Baudrate_Max.  
  - **Number of Items** - a selection of item counts (including unusual/odd counts) used by USART_Number_Of_Items
    to verify transfers comply with the CMSIS-Driver specification.

**Tests** section - enable/disable test groups (and individual tests):  
- **Driver Management** - see usart_tests_drv_mgmt.  
- **Data Exchange** - see usart_tests_data_xchg.  
- **Modem** - see usart_tests_modem.  
- **Event** - see usart_tests_evt.
