---
id: "zepb-nucleo-h563zi-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_h563zi: Hardware"
summary: "The STM32H563xx devices are high-performance microcontrollers from the STM32H5 Series based on the high-performance Arm® Cortex®-M33 32-bit RISC core. They operate at a frequency of up to 250 MHz."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_h563zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

The STM32H563xx devices are high-performance microcontrollers from the STM32H5
Series based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 250 MHz.

- Core: ARM® 32-bit Cortex®-M33 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 375 DMPIS/MHz (Dhrystone 2.1)

- Security

  - Arm® TrustZone® with ARMv8-M mainline security extension
  - Up to 8 configurable SAU regions
  - TrustZone® aware and securable peripherals
  - Flexible lifecycle scheme with secure debug authentication
  - SFI (secure firmware installation)
  - Secure firmware upgrade support with TF-M
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - Active tampers

- Clock management:

  - 25 MHz crystal oscillator (HSE)
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 64 MHz (HSI) trimmable by software
  - Internal low-power 32 kHz RC (LSI)(±5%)
  - Internal 4 MHz oscillator (CSI), trimmable by software
  - Internal 48 MHz (HSI48) with recovery system
  - 3 PLLs for system clock, USB, audio, ADC

- Power management

  - Embedded regulator (LDO) with three configurable range output to supply the digital circuitry
  - Embedded SMPS step-down converter

- RTC with HW calendar, alarms and calibration
- Up to 139 fast I/Os, most 5 V-tolerant, up to 10 I/Os with independent supply down to 1.08 V
- Up to 16 timers and 2 watchdogs

  - 12x 16-bit
  - 2x 32-bit timers with up to 4 IC/OC/PWM or pulse counter and quadrature (incremental) encoder input
  - 6x 16-bit low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer

- Memories

  - Up to 2 MB Flash, 2 banks read-while-write
  - 1 Kbyte OTP (one-time programmable)
  - 640 KB of SRAM including 64 KB with hardware parity check and 320 Kbytes with flexible ECC
  - 4 Kbytes of backup SRAM available in the lowest power modes
  - Flexible external memory controller with up to 16-bit data bus: SRAM, PSRAM, FRAM, SDRAM/LPSDR SDRAM, NOR/NAND memories
  - 1x OCTOSPI memory interface with on-the-fly decryption and support for serial PSRAM/NAND/NOR, Hyper RAM/Flash frame formats
  - 2x SD/SDIO/MMC interfaces

- Rich analog peripherals (independent supply)

  - 2x 12-bit ADC with up to 5 MSPS in 12-bit
  - 1x 12-bit D/A with 2 channels
  - 1x Digital temperature sensor

- 34x communication interfaces

  - 1x USB Type-C / USB power-delivery controller
  - 1x USB 2.0 full-speed host and device
  - 4x I2C FM+ interfaces (SMBus/PMBus)
  - 1x I3C interface
  - 12x U(S)ARTS (ISO7816 interface, LIN, IrDA, modem control)
  - 1x LP UART
  - 6x SPIs including 3 muxed with full-duplex I2S
  - 5x additional SPI from 5x USART when configured in Synchronous mode
  - 2x SAI
  - 2x FDCAN
  - 1x SDMMC interface
  - 2x 16 channel DMA controllers
  - 1x 8- to 14- bit camera interface
  - 1x HDMI-CEC
  - 1x Ethernel MAC interface with DMA controller
  - 1x 16-bit parallel slave synchronous-interface

- CORDIC for trigonometric functions acceleration
- FMAC (filter mathematical accelerator)
- CRC calculation unit
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32H563ZI can be found here:

- STM32H563ZI on www.st.com
- STM32H563 reference manual


### Supported Features



### Connections and IOs


Nucleo H563ZI Board has 9 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to STM32H5 Nucleo-144 board User Manual.


#### Default Zephyr Peripheral Mapping:


- ADC1 channel 3 input: PA6
- ADC1 channel 15 input: PA3
- DAC1 channel 2 output: PA5
- CAN/CANFD TX/RX: PD1/PD0
- LD1 (green): PB0
- LD2 (yellow): PF4
- LD3 (red): PG4
- LPUART1 TX/RX : PB6/PB7 (Arduino LPUART1)
- SPI1 SCK/MISO/MOSI/CS: PA5/PG9/PB5/PD14
- UART3 TX/RX : PD8/PD9 (VCP)
- USER_PB : PC13
- I3C1: PD12(SCL) & PD13(SDA)


#### System Clock


Nucleo H563ZI System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
240MHz, driven by 8MHz external clock provided from the STLINK-V3EC.


#### Serial Port


Nucleo H563ZI board has up to 12 U(S)ARTs. The Zephyr console output is assigned
to USART3. Default settings are 115200 8N1.


#### Backup SRAM


In order to test backup SRAM, you may want to disconnect VBAT from VDD_MCU.
You can do it by removing `SB55` jumper on the back side of the board.
VBAT can be provided via the left ST Morpho connector's pin 33.
