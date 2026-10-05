---
id: "zepb-b-u585i-iot02a-hardware"
type: "concept"
domain: "bring-up"
title: "b_u585i_iot02a: Hardware"
summary: "The STM32U585xx devices are an ultra-low-power microcontrollers family (STM32U5 Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core. They operate at a frequency of up to 160 MHz."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/b_u585i_iot02a/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/b_u585i_iot02a/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

The STM32U585xx devices are an ultra-low-power microcontrollers family (STM32U5
Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 160 MHz.

- Ultra-low-power with FlexPowerControl (down to 300 nA Standby mode and 19.5 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M33 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 1.5 DMPIS/MHz (Drystone 2.1)
  - 651 CoreMark® (4.07 CoreMark® /MHZ)

- Security and cryptography

  - Arm®  TrustZone® and securable I/Os memories and peripherals
  - Flexible life cycle scheme with RDP (readout protection) and password protected debug
  - Root of trust thanks to unique boot entry and secure hide protection area (HDP)
  - Secure Firmware Installation thanks to embedded Root Secure Services
  - Secure data storage with hardware unique key (HUK)
  - Secure Firmware Update support with TF-M
  - 2 AES coprocessors including one with DPA resistance
  - Public key accelerator, DPA resistant
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - Active tampers
  - True Random Number Generator NIST SP800-90B compliant
  - 96-bit unique ID
  - 512-byte One-Time Programmable for user data
  - Active tampers

- Clock management:

  - 4 to 50 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC (±1%)
  - Internal low-power 32 kHz RC (±5%)
  - 2 internal multispeed 100 kHz to 48 MHz oscillators, including one auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 3 PLLs for system clock, USB, audio, ADC
  - Internal 48 MHz with clock recovery

- Power management

  - Embedded regulator (LDO)
  - Embedded SMPS step-down converter supporting switch on-the-fly and voltage scaling

- RTC with HW calendar and calibration
- Up to 136 fast I/Os, most 5 V-tolerant, up to 14 I/Os with independent supply down to 1.08 V
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- Up to 17 timers and 2 watchdogs

  - 2x 16-bit advanced motor-control
  - 2x 32-bit and 5 x 16-bit general purpose
  - 4x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer

- ART accelerator

  - 8-Kbyte instruction cache allowing 0-wait-state execution from Flash and
    external memories: up to 160 MHz, MPU, 240 DMIPS and DSP
  - 4-Kbyte data cache for external memories

- Memories

  - 2-Mbyte Flash memory with ECC, 2 banks read-while-write, including 512 Kbytes with 100 kcycles
  - 786-Kbyte SRAM with ECC OFF or 722-Kbyte SRAM including up to 322-Kbyte SRAM with ECC ON
  - External memory interface supporting SRAM, PSRAM, NOR, NAND and FRAM memories
  - 2 Octo-SPI memory interfaces

- Rich analog peripherals (independent supply)

  - 14-bit ADC 2.5-Msps, resolution up to 16 bits with hardware oversampling
  - 12-bit ADC 2.5-Msps, with hardware oversampling, autonomous in Stop 2 mode
  - 12-bit DAC, low-power sample and hold
  - 2 operational amplifiers with built-in PGA
  - 2 ultra-low-power comparators

- Up to 22 communication interfaces

  - USB Type-C / USB power delivery controller
  - USB OTG 2.0 full-speed controller
  - 2x SAIs (serial audio interface)
  - 4x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 6x USARTs (ISO 7816, LIN, IrDA, modem)
  - 3x SPIs (5x SPIs with dual OCTOSPI in SPI mode)
  - 1x FDCAN
  - 2x SDMMC interface
  - 16- and 4-channel DMA controllers, functional in Stop mode
  - 1 multi-function digital filter (6 filters)+ 1 audio digital filter with
    sound-activity detection

- CRC calculation unit
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™
- True Random Number Generator (RNG)

- Graphic features

  - Chrom-ART Accelerator (DMA2D) for enhanced graphic content creation
  - 1 digital camera interface

- Mathematical co-processor

 - CORDIC for trigonometric functions acceleration
 - FMAC (filter mathematical accelerator)



More information about STM32U585AI can be found here:

- STM32U585 on www.st.com
- STM32U585 reference manual



### Supported Features



### Zephyr board options


The STM32U585i is an SoC with Cortex-M33 architecture. Zephyr provides support
for building for both Secure and Non-Secure firmware.

The BOARD options are summarized below:

+-------------------------------+-------------------------------------------+
| BOARD                         | Description                               |
+===============================+===========================================+
| b_u585i_iot02a                | For building Trust Zone Disabled firmware |
+-------------------------------+-------------------------------------------+
| b_u585i_iot02a/stm32u585xx/ns | For building Non-Secure firmware          |
+-------------------------------+-------------------------------------------+

Here are the instructions to build Zephyr with a non-secure configuration,
using tfm_ipc sample:

```bash

$ west build -b b_u585i_iot02a/stm32u585xx/ns samples/tfm_integration/tfm_ipc/
```
Once done, before flashing, you need to first run a generated script that
will set platform option bytes config and erase platform (among others,
option bit TZEN will be set).

```bash

$ ./build/tfm/api_ns/regression.sh
$ west flash
```
Please note that, after having run a TFM sample on the board, you will need to
run `./build/tfm/api_ns/regression.sh` once more to clean up the board from secure
options and get back the platform back to a "normal" state and be able to run
usual, non-TFM, binaries.
Also note that, even then, TZEN will remain set, and you will need to use
STM32CubeProgrammer_ to disable it fully, if required.


### Connections and IOs


B_U585I_IOT02A Discovery kit has 9 GPIO controllers (from A to I). These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to B U585I IOT02A board User Manual.


#### Default Zephyr Peripheral Mapping:


- UART_1 TX/RX : PA9/PA10 (ST-Link Virtual Port Com)
- LD1 : PH7
- LD2 : PH6
- user button : PC13
- SPI1 NSS/SCK/MISO/MOSI : PE12/P13/P14/P15 (Arduino SPI)
- I2C_1 SDA/SDL : PB9/PB8 (Arduino I2C)
- I2C_2 SDA/SDL : PH5/PH4
- DAC1 CH1 : PA4 (STMOD+1)
- ADC1_IN15 : PB0
- USB OTG : PA11/PA12
- PWM4 : CN14 PB6
- PWM3 : CN4 PE4


#### System Clock


B_U585I_IOT02A Discovery System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default the System clock is driven by the PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.


#### Serial Port


B_U585I_IOT02A Discovery kit has 4 U(S)ARTs. The Zephyr console output is assigned to UART1.
Default settings are 115200 8N1.



#### Backup SRAM


In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB6` jumper on the back side of the board.
