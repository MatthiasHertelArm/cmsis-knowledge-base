---
id: "zepb-nucleo-f401re-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_f401re: Hardware"
summary: "Nucleo F401RE provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_f401re/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f401re/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

Nucleo F401RE provides the following hardware components:

- STM32F401RET6 in LQFP64 package
- ARM® 32-bit Cortex®-M4 CPU with FPU
- 84 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 512 KB Flash
- 96 KB SRAM
- GPIO with external interrupt capability
- 12-bit ADC with 16 channels
- RTC
- Advanced-control Timer
- General Purpose Timers (7)
- Watchdog Timers (2)
- USART/UART (3)
- I2C (3)
- SPI (4)
- SDIO
- USB 2.0 OTG FS
- DMA Controller

More information about STM32F401RE can be found here:

- STM32F401RE on www.st.com
- STM32F401 reference manual


### Supported Features



### Pin Mapping


Nucleo F401RE Board has 6 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.


#### Available pins:

For more details please refer to STM32 Nucleo-64 board User Manual.


#### Default Zephyr Peripheral Mapping:


- UART_1 TX/RX : PB6/PB7
- UART_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI1 CS/SCK/MISO/MOSI : PB6/PA5/PA6/PA7 (Arduino SPI)
- PWM_2_CH1 : PA0
- USER_PB   : PC13
- LD2       : PA5


### System Clock


Nucleo F401RE System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 84MHz,
driven by 8MHz high speed external clock.


### Serial Port


Nucleo F401RE board has 3 UARTs. The Zephyr console output is assigned to UART2.
Default settings are 115200 8N1.


### I2C


Nucleo F401RE board has up to 3 I2Cs. The default I2C mapping for Zephyr is:

- I2C1_SCL : PB8
- I2C1_SDA : PB9
