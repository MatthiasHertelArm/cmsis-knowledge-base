---
id: "zepb-mimxrt1060-evk-board-revisions-and-targets"
type: "concept"
domain: "bring-up"
title: "mimxrt1060_evk: Board Revisions and Targets"
summary: "There are three revisions of this board."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/nxp/mimxrt1060_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1060_evk/doc/index.html#board-revisions-and-targets"
license: "Apache-2.0"
mode: "V"
---

There are three revisions of this board.

Rev A:

* Initial version

Rev B:

* adds the M.2 connector for Wi-Fi/BLE
* adds audio expansion connector J23
* USER LED1 changed to GPIO1 pin 8

Rev C:

* Replaces audio codec WM8960(EOL) to WM8962
* Replaces 32.768 KHz oscillator from ASH7K-32.768KHz-T(EOL)to ASH7KW-32.768KHZ-L-T
* Replaces motion sensor from FXOS8700CQ(EOL) to FXLS8974CFR3
* Re-assigns Bluetooth Audio PCM with dedicated I2S2
* Re-assigns Bluetooth interface UART_CTS, UART_RTS to hardware PIN

This board has two variants that can be targeted,
depending on which flash to set as `zephyr,flash`:

* `mimxrt1060_evk/mimxrt1062/qspi` is the default variant for the out of box
  setup of the board using the qspi flash.
* `mimxrt1060_evk/mimxrt1062/hyperflash` is for a board that has been reworked to use the
  hyperflash instead of the qspi flash.
* This board also has two revisions, the EVKA and EVKB. EVKA is the default target for this board.
  To target EVKB, the board target string would become `mimxrt1060_evk@B//qspi`, for example.
