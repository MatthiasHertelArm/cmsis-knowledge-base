---
id: "zepb-nucleo-f756zg-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_f756zg: Hardware"
summary: "Nucleo F756ZG provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_f756zg/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f756zg/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

Nucleo F756ZG provides the following hardware components:

- STM32F756ZG in LQFP144 package
- ARM 32-bit Cortex-M7 CPU with FPU
- Chrom-ART Accelerator
- ART Accelerator
- 216 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 1 MB Flash
- 320 KB SRAM
- 16-bit timers(10)
- 32-bit timers(2)
- SPI(6)
- I2C(4)
- I2S (3)
- USART(4)
- UART(4)
- USB OTG Full Speed and High Speed(1)
- USB OTG Full Speed(1)
- CAN(2)
- SAI(2)
- SPDIF_Rx(4)
- HDMI_CEC(1)
- Dual Mode Quad SPI(1)
- Camera Interface
- GPIO(up to 168) with external interrupt capability
- 12-bit ADC(3) with 24 channels / 2.4 MSPS
- 12-bit DAC with 2 channels(2)
- True Random Number Generator (RNG)
- 16-channel DMA
- LCD-TFT Controller with XGA resolution


### Supported Features


For more details please refer to STM32 Nucleo-144 board User Manual.


#### Default Zephyr Peripheral Mapping:


The Nucleo F756ZG board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- UART_2 TX/RX/RTS/CTS : PD5/PD6/PD4/PD3
- UART_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- UART_6 TX/RX : PG14/PG9 (Arduino UART)
- USER_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- USB DM : PA11
- USB DP : PA12
- I2C : PB8, PB9
- PWM : PE13
- SPI : PD14, PA5, PA6, PA7

Note. The Arduino Uno v3 specified SPI device conflicts with the on-board ETH
device on pin PA7.


#### System Clock


Nucleo F756ZG System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 72MHz, driven by an 8MHz high-speed external clock.


#### Serial Port


Nucleo F756ZG board has 4 UARTs and 4 USARTs. The Zephyr console output is
assigned to UART3. Default settings are 115200 8N1.
