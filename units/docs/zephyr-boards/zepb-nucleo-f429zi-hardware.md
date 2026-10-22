---
id: "zepb-nucleo-f429zi-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_f429zi: Hardware"
summary: "The Nucleo F429ZI provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_f429zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f429zi/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

The Nucleo F429ZI provides the following hardware components:

- STM32F429ZIT6 in LQFP144 package
- ARM® 32-bit Cortex®-M4 CPU with FPU
- 180 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 2 MB Flash
- 256+4 KB SRAM including 64-Kbyte of core coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer
- General Purpose Timers (17)
- Watchdog Timers (2)
- USART/UART (4/4)
- I2C (3)
- SPI (6)
- SDIO
- 2xCAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA
- 8- to 14-bit parallel camera
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F429ZI can be found here:

- STM32F429ZI on www.st.com
- STM32F429 reference manual
- STM32F429 datasheet


### Supported Features



### Connections and IOs


The Nucleo F429ZI Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.


#### Available pins:

For more details please refer to STM32 Nucleo-144 board User Manual.


#### Default Zephyr Peripheral Mapping:


The Nucleo F429ZI board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows

- UART_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- UART_6 TX/RX : PG14/PG9 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI1 NSS/SCK/MISO/MOSI : PD14/PA5/PA6/PA7 (Arduino SPI)
- PWM_2_CH1 : PE13
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- USER_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- USB DM : PA11
- USB DP : PA12
- ADC1 : PA0


#### System Clock


The Nucleo F429ZI System Clock could be driven by an internal or external oscillator,
as well as by the main PLL clock. By default System clock is driven by PLL clock at 180MHz,
driven by an 8MHz high speed external clock.


#### Serial Port


The Nucleo F429ZI board has 8 UARTs. The Zephyr console output is assigned to UART3.
Default settings are 115200 8N1.
