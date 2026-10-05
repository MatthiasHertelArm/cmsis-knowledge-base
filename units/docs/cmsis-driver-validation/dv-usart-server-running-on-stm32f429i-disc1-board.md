---
id: "dv-usart-server-running-on-stm32f429i-disc1-board"
type: "concept"
domain: "drivers"
title: "USART Server: Running on STM32F429I-DISC1 board"
summary: "Using the Arm CMSIS Solution VS Code extension, create a new solution from example:"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USART.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usart_server.html"
license: "Apache-2.0"
mode: "V"
---

Using the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) VS Code extension,
create a new solution from **example**:

1. In the **CMSIS** extension, click **Create a New Solution**.
   
2. Select an **STM32F429I-DISC1 board** as a **Target Board**.
3. Under **Templates, Reference Applications, and Examples**,
   select **USART Server (CMSIS-Driver Validation USART Server application for STM32F429I-DISC1 board)**.
   
4. Choose **Solution Base Folder** and click **Create**.
   
5. Build and run the **USART Server application** on the **STM32F429I-DISC1 board**.

**USART1 pinout (STM32F429I-DISC1):**

| USART function | Pin  |
| :------------- | :--: |
| Tx             | PA9  |
| Rx             | PA10 |
| CLK (sync)     | PA8  |
| CTS            | PA11 |
| RTS            | PA12 |
| DCD test pin   | PA13 |
| RI test pin    | PA14 |

**Note:** **IMPORTANT:** Connect **ground between** the **USART Server** and the **Device (Driver) Under Test** to ensure a common
reference potential.
**Note:** For synchronous testing, this hardware supports only **synchronous Master** mode, therefore it can only be used to
test **synchronous Slave** mode of the Driver Under Test.
**Note:** The STM32F429I-DISC1 USART Server for **build-type: Debug** displays command execution on an on-board LCD.
