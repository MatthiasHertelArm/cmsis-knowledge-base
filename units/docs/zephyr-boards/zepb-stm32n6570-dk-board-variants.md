---
id: "zepb-stm32n6570-dk-board-variants"
type: "concept"
domain: "bring-up"
title: "stm32n6570_dk: Board variants"
summary: "Three variants are available with STM32N6570_DK:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/stm32n6570_dk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/stm32n6570_dk/doc/index.html#board-variants"
license: "Apache-2.0"
mode: "V"
---

Three variants are available with STM32N6570_DK:

- Main application (default variant). Available as a chainloaded application which should
  be loaded by a bootloader, it has access to the whole AXISRAM1 and AXISRAM2 regions.
  It is expected to be built using `--sysbuild` option exclusively.
- `fsbl`: First Stage Boot Loader (FSBL) which is available as an application loaded by the
  Boot ROM and flashed using ST-Link. This is typically a bootloader image. It runs
  in RAM LOAD mode on second half of AXISRAM2. 511K are available for the whole image.
- `sb`: First Stage Boot Loader - Serial Boot. Equivalent to the FSBL image, but could be
  loaded using USB and doesn't require switching the bootpins. This is the most practical
  for developments steps.
