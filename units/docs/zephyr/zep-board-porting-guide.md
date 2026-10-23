---
id: "zep-board-porting-guide"
type: "concept"
domain: "bring-up"
title: "Board Porting Guide"
summary: "To add Zephyr support for a new board, you at least need a board directory with various files in it. Files in the board directory inherit support for at least one SoC and all of its features."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/board_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/board_porting.rst"
license: "Apache-2.0"
mode: "V"
---

To add Zephyr support for a new `board`, you at least need a *board
directory* with various files in it. Files in the board directory inherit
support for at least one SoC and all of its features. Therefore, Zephyr must
support your `SoC` as well.
