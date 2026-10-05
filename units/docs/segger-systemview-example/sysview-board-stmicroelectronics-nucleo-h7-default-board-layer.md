---
id: "sysview-board-stmicroelectronics-nucleo-h7-default-board-layer"
type: "concept"
domain: "trace"
title: "Board: STMicroelectronics NUCLEO-H743ZI2: Default Board Layer"
summary: "This setup is configured using STM32CubeMX, an interactive tool provided by STMicroelectronics for device configuration. Refer to \"Configure STM32 Devices with CubeMX\" for additional information."
status: "draft"
collection: "segger-systemview-example"
source: "Arm-Examples/SEGGER-SystemView@9be0601:Board/NUCLEO-H743ZI2/README.md"
doc_source: "https://github.com/Arm-Examples/SEGGER-SystemView/blob/9be0601/Board/NUCLEO-H743ZI2/README.md#default-board-layer"
license: "Apache-2.0"
mode: "V"
---

Device: **STM32H743ZITx**

System Core Clock: **480 MHz**

This setup is configured using **STM32CubeMX**, an interactive tool provided by STMicroelectronics for device configuration.
Refer to ["Configure STM32 Devices with CubeMX"](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/) for additional information.

### System Configuration

| System resource       | Setting
|:----------------------|:--------------------------------------
| Heap                  | 64 kB (configured in the STM32CubeMX)
| Stack (MSP)           |  1 kB (configured in the STM32CubeMX)

### STDIO mapping

**STDIO** is routed to Virtual COM port on the ST-LINK (using **USART3** peripheral)

### CMSIS-Driver mapping

| CMSIS-Driver          | Peripheral            | Board connector/component                     | Connection
|:----------------------|:----------------------|:----------------------------------------------|:------------------------------
| Driver_ETH_MAC0       | ETH                   | Ethernet RJ45 connector (CN14)                | CMSIS_ETH
| Driver_ETH_PHY0       | LAN8742A (external)   | Ethernet RJ45 connector (CN14)                | CMSIS_ETH
| Driver_GPIO0          | GPIO                  | Arduino digital I/O pins D2..D10, D14..D19    | ARDUINO_UNO_D2..D10, D14..D19
| Driver_I2C1           | I2C1                  | Arduino I2C pins D20..D21                     | ARDUINO_UNO_I2C
| Driver_SPI1           | SPI1                  | Arduino SPI pins D10..D13                     | ARDUINO_UNO_SPI
| Driver_USART1         | USART1                | Arduino UART pins D0..D1                      | ARDUINO_UNO_UART
| Driver_USART2         | USART2                | ZIO pins D52, D53 (CN9)                       | CMSIS_USART
| Driver_USART3         | USART3                | ST-LINK connector (CN1)                       | STDIN, STDOUT, STDERR
| Driver_USBD0          | USB_OTG_FS            | User USB connector (CN13)                     | CMSIS_USB_Device
| CMSIS-Driver VIO      | GPIO                  | LEDs (LD3, LD1, LD2) and USER button (B1)     | CMSIS_VIO

Reference to [Arduino UNO connector description](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/#arduino-shield).

### CMSIS-Driver Virtual I/O mapping

| CMSIS-Driver VIO      | Board component
|:----------------------|:--------------------------------------
| vioBUTTON0            | USER button (B1)
| vioLED0               | LED red     (LD3)
| vioLED1               | LED green   (LD1)
| vioLED2               | LED yellow  (LD2)
