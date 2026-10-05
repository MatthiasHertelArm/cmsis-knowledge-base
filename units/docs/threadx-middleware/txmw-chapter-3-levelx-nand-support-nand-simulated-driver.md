---
id: "txmw-chapter-3-levelx-nand-support-nand-simulated-driver"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: NAND Simulated Driver"
summary: "LevelX provides a simulated NAND flash driver that simply uses RAM to simulate the operation of a NAND flash part."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#nand-simulated-driver"
license: "MIT"
mode: "V"
---

LevelX provides a simulated NAND flash driver that simply uses RAM to simulate the operation of a NAND flash part. By default, the NAND simulated driver provides 8 NAND flash blocks with 16 pages per block and 2048 bytes per page.

The simulated NAND flash driver initialization function is ***lx_nand_flash_simulator_initialize*** and is defined in ***lx_nand_flash_simulator.c***. This driver also provides a good template for writing specific NAND flash drivers.
