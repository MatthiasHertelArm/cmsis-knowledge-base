---
id: "ocp-readme-3"
type: "concept"
domain: "project"
title: "README"
summary: "Board: STMicroelectronics B-U585I-IOT02A ------------------------------------------"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/Board/B-U585I-IOT02A/IoT/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Board/B-U585I-IOT02A/IoT/README.md"
license: "Apache-2.0"
mode: "V"
---

Board: STMicroelectronics [B-U585I-IOT02A](https://www.st.com/en/evaluation-tools/b-u585i-iot02a.html)
------------------------------------------

Device: **STM32U585AII6QU**  
System Core Clock: **160 MHz**

This setup is configured using **STM32CubeMX**, an interactive tool provided by STMicroelectronics for device configuration.
Refer to ["Create Projects with STM32Cube HAL and STM32CubeMX"](https://www.keil.com/pack/doc/STM32Cube/html/index.html) for additional information.

For **STM32CubeMX** configuration settings please refer to [STM32CubeMX Configuration](https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Board/B-U585I-IOT02A/IoT/STM32CubeMX/STM32CubeMX.pdf).

The Heap/stack settings and CMSIS-Driver assignments are configured in the configuration files of respective software components.

The example project can be re-configured to work on custom hardware.
Refer to ["Migrate STM32 Based Example Projects to Custom Hardware"](https://github.com/MDK-Packs/Documentation/tree/master/Porting_to_Custom_Hardware) for additional information.

### System Configuration

**TrustZone** disabled (option bit TZEN=0)

| System resource         | Setting
|:------------------------|:--------------------------------------------
| Heap                    | 64 kB (configured in the linker script file)
| Stack (MSP)             | 1 kB (configured in the linker script file)

### STDIO mapping

**STDIO** is routed to Virtual COM port on the ST-Link (using USART1 peripheral)

### CMSIS-Driver mapping

| CMSIS-Driver  | Peripheral  | Physical connection
|:--------------|:------------|:------------------------------------
| Driver_SPI1   | SPI1        | Arduino UNO R3 connector (CN13)
| Driver_USART3 | USART3      | Arduino UNO R3 connector (CN13)
| Driver_USART4 | UART4       | Bluetooth Low Energy Wireless module
| Driver_WiFi0  | SPI2        | WiFi MXCHIP EMW3080 module
| Driver_GPIO0  | GPIO0       | Digital I/O pins

### CMSIS-Driver Virtual I/O mapping

| CMSIS-Driver VIO  | Physical resource
|:------------------|:-------------------------------
| vioBUTTON0        | Button USER (PC13)
| vioLED0           | LED RED (PH6)
| vioLED1           | LED GREEN (PH7)

### Arduino UNO mapping

| Arduino resource  | Driver
|:------------------|:-------------------------------
| UART (D0,D1)      | USART3 Driver (ARDUINO_UNO_UART)
| SPI (D11,D12,D13) | SPI1 Driver (ARDUINO_UNO_SPI)
| I2C (D20,D21)     | I2C1 Driver (ARDUINO_UNO_I2C)
| Digital I/O: D2   | GPIO0 Driver (ARDUINO_UNO_D2)
| Digital I/O: D3   | GPIO0 Driver (ARDUINO_UNO_D3)
| Digital I/O: D4   | GPIO0 Driver (ARDUINO_UNO_D4)
| Digital I/O: D5   | GPIO0 Driver (ARDUINO_UNO_D5)
| Digital I/O: D6   | GPIO0 Driver (ARDUINO_UNO_D6)
| Digital I/O: D7   | GPIO0 Driver (ARDUINO_UNO_D7)
| Digital I/O: D8   | GPIO0 Driver (ARDUINO_UNO_D8)
| Digital I/O: D9   | GPIO0 Driver (ARDUINO_UNO_D9)
| Digital I/O: D10  | GPIO0 Driver (ARDUINO_UNO_D10)
| Digital I/O: D14  | GPIO0 Driver (ARDUINO_UNO_D14)
| Digital I/O: D15  | GPIO0 Driver (ARDUINO_UNO_D15)
| Digital I/O: D16  | GPIO0 Driver (ARDUINO_UNO_D16)
| Digital I/O: D17  | GPIO0 Driver (ARDUINO_UNO_D17)
| Digital I/O: D18  | GPIO0 Driver (ARDUINO_UNO_D18)
| Digital I/O: D19  | GPIO0 Driver (ARDUINO_UNO_D19)
