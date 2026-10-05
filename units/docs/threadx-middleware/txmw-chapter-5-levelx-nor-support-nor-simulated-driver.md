---
id: "txmw-chapter-5-levelx-nor-support-nor-simulated-driver"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: NOR Simulated Driver"
summary: "LevelX provides a simulated NOR flash driver that simply uses RAM to simulate the operation of a NOR flash part. By default, the NOR simulated driver provides 8 NOR flash blocks with 16 512-byte sectors per block."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#nor-simulated-driver"
license: "MIT"
mode: "V"
---

LevelX provides a simulated NOR flash driver that simply uses RAM to simulate the operation of a NOR flash part. By default, the NOR simulated driver provides 8 NOR flash blocks with 16 512-byte sectors per block.

The simulated NOR flash driver initialization function is ***lx_nor_flash_simulator_initialize*** and is defined in ***lx_nor_flash_simulator.c***. This driver also provides a good template for writing specific NOR flash drivers.
