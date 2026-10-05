---
id: "dv-usart-server-configuration"
type: "concept"
domain: "drivers"
title: "USART Server: Configuration"
summary: "Communication settings are defined in USART_Server_Config.h file. \"USART_Server_Config.h configuration file in Configuration Wizard view mode\""
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_server.html"
license: "Apache-2.0"
mode: "V"
---

Communication settings are defined in **USART_Server_Config.h** file.
 "USART_Server_Config.h configuration file in Configuration Wizard view mode"


### Configuration settings


- **Driver_USART#** - selects the USART driver instance used by the Server.
- **Communication settings**:
  - **Mode** - defines the mode used for command exchange (must match DUT setup).
  - Fixed parameters used for command exchange:
    - **Baudrate:** 115200
    - **Data Bits:** 8
    - **Parity:** None
    - **Stop Bits:** 1
    - **Flow Control:** None
