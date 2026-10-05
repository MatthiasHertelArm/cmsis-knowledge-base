---
id: "dv-usart-server-running-on-specific-hardware"
type: "concept"
domain: "drivers"
title: "USART Server: Running on specific hardware"
summary: "Using the Arm CMSIS Solution VS Code extension, create a new solution from template:"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_server.html"
license: "Apache-2.0"
mode: "V"
---

Using the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) VS Code extension,
create a new solution from **template**:

1. In the **CMSIS** extension, click **Create a New Solution**.
   
2. Select the **Target Board**.
3. Under **Templates, Reference Applications, and Examples**,
   select **USART Server (CMSIS-Driver Validation USART Server application)**.
   
4. Choose **Solution Base Folder**, click **Create**.
   
5. Select the board layer that provides an USART Driver, click **OK**.
6. If the board's USART is not routed to ARDUINO (or a different peripheral is required)
   , open **USART_Server_Config.h**, **Open Preview** and edit **Driver_USART#** to 
   the required instance.
7. Build and run the **USART Server application** on your hardware.

**Note:** **IMPORTANT:** The target board's USART CMSIS-Driver must be **fully CMSIS compliant**!
**Note:** The USART Server for **build-type: Debug** displays command execution on an STDOUT channel (typically Virtual COM Port via Debug adapter).
