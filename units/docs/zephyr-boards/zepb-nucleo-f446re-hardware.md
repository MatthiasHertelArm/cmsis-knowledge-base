---
id: "zepb-nucleo-f446re-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_f446re: Hardware"
summary: "Nucleo F446RE provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_f446re/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f446re/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

Nucleo F446RE provides the following hardware components:

- STM32F446RET6 in LQFP64 package
- ARM® 32-bit Cortex®-M4 CPU with FPU
- Adaptive real-time accelerator (ART Accelerator)
- 180 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 512 KB Flash
- 128 KB SRAM
- 10 General purpose timers
- 2 Advanced control timers
- 2 basic timers
- SPI(4)
- I2C(3)
- USART(4)
- UART(2)
- USB OTG Full Speed and High Speed
- CAN(2)
- SAI(2)
- SPDIF_Rx(1)
- HDMI_CEC(1)
- Quad SPI(1)
- Camera Interface
- GPIO(50) with external interrupt capability
- 12-bit ADC(3) with 16 channels
- 12-bit DAC with 2 channels

More information about STM32F446RE can be found here:

- STM32F446RE on www.st.com
- STM32F446 reference manual


### Supported Features



### Connections and IOs


Nucleo F446RE Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.


#### Available pins:

For more details please refer to STM32 Nucleo-64 board User Manual.


#### Default Zephyr Peripheral Mapping:


- UART_1_TX : PB6
- UART_1_RX : PB7
- UART_2_TX : PA2
- UART_2_RX : PA3
- USER_PB   : PC13
- LD2       : PA5
- I2C1_SDA  : PB9
- I2C1_SCL  : PB8
- I2C2_SDA  : PB3
- I2C2_SCL  : PB10
- I2C3_SDA  : PB4
- I2C3_SCL  : PA8


#### System Clock


Nucleo F446RE System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default, the System clock is driven by the PLL clock at 84MHz,
driven by an 8MHz high-speed external clock.


#### Serial Port


Nucleo F446RE board has 2 UARTs and 4 USARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.


#### Backup SRAM


In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB45` jumper on the back side of the board.


#### Controller Area Network


The TX/RX wires connected with D14/D15 of CN5 connector. Thus the board can be
used with RS485 CAN Shield.
