---
id: "zepb-nucleo-wl55jc-hardware"
type: "concept"
domain: "bring-up"
title: "nucleo_wl55jc: Hardware"
summary: "The STM32WL55JC long-range wireless and ultra-low-power devices embed a powerful and ultra-low-power LPWAN-compliant radio solution, enabling the following modulations: LoRa®, (G)FSK, (G)MSK, and BPSK It provides the following hardware capabilities:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_wl55jc/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

The STM32WL55JC long-range wireless and ultra-low-power devices embed a powerful
and ultra-low-power LPWAN-compliant radio solution, enabling the following
modulations: LoRa®, (G)FSK, (G)MSK, and BPSK
It provides the following hardware capabilities:

- Radio

  - Frequency range: 150 MHz to 960 MHz
  - Modulation: LoRa®, (G)FSK, (G)MSK and BPSK
  - RX sensitivity: –123 dBm for 2-FSK(at 1.2 Kbit/s), –148 dBm for LoRa®
    (at 10.4 kHz, spreading factor 12)
  - Transmitter high output power, programmable up to +22 dBm
  - Transmitter low output power, programmable up to +15 dBm
  - Compliant with the following radio frequency regulations such as
    ETSI EN 300 220, EN 300 113, EN 301 166, FCC CFR 47 Part 15, 24, 90, 101
    and the Japanese ARIB STD-T30, T-67, T-108
  - Compatible with standardized or proprietary protocols such as LoRaWAN®,
    Sigfox™, W-MBus and more (fully open wireless system-on-chip)

- Core

  - 32-bit Arm® Cortex®-M4 CPU

    - Adaptive real-time accelerator (ART Accelerator) allowing 0-wait-state
      execution from Flash memory, frequency up to 48 MHz, MPU
      and DSP instructions
    - 1.25 DMIPS/MHz (Dhrystone 2.1)

  - 32-bit Arm®Cortex®-M0+ CPU

    - Frequency up to 48 MHz, MPU
    - 0.95 DMIPS/MHz (Dhrystone 2.1)

- Security and identification

  - Hardware encryption AES 256-bit
  - True random number generator (RNG)
  - Sector protection against read/write operations (PCROP, RDP, WRP)
  - CRC calculation unit
  - Unique device identifier (64-bit UID compliant with IEEE 802-2001 standard)
  - 96-bit unique die identifier
  - Hardware public key accelerator (PKA)
  - Key management services
  - Secure sub-GHz MAC layer
  - Secure firmware update (SFU)
  - Secure firmware install (SFI)

- Supply and reset management

  - High-efficiency embedded SMPS step-down converter
  - SMPS to LDO smart switch
  - Ultra-safe, low-power BOR (brownout reset) with 5 selectable thresholds
  - Ultra-low-power POR/PDR
  - Programmable voltage detector (PVD)
  - VBAT mode with RTC and 20x32-byte backup registers

- Clock sources

  - 32 MHz crystal oscillator
  - TCXO support: programmable supply voltage
  - 32 kHz oscillator for RTC with calibration
  - High-speed internal 16 MHz factory trimmed RC (± 1 %)
  - Internal low-power 32 kHz RC
  - Internal multi-speed low-power 100 kHz to 48 MHz RC
  - PLL for CPU, ADC and audio clocks

- Memories

  - 256-Kbyte Flash memory
  - 64-Kbyte RAM
  - 20x32-bit backup register
  - Bootloader supporting USART and SPI interfaces
  - OTA (over-the-air) firmware update capable
  - Sector protection against read/write operations

- Rich analog peripherals (down to 1.62 V)

  - 12-bit ADC 2.5 Msps, up to 16 bits with hardware oversampling,
    conversion range up to 3.6 V
  - 12-bit DAC, low-power sample-and-hold
  - 2x ultra-low-power comparators

- System peripherals

  - Mailbox and semaphores for communication between Cortex®-M4 and Cortex®-M0+
    firmware

- Controllers

  - 2x DMA controller (7 channels each) supporting ADC, DAC, SPI, I2C, LPUART,
    USART, AES and timers
  - 2x USART (ISO 7816, IrDA, SPI)
  - 1x LPUART (low-power)
  - 2x SPI 16 Mbit/s (1 over 2 supporting I2S)
  - 3x I2C (SMBus/PMBus™)
  - 2x 16-bit 1-channel timer
  - 1x 16-bit 4-channel timer (supporting motor control)
  - 1x 32-bit 4-channel timer
  - 3x 16-bit ultra-low-power timer
  - 1x RTC with 32-bit sub-second wakeup counter
  - 1x independent SysTick
  - 1x independent watchdog
  - 1x window watchdog

- Up to 43 I/Os, most 5 V-tolerant
- Development support
  - Serial-wire debug (SWD), JTAG
  - Dual CPU cross trigger capabilities


More information about STM32WL55JC can be found here:

- STM32WL55JC on www.st.com
- STM32WL55JC datasheet
- STM32WL55JC reference manual


### Supported Features



### Connections and IOs


Nucleo WL55JC Board has 4 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.


#### Default Zephyr Peripheral Mapping:


- LPUART_1 TX/RX : PA3/PA2 (ST-Link Virtual Port Com)
- I2C_2_SCL : PA12 (Arduino I2C)
- I2C_2_SDA : PA11 (Arduino I2C)
- SPI_1_NSS : PA4 (arduino_spi)
- SPI_1_SCK : PA5 (arduino_spi)
- SPI_1_MISO : PA6 (arduino_spi)
- SPI_1_MOSI : PA7 (arduino_spi)
- ADC1_IN5 : PB1 (Arduino pin A0)
- DAC1_OUT1 : PA10 (Arduino pin A2)


#### System Clock


Nucleo WL55JC System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by HSE clock at
32MHz.


#### Serial Port


Nucleo WL55JC board has 2 (LP)U(S)ARTs. The Zephyr console output is assigned
to LPUART_1.
Default settings are 115200 8N1.
