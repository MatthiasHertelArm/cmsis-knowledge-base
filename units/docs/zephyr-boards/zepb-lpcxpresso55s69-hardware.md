---
id: "zepb-lpcxpresso55s69-hardware"
type: "concept"
domain: "bring-up"
title: "lpcxpresso55s69: Hardware"
summary: "For more information about the LPC55S69 SoC and LPCXPRESSO55S69 board, see:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/lpcxpresso55s69/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- LPC55S69 dual core Arm Cortex-M33 microcontroller running at up to 100 MHz
- Onboard, high-speed USB, Link2 debug probe with CMSIS-DAP and SEGGER J-Link
  protocol options
- UART and SPI port bridging from LPC55S69 target to USB via the onboard debug
  probe
- Hardware support for external debug probe
- 3 x user LEDs, plus Reset, ISP (3) and user buttons
- Micro SD card slot (4-bit SDIO)
- NXP MMA8652FCR1 accelerometer
- Stereo audio codec with line in/out
- High and full speed USB ports with micro A/B connector for host or device
  functionality
- MikroEletronika Click expansion option
- LPCXpresso-V3 expansion option compatible with Arduino UNO
- PMod compatible expansion / host connector

For more information about the LPC55S69 SoC and LPCXPRESSO55S69 board, see:

- LPC55S69 SoC Website
- LPC55S69 Datasheet
- LPC55S69 Reference Manual
- LPCXPRESSO55S69 Website
- LPCXPRESSO55S69 User Guide
- LPCXPRESSO55S69 Schematics
- LPCXPRESSO55S69 Debug Firmware


### Supported Features


NXP considers the LPCXpresso55S69 as the superset board for the LPC55xx
series of MCUs.  This board is a focus for NXP's Full Platform Support for
Zephyr, to better enable the entire LPC55xx series.  NXP prioritizes enabling
this board with new support for Zephyr features.


### Targets available


The default configuration file
`boards/nxp/lpcxpresso55s69/lpcxpresso55s69_lpc55s69_cpu0_defconfig`
only enables the first core.
CPU0 is the only target that can run standalone.

- *lpcxpresso55s69/lpc55s69/cpu0* secure (S) address space for CPU0
- *lpcxpresso55s69/lpc55s69/cpu0/ns* non-secure (NS) address space for CPU0
- *lpcxpresso55s69/lpc55s69/cpu1* CPU1 target, no security extensions

NS target for CPU0 does not work correctly without a secure image to configure
the system, then hand execution over to the NS environment. To enable a secure
image, run any of the `tfm_integration` samples. When using the NS target
`CONFIG_BUILD_WITH_TFM` is always enabled to ensure that a valid S image is
included during the build process.

CPU1 does not work without CPU0 enabling it.
To enable it, run one of the following samples in `subsys\ipc`:

- `ipm_mcux`
- `openamp`


### Connections and IOs


The LPC55S69 SoC has IOCON registers, which can be used to configure the
functionality of a pin.

+---------+-----------------+----------------------------+
| Name    | Function        | Usage                      |
+=========+=================+============================+
| PIO0_26 | SPI             | SPI MOSI                   |
+---------+-----------------+----------------------------+
| PIO0_27 | USART           | USART TX                   |
+---------+-----------------+----------------------------+
| PIO0_29 | USART           | USART RX                   |
+---------+-----------------+----------------------------+
| PIO0_30 | USART           | USART TX                   |
+---------+-----------------+----------------------------+
| PIO1_1  | SPI             | SPI SSEL                   |
+---------+-----------------+----------------------------+
| PIO1_2  | SPI             | SPI SCK                    |
+---------+-----------------+----------------------------+
| PIO1_3  | SPI             | SPI MISO                   |
+---------+-----------------+----------------------------+
| PIO1_4  | GPIO            | RED LED                    |
+---------+-----------------+----------------------------+
| PIO1_6  | GPIO            | BLUE_LED                   |
+---------+-----------------+----------------------------+
| PIO1_7  | GPIO            | GREEN LED                  |
+---------+-----------------+----------------------------+
| PIO1_20 | I2C             | I2C SCL                    |
+---------+-----------------+----------------------------+
| PIO1_21 | I2C             | I2C SDA                    |
+---------+-----------------+----------------------------+
| PIO1_24 | USART           | USART RX                   |
+---------+-----------------+----------------------------+
| PIO0_20 | I2S             | I2S DATAOUT                |
+---------+-----------------+----------------------------+
| PIO0_19 | I2S             | I2S TX WS                  |
+---------+-----------------+----------------------------+
| PIO0_21 | I2S             | I2S TX SCK                 |
+---------+-----------------+----------------------------+
| PIO1_13 | I2S             | I2S DATAIN                 |
+---------+-----------------+----------------------------+
| PIO0_15 | SCT0_OUT2       | PWM                        |
+---------+-----------------+----------------------------+
| PIO0_24 | SD0_D0          | SDHC                       |
+---------+-----------------+----------------------------+
| PIO0_25 | SD0_D1          | SDHC                       |
+---------+-----------------+----------------------------+
| PIO0_31 | SD0_D2          | SDHC                       |
+---------+-----------------+----------------------------+
| PIO0_7  | SD0_CLK         | SDHC                       |
+---------+-----------------+----------------------------+
| PIO0_8  | SD0_CMD         | SDHC                       |
+---------+-----------------+----------------------------+
| PIO0_9  | SD0_POW_EN      | SDHC                       |
+---------+-----------------+----------------------------+
| PIO1_0  | SD0_D3          | SDHC                       |
+---------+-----------------+----------------------------+


### Memory mappings


There are multiple memory configurations, they all start from the
MCUboot partitioning which looks like the table below

+----------+------------------+---------------------------------+
| Name     | Address[Size]    | Comment                         |
+==========+==================+=================================+
| boot     | 0x00000000[32K]  | Bootloader                      |
+----------+------------------+---------------------------------+
| slot0    | 0x00008000[160k] | Image that runs after boot      |
+----------+------------------+---------------------------------+
| slot0_ns | 0x00030000[96k]  | Second image, core 1 or NS      |
+----------+------------------+---------------------------------+
| slot1    | 0x00048000[160k] | Updates slot0 image             |
+----------+------------------+---------------------------------+
| slot1_ns | 0x00070000[96k]  | Updates slot0_ns image          |
+----------+------------------+---------------------------------+
| storage  | 0x00088000[50k]  | File system, persistent storage |
+----------+------------------+---------------------------------+

See below examples of how this partitioning is used
