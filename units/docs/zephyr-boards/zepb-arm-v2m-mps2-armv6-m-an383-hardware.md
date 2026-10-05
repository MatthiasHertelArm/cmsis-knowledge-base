---
id: "zepb-arm-v2m-mps2-armv6-m-an383-hardware"
type: "concept"
domain: "bring-up"
title: "ARM V2M MPS2 Armv6-m (AN383): Hardware"
summary: "ARM V2M MPS2 AN383 provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/arm/mps2/doc/mps2_armv6m.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

ARM V2M MPS2 AN383 provides the following hardware components:

- ARM Cortex-M0+
- ARM IoT Subsystem for Cortex-M
- Form factor: 140x120cm
- ZBTSRAM: 8MB single cycle SRAM, 16MB PSRAM
- Video: QSVGA touch screen panel, 4bit RGB VGA connector
- Audio: Audio Codec
- Debug:

  - ARM JTAG20 connector
  - ARM parallel trace connector (MICTOR38)
  - 20 pin Cortex debug connector
  - 10 pin Cortex debug connector
  - ILA connector for FPGA debug

- Expansion

  - GPIO
  - SPI


**Note:** 4 MB of flash memory (in ZBTSRAM 1, starting at address 0x00400000) and 4 MB of RAM (in ZBTSRAM 2 & 3, starting at address 0x20000000) are available.


### Supported Features


* Refer to mps2 for details.


### Interrupt Controller


MPS2 is a Cortex-M0+ based SoC and has 6 fixed exceptions and 32 IRQs.

A Cortex-M0+ board uses vectored exceptions. This means each exception
calls a handler directly from the vector table.

Handlers are provided for exceptions 1-3, 11, and 14-15. The table here
MPS2 is a Cortex-M0+ based SoC and has 15 fixed exceptions and 45 IRQs.

+------+------------+----------------+--------------------------+
| Exc# | Name       | Remarks        | Used by Zephyr Kernel    |
+======+============+================+==========================+
| 1    | Reset      |                | system initialization    |
+------+------------+----------------+--------------------------+
| 2    | NMI        |                | system fatal error       |
+------+------------+----------------+--------------------------+
| 3    | Hard fault |                | system fatal error       |
+------+------------+----------------+--------------------------+
| 11   | SVC        |                | system calls, kernel     |
|      |            |                | run-time exceptions,     |
|      |            |                | and IRQ offloading       |
+------+------------+----------------+--------------------------+
| 14   | PendSV     |                | context switch           |
+------+------------+----------------+--------------------------+
| 15   | SYSTICK    | optional       | system clock             |
+------+------------+----------------+--------------------------+


### Pin Mapping


The ARM V2M MPS2 Board has 4 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

All GPIO controller pins are exposed via the following sequence of pin numbers:

- Pins 0 - 15 are for GPIO 0
- Pins 16 - 31 are for GPIO 1
- Pins 32 -  47 are for GPIO 2
- Pins 48 -  51 are for GPIO 3

Mapping from the ARM MPS2 Board pins to GPIO controllers:

Peripheral Mapping:

For more details please refer to MPS2 Technical Reference Manual (TRM).


### System Clock


The V2M MPS2 main clock is 24 MHz.


### Serial Port


The V2M MPS2 processor has five UARTs. Both the UARTs have only two wires for
RX/TX and no flow control (CTS/RTS) or FIFO. The Zephyr console output, by
default, is utilizing UART0.
