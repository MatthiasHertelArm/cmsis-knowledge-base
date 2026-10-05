---
id: "zepb-lpcxpresso55s69-dual-core-samples"
type: "concept"
domain: "bring-up"
title: "lpcxpresso55s69: Dual Core samples"
summary: "+--------+------------------+----------------------------+ | Memory | Address[Size] | Comment | +========+==================+============================+ | CPU0 | 0x00000000[630K] | CPU0, can access all flash | +--------+------------------+----------------------------+ | CPU1 | 0x00030000[96k] | CPU1, has no MPU | +--------+------------------+----------------------------+"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/lpcxpresso55s69/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#dual-core-samples"
license: "Apache-2.0"
mode: "V"
---

+--------+------------------+----------------------------+
| Memory | Address[Size]    | Comment                    |
+========+==================+============================+
| CPU0   | 0x00000000[630K] | CPU0, can access all flash |
+--------+------------------+----------------------------+
| CPU1   | 0x00030000[96k]  | CPU1, has no MPU           |
+--------+------------------+----------------------------+

+-------+------------------+-----------------------+
| RAM   | Address[Size]    | Comment               |
+=======+==================+=======================+
| sram0 | 0x20000000[64k]  | CPU0 memory           |
+-------+------------------+-----------------------+
| sram3 | 0x20030000[64k]  | CPU1 memory           |
+-------+------------------+-----------------------+
| sram4 | 0x20040000[16k]  | Mailbox/shared memory |
+-------+------------------+-----------------------+


### System Clock


The LPC55S69 SoC is configured to use PLL1 clocked from the external 16MHz
crystal, running at 144MHz as a source for the system clock. When the flash
controller is enabled, the core clock will be reduced to 96MHz. The application
may reconfigure clocks after initialization, provided that the core clock is
always set to 96MHz when flash programming operations are performed.


### Serial Port


The LPC55S69 SoC has 8 FLEXCOMM interfaces for serial communication.  One is
configured as USART for the console and the remaining are not used.
