---
id: "zepb-arm-mps2-an521-hardware"
type: "concept"
domain: "bring-up"
title: "ARM MPS2+ AN521: Hardware"
summary: "ARM MPS2+ AN521 provides the following hardware components:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/arm/mps2/doc/mps2_an521.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#hardware"
license: "Apache-2.0"
mode: "V"
---

ARM MPS2+ AN521 provides the following hardware components:

- Dual core ARM Cortex-M33
- Soft Macro Model (SMM) implementation of SSE-200 subsystem
- Memory

  - 4MB of code memory (SSRAM1)
  - 4MB of SRAM (SSRAM2 and SSRAM3)
  - 16MB of parallel SRAM (PSRAM, non-secure only)
  - 8KB of NVM code

- Debug

  - P-JTAG, SWD & 16-bit TRACE
  - UART port

- Interface

  - AHB GPIO connected to the EXP port
  - UART
  - SPI
  - I2C
  - I2S
  - Color LCD serial interface
  - Ethernet
  - VGA

- On-board Peripherals

  - Color LCD
  - 8 LEDs
  - 8 Switches
  - External SSRAM1, SSRAM2 & SSRAM3
  - SMSC9220
  - CS42L52



### User push buttons


The mps2/an521 board provides the following user push buttons:

- ON power on
- nSRST: Cortex-M33 system reset and CoreSight debug reset
- USERPB0 and USERPB1: User defined buttons



### Supported Features


* Refer to mps2 for details.


### Interrupt Controller


MPS2+ AN521 is a Cortex-M33 based SoC and has 15 fixed exceptions and 77 IRQs.

A Cortex-M33-based board uses vectored exceptions. This means each exception
calls a handler directly from the vector table.

Zephyr provides handlers for exceptions 1-7, 11, 12, 14, and 15, as listed
in the following table:

+------+------------+----------------+--------------------------+
| Exc# | Name       | Remarks        | Used by Zephyr Kernel    |
+======+============+================+==========================+
|  1   | Reset      |                | system initialization    |
+------+------------+----------------+--------------------------+
|  2   | NMI        |                | system fatal error       |
+------+------------+----------------+--------------------------+
|  3   | Hard fault |                | system fatal error       |
+------+------------+----------------+--------------------------+
|  4   | MemManage  | MPU fault      | system fatal error       |
+------+------------+----------------+--------------------------+
|  5   | Bus        |                | system fatal error       |
+------+------------+----------------+--------------------------+
|  6   | Usage      | Undefined      | system fatal error       |
|      | fault      | instruction,   |                          |
|      |            | or switch      |                          |
|      |            | attempt to ARM |                          |
|      |            | mode           |                          |
+------+------------+----------------+--------------------------+
|  7   | SecureFault| Unauthorized   | system fatal error       |
|      |            | access to      |                          |
|      |            | secure region  |                          |
|      |            | from ns space  |                          |
+------+------------+----------------+--------------------------+
|  8   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+
|  9   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+
| 10   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+
| 11   | SVC        |                | system calls, kernel     |
|      |            |                | run-time exceptions,     |
|      |            |                | and IRQ offloading       |
+------+------------+----------------+--------------------------+
| 12   | Debug      |                | system fatal error       |
|      | monitor    |                |                          |
+------+------------+----------------+--------------------------+
| 13   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+
| 14   | PendSV     |                | context switch           |
+------+------------+----------------+--------------------------+
| 15   | SYSTICK    |                | system clock             |
+------+------------+----------------+--------------------------+
| 16   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+
| 17   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+
| 18   | Reserved   |                | not handled              |
+------+------------+----------------+--------------------------+


### Pin Mapping


The ARM MPS2+ AN521 Board has 4 CMSDK AHB GPIO controllers. Each providing 16
bits of IO. These controllers are responsible for pin-muxing, input/output,
pull-up, etc.

All GPIO controller pins are exposed via the following sequence of pin numbers:

- Pins 0 - 15 are for GPIO0
- Pins 16 -  31 are for GPIO1
- Pins 32 -  47 are for GPIO2
- Pins 48 -  51 are for GPIO3

Mapping from the ARM MPS2+ AN521 Board pins to GPIO controllers:

Peripheral Mapping:

For more details refer to MPS2+ AN521 Technical Reference Manual (TRM).


### LED


MPS2+ has 8 built-in LEDs connected to Serial Configuration Controller (SCC).


**Note:** The SCC register CFG_REG1 Bits [7:0] for LEDa, 0 = OFF 1 = ON.


### System Clock


MPS2+ AN521 has several clocks connected:


### Serial Port


The MPS2+ AN521 has five UARTs. The Zephyr console output by default, uses
UART0, which is J10 on the board.

UART2 is reserved. And UART 1, 3 and 4 are alt-functions on the EXP ports.


### Security components


- Implementation Defined Attribution Unit (IDAU). The IDAU is used to define
  secure and non-secure memory maps. By default, all of the memory space is
  defined to be secure accessible only
- Secure and Non-secure peripherals via the Peripheral Protection Controller
  (PPC). Peripherals can be assigned as secure or non-secure accessible
- Secure boot
- Secure AMBA® interconnect


### Serial Configuration Controller (SCC)


The MPS2+ AN521 implements a Serial Configuration Control (SCC) register.
The purpose of this register is to allow individual control of clocks,
reset-signals and interrupts to peripherals, and pin-muxing, and the LEDs and
switches.
