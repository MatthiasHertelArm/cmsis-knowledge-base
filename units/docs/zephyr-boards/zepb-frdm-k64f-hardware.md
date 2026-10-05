---
id: "zepb-frdm-k64f-hardware"
type: "concept"
domain: "bring-up"
title: "frdm_k64f: Hardware"
summary: "For more information about the K64F SoC and FRDM-K64F board:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/frdm_k64f/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

- MK64FN1M0VLL12 MCU (120 MHz, 1 MB flash memory, 256 KB RAM, low-power,
  crystal-less USB, and 100 Low profile Quad Flat Package (LQFP))
- Dual role USB interface with micro-B USB connector
- RGB LED
- FXOS8700CQ accelerometer and magnetometer
- Two user push buttons
- Flexible power supply option - OpenSDAv2 USB, Kinetis K64 USB, and external source
- Easy access to MCU input/output through Arduino* R3 compatible I/O connectors
- Programmable OpenSDAv2 debug circuit supporting the CMSIS-DAP Interface
  software that provides:

  - Mass storage device (MSD) flash programming interface
  - CMSIS-DAP debug interface over a driver-less USB HID connection providing
    run-control debugging and compatibility with IDE tools
  - Virtual serial port interface
  - Open source CMSIS-DAP software project

- Ethernet
- SDHC

For more information about the K64F SoC and FRDM-K64F board:

- K64F Website
- K64F Datasheet
- K64F Reference Manual
- FRDM-K64F Website
- FRDM-K64F User Guide
- FRDM-K64F Schematics


### Supported Features


NXP considers the FRDM-K64F as the superset board for the Kinetis K
series of MCUs.  This board is a focus for NXP's Full Platform Support for
Zephyr, to better enable the entire Kinetis K series.  NXP prioritizes enabling
this board with new support for Zephyr features.


### Connections and IOs


The K64F SoC has five pairs of pinmux/gpio controllers.

+-------+-----------------+---------------------------+
| Name  | Function        | Usage                     |
+=======+=================+===========================+
| PTB22 | GPIO            | Red LED                   |
+-------+-----------------+---------------------------+
| PTE26 | GPIO            | Green LED                 |
+-------+-----------------+---------------------------+
| PTB21 | GPIO            | Blue LED                  |
+-------+-----------------+---------------------------+
| PTC6  | GPIO            | SW2 / FXOS8700 INT1       |
+-------+-----------------+---------------------------+
| PTC13 | GPIO            | FXOS8700 INT2             |
+-------+-----------------+---------------------------+
| PTA4  | GPIO            | SW3                       |
+-------+-----------------+---------------------------+
| PTB10 | ADC             | ADC1 channel 14           |
+-------+-----------------+---------------------------+
| PTB16 | UART0_RX        | UART Console              |
+-------+-----------------+---------------------------+
| PTB17 | UART0_TX        | UART Console              |
+-------+-----------------+---------------------------+
| PTB18 | CAN0_TX         | CAN TX                    |
+-------+-----------------+---------------------------+
| PTB19 | CAN0_RX         | CAN RX                    |
+-------+-----------------+---------------------------+
| PTC8  | PWM             | PWM_3 channel 4           |
+-------+-----------------+---------------------------+
| PTC9  | PWM             | PWM_3 channel 5           |
+-------+-----------------+---------------------------+
| PTC16 | UART3_RX        | UART BT HCI               |
+-------+-----------------+---------------------------+
| PTC17 | UART3_TX        | UART BT HCI               |
+-------+-----------------+---------------------------+
| PTD0  | SPI0_PCS0       | SPI                       |
+-------+-----------------+---------------------------+
| PTD1  | SPI0_SCK        | SPI                       |
+-------+-----------------+---------------------------+
| PTD2  | SPI0_SOUT       | SPI                       |
+-------+-----------------+---------------------------+
| PTD3  | SPI0_SIN        | SPI                       |
+-------+-----------------+---------------------------+
| PTE24 | I2C0_SCL        | I2C / FXOS8700            |
+-------+-----------------+---------------------------+
| PTE25 | I2C0_SDA        | I2C / FXOS8700            |
+-------+-----------------+---------------------------+
| PTA5  | MII0_RXER       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA12 | MII0_RXD1       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA13 | MII0_RXD0       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA14 | MII0_RXDV       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA15 | MII0_TXEN       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA16 | MII0_TXD0       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA17 | MII0_TXD1       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTA28 | MII0_TXER       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTB0  | MII0_MDIO       | Ethernet                  |
+-------+-----------------+---------------------------+
| PTB1  | MII0_MDC        | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC16 | ENET0_1588_TMR0 | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC17 | ENET0_1588_TMR1 | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC18 | ENET0_1588_TMR2 | Ethernet                  |
+-------+-----------------+---------------------------+
| PTC19 | ENET0_1588_TMR3 | Ethernet                  |
+-------+-----------------+---------------------------+


**Note:** Do not enable Ethernet and UART BT HCI simultaneously because they conflict on PTC16-17.


### System Clock


The K64F SoC is configured to use the 50 MHz external oscillator on the board
with the on-chip PLL to generate a 120 MHz system clock.


### Serial Port


The K64F SoC has six UARTs. One is configured for the console, another for BT
HCI, and the remaining are not used.


### USB


The K64F SoC has a USB OTG (USBOTG) controller that supports both
device and host functions through its micro USB connector (K64F USB).
Only USB device function is supported in Zephyr at the moment.


### CAN


The FRDM-K64F board does not come with an onboard CAN transceiver. In order to
use the CAN bus, an external CAN bus transceiver must be connected to `PTB18`
(`CAN0_TX`) and `PTB19` (`CAN0_RX`).
