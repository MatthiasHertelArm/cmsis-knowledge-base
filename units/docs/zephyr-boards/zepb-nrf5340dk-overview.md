---
id: "zepb-nrf5340dk-overview"
type: "concept"
domain: "bring-up"
title: "nrf5340dk: Overview"
summary: "The nRF5340 DK (PCA10095) is a single-board development kit for evaluation and development on the Nordic nRF5340 System-on-Chip (SoC)."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nordic/nrf5340dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The nRF5340 DK (PCA10095) is a single-board development kit for evaluation
and development on the Nordic nRF5340 System-on-Chip (SoC).

The nRF5340 is a dual-core SoC based on the Arm® Cortex®-M33 architecture, with:

* a full-featured Arm Cortex-M33F core with DSP instructions, FPU, and
  Armv8-M Security Extension, running at up to 128 MHz, referred to as
  the **application core**
* a secondary Arm Cortex-M33 core, with a reduced feature set, running at
  a fixed 64 MHz, referred to as the **network core**.

The `nrf5340dk/nrf5340/cpuapp` build target provides support for the application
core on the nRF5340 SoC. The `nrf5340dk/nrf5340/cpunet` build target provides
support for the network core on the nRF5340 SoC.

More information about the board can be found at the
nRF5340 DK website.
The nRF5340 DK Product Specification
contains the processor's information and the datasheet.
