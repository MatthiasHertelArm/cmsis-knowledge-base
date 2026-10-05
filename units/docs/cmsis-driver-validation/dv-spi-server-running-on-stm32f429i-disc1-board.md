---
id: "dv-spi-server-running-on-stm32f429i-disc1-board"
type: "concept"
domain: "drivers"
title: "SPI Server: Running on STM32F429I-DISC1 board"
summary: "Using the Arm CMSIS Solution VS Code extension, create a new solution from example:"
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_SPI.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/spi_server.html"
license: "Apache-2.0"
mode: "V"
---

Using the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) VS Code extension,
create a new solution from **example**:

1. In the **CMSIS** extension, click **Create a New Solution**.
   
2. Select an **STM32F429I-DISC1 board** as a **Target Board**.
3. Under **Templates, Reference Applications, and Examples**,
   select **SPI Server (CMSIS-Driver Validation SPI Server application for STM32F429I-DISC1 board)**.
   
4. Choose **Solution Base Folder** and click **Create**.
   
5. Build and run the **SPI Server application** on the **STM32F429I-DISC1 board**.

**SPI1 pinout (STM32F429I-DISC1):**
| SPI function                     | Pin  |
| :------------------------------- | :--: |
| SPI Clock                        | PA5  |
| Master Output Slave Input (MOSI) | PA7  |
| Master Input Slave Output (MISO) | PB4  |
| Slave Select                     | PA15 |

**Note:** **IMPORTANT:** Connect **ground between** the **SPI Server** and the **Device (Driver) Under Test** to ensure a common
reference potential.
**Note:** The STM32F429I-DISC1 SPI Server does **not** support National Semiconductor **Microwire** frame format.
**Note:** The STM32F429I-DISC1 SPI Server for **build-type: Debug** displays command execution on an on-board LCD.
