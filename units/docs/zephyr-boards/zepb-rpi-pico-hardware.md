---
id: "zepb-rpi-pico-hardware"
type: "concept"
domain: "bring-up"
title: "rpi_pico: Hardware"
summary: "The peripherals of the RP2040 SoC can be routed to various pins on the board. The configuration of these routes can be modified through DTS. Please refer to the datasheet to see the possible routings for each peripheral."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/raspberrypi/rpi_pico/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- Dual core Arm Cortex-M0+ processor running up to 133MHz
- 264KB on-chip SRAM
- 2MB on-board QSPI flash with XIP capabilities
- 26 GPIO pins
- 3 Analog inputs
- 2 UART peripherals
- 2 SPI controllers
- 2 I2C controllers
- 16 PWM channels
- USB 1.1 controller (host/device)
- 8 Programmable I/O (PIO) for custom peripherals
- On-board LED
- 1 Watchdog timer peripheral
- Infineon CYW43439 2.4 GHz Wi-Fi chip (Pico W only)



### Supported Features



### Pin Mapping


The peripherals of the RP2040 SoC can be routed to various pins on the board.
The configuration of these routes can be modified through DTS. Please refer to
the datasheet to see the possible routings for each peripheral.

External pin mapping on the Pico W is identical to the Pico, but note that internal
RP2040 GPIO lines 23, 24, 25, and 29 are routed to the Infineon module on the W.
Since GPIO 25 is routed to the on-board LED on the Pico, but to the Infineon module
on the Pico W, the "blinky" sample program does not work on the W (use hello_world for
a simple test program instead).


#### Default Zephyr Peripheral Mapping:


- UART0_TX : P0
- UART0_RX : P1
- I2C0_SDA : P4
- I2C0_SCL : P5
- I2C1_SDA : P6
- I2C1_SCL : P7
- SPI0_RX : P16
- SPI0_CSN : P17
- SPI0_SCK : P18
- SPI0_TX : P19
- ADC_CH0 : P26
- ADC_CH1 : P27
- ADC_CH2 : P28
- ADC_CH3 : P29
