---
id: "zepb-mimxrt1050-evk-board-targets"
type: "concept"
domain: "bring-up"
title: "mimxrt1050_evk: Board Targets"
summary: "This board has two variants that can be targeted, depending on which flash to set as zephyr,flash:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/mimxrt1050_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1050_evk/doc/index.html#board-targets"
license: "Apache-2.0"
mode: "V"
---

This board has two variants that can be targeted,
depending on which flash to set as `zephyr,flash`:

* `mimxrt1050_evk/mimxrt1052/hyperflash` is the default variant for the out of box
  setup of the board using hyperflash.
* `mimxrt1050_evk/mimxrt1052/qspi` is for a board that has been reworked to use the
  qspi flash instead of hyperflash.
