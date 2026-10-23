---
id: "zepb-mps3-hardware"
type: "concept"
domain: "bring-up"
title: "mps3: Hardware"
summary: "ARM MPS3 provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/arm/mps3/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps3/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

ARM MPS3 provides the following hardware components:

- CPU

  - AN547 and AN552 support Arm Cortex-M55 CPU and
    Soft Macro Model (SMM) implementation of SSE-300 subsystem
  - AN555 support Arm Cortex-M85 CPU and
    Soft Macro Model (SMM) implementation of SSE-310 subsystem
  - AN536 supports Arm Cortex-R52 CPU and
    an example Cortex-R52x2 subsystem

- Memory

  - 8MB BRAM
  - 4GB DDR4 SODIMM (by default, upgradeable to 8GB)
  - 16GB eMMC
  - 8MB QSPI Flash

- Debug

  - P‐JTAG, F-JTAG, SWD, 4-bit trace, 16-bit trace
  - Four serial ports over USB

- Interface

  - AHB GPIO
  - UART
  - SPI
  - I2C
  - I2S
  - Color LCD serial interface
  - Ethernet
  - VGA

- On-board Peripherals

  - Color LCD
  - 10 LEDs
  - 8 Switches
  - 2 user push buttons


### Supported Features



### Serial Port


The MPS3 has six UARTs. The Zephyr console output by default, uses
UART0, which is exposed over the Debug USB interface (J8).

Serial port 0 on the Debug USB interface is the MCC board control console.

Serial port 1 on the Debug USB interface is connected to UART 0.

Serial port 2 on the Debug USB interface is connected to UART 1.

Serial port 3 on the Debug USB interface is connected to UART 2.

For AN536, the Cortex-R52x2 subsystem provides LLPP UART0 and LLPP UART1
as CPU-private UARTs, and additional shared CMSDK UARTs. The
`mps3/an536/cpu0` target uses LLPP UART0 as the Zephyr console.

.. Programming and Debugging:
