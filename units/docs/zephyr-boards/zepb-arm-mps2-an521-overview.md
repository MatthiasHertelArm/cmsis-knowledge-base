---
id: "zepb-arm-mps2-an521-overview"
type: "concept"
domain: "bring-up"
title: "ARM MPS2+ AN521: Overview"
summary: "The mps2/an521 board configuration is used by Zephyr applications that run on the MPS2+ AN521 board. It provides support for the MPS2+ AN521 ARM Cortex-M33 CPU and the following devices:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/arm/mps2/doc/mps2_an521.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The mps2/an521 board configuration is used by Zephyr applications that run
on the MPS2+ AN521 board. It provides support for the MPS2+ AN521 ARM Cortex-M33
CPU and the following devices:

- Nested Vectored Interrupt Controller (NVIC)
- System Tick System Clock (SYSTICK)
- Cortex-M System Design Kit GPIO
- Cortex-M System Design Kit UART

In addition to enabling actual hardware usage, this board configuration can
also use QEMU to emulate the AN521 platform running on the MPS2+.

More information about the board can be found at the MPS2 FPGA Website.


**Note:** This board configuration makes no claims about its suitability for use with actual MPS2 hardware systems using AN521, or any other hardware system. It has been tested on actual hardware, but its primary purpose is for use with QEMU and unit tests for the ARM Cortex-M33.


### Zephyr board options


The MPS2+ AN521 is a dual core SoC with Cortex-M33 architecture on both cores
(CPU0 and CPU1). Zephyr provides support for building firmware
images for both CPU0 and CPU1. For CPU0 supporting ARM Security Extensions
both Secure and Non-Secure firmware images may be built.

The BOARD options are summarized below:

+----------------------+-------------------------------------------------------+
| BOARD                | Description                                           |
+======================+=======================================================+
| mps2/an521/cpu0      | For building Secure (or Secure-only) firmware on CPU0 |
+----------------------+-------------------------------------------------------+
| mps2/an521/cpu0/ns   | For building Non-Secure firmware for CPU0             |
+----------------------+-------------------------------------------------------+
| mps2/an521/cpu1      | For building firmware on CPU1                         |
+----------------------+-------------------------------------------------------+


### Memory Partitioning


The AN521 has 4MB allocated for code space, and 4MB for SRAM. These memory
regions are shared across both cores, and are aliased in both secure and
non-secure regions, where the secure memory alias has an offset of
0x10000000 relative to non-secure.

The following memory map and partitioning schemes are used by default, where
the offset value is the offset from the base of the 4MB code or SRAM block,
ignoring the S/NS alias difference.

+-------------------------+-----+----------------+----------------+------------+
| Board                   | CPU | Code (Offset)  | SRAM (Offset)  | S/NS Alias |
+=========================+=====+================+================+============+
| mps2/an521/cpu0         | 0   | 4MB (0)        | 4MB (0)        | S          |
+-------------------------+-----+----------------+----------------+------------+
| mps2/an521/cpu0/ns      | 0   | 512KB (1MB)    | 512KB (1MB)    | NS         |
+-------------------------+-----+----------------+----------------+------------+
| mps2/an521/cpu1         | 1   | 468KB (3628KB) | 512KB (1.5MB)  | NS         |
+-------------------------+-----+----------------+----------------+------------+

The `mps2/an521/cpu0/ns` board target is intended to be used with TF-M, with the
Zephyr memory map matching the AN521 memory map defined upstream in TF-M. TF-M
boots the secure processing environment before initialising Zephyr in the
non-secure processing environment. The non-secure Zephyr image is offset to
make room for the secure bootloader, and the secure firmware (TF-M), resulting
in a starting address of 0x00100000. SRAM begins with a 1MB offset at
0x28100000.

The `mps2/an521/cpu1` board target is setup for the second core on the
AN521, using the final 468KB code memory in the 4MB code block. This value
is chosen to maintain compatibility with TF-M, which marks that final 468KB
code region as `Unused`. Code memory thus starts with an offset of
3628KB (address 0x0038B000), and sram starts with an offset of 1.5MB
(address 0x28180000).

This memory map enables the two alternative board targets to be used together
if required, at the cost of reducing the amount of code memory available on
the second core to the worst-case scenario from TF-M.

When using one of the alternative board targets (`mps2/an521/cpu0/ns` or
`mps2/an521/cpu1`), care needs to be taken with the amount of code or
SRAM memory used on the primary board target (`mps2/an521`) since there is
some overlap in the memory maps.
