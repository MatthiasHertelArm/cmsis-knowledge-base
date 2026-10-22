---
id: "zepb-nucleo-h743zi-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_h743zi: Hardware"
summary: "Nucleo H743ZI provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_h743zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

Nucleo H743ZI provides the following hardware components:

- STM32H743ZI in LQFP144 package
- ARM 32-bit Cortex-M7 CPU with FPU
- Chrom-ART Accelerator
- Hardware JPEG Codec
- 480 MHz max CPU frequency
- VDD from 1.62 V to 3.6 V
- 2 MB Flash
- 1 MB SRAM
- High-resolution timer (2.1 ns)
- 32-bit timers(2)
- 16-bit timers(12)
- SPI(6)
- I2C(4)
- I2S (3)
- USART(4)
- UART(4)
- USB OTG Full Speed and High Speed(1)
- USB OTG Full Speed(1)
- CAN FD(2)
- SAI(2)
- SPDIF_Rx(4)
- HDMI_CEC(1)
- Dual Mode Quad SPI(1)
- Camera Interface
- GPIO (up to 114) with external interrupt capability
- 16-bit ADC(3) with 36 channels / 3.6 MSPS
- 12-bit DAC with 2 channels(2)
- True Random Number Generator (RNG)
- 16-channel DMA
- LCD-TFT Controller with XGA resolution


### Supported Features


For more details please refer to STM32 Nucleo-144 board User Manual.


#### Default Zephyr Peripheral Mapping:


The Nucleo H743ZI board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- UART_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- USER_PB : PC13
- LD1 : PB0
- LD2 : PE1
- LD3 : PB14
- I2C : PB8, PB9
- ADC1_INP15 : PA3
- DAC1_OUT1 : PA4
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- SPI1 NSS/SCK/MISO/MOSI : PD14/PA5/PA6/PB5 (Arduino SPI)
- CAN/CANFD : PD0, PD1


#### System Clock


Nucleo H743ZI System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 96MHz, driven by an 8MHz high-speed external clock.


#### Serial Port


Nucleo H743ZI board has 4 UARTs and 4 USARTs. The Zephyr console output is
assigned to UART3. Default settings are 115200 8N1.


#### Backup SRAM


In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB156` jumper on the back side of the board.


#### CAN, CANFD


Requires an external CAN or CANFD transceiver.
