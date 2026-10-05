---
id: "tbx-pack-creation-board-support-pack-bsp-content"
type: "concept"
domain: "pack"
title: "Pack Creation: Board Support Pack (BSP) Content"
summary: "A BSP extends the DFP with information that relates to boards:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#board-support-pack-bsp-content"
license: "Apache-2.0"
mode: "V"
---

A BSP extends the DFP with information that relates to boards:

- The Blinky example verifies hardware and tool setup and provides the bootstrap for IDE workflows.
- With CMSIS-Driver VIO, simple I/Os such as LEDs and push buttons are controlled, and test automation is supported.
- Project templates configured for board peripherals.
- A layer can provide a pre-configured driver set for reference applications that interface to middleware.
- Board memory with download algorithms extend the information for programmers and linker scripts.

!!! Tip
    The Blinky example of the [BSP-Pack-HandsOn](https://github.com/Open-CMSIS-Pack/BSP-Pack-HandsOn) is generic. All it requires to adapt the `./Driver/vio*.c` to the actual hardware of the board.

| Must have         | Strongly recommended                 | Optional                              |
|:------------------|:-------------------------------------|:--------------------------------------|
| [Board description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html) | [`Overview.md` file](https://github.com/Open-CMSIS-Pack/BSP-Pack-HandsOn/blob/main/Docs/Overview.md)                                                    | Additional examples                   |
|                                                                                                           | [Blinky example](https://github.com/Open-CMSIS-Pack/BSP-Pack-HandsOn/tree/main/Examples/Blinky)                                                         | [Layers](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#software-layers) for Reference Applications     |
|                                                                                                           | [CMSIS-Driver VIO](https://arm-software.github.io/CMSIS_6/latest/Driver/group__vio__interface__gr.html) for LED and button                              | HAL drivers for board peripherals     |
|                                                                                                           | [Board features](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_feature)                            | Project templates (board specific)    |
|                                                                                                           | [Download algorithms for on-board memory](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_algorithm) |                                       |
|  | [Pack Requirements](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html) |                                                                                                                                           |

!!! Note
    The content of a DFP and BSP may be provided in a single pack.

**Hands-on Tutorial:**

- [BSP-Pack-HandsOn](https://github.com/Open-CMSIS-Pack/BSP-Pack-HandsOn) explains the structure and creation of a Board Support Pack (BSP).

**Pack Example:**

- [NUCLEO-F746ZG_BSP](https://github.com/Open-CMSIS-Pack/ST_NUCLEO-F746ZG_BSP) available on [keil.arm.com/packs/nucleo-f746zg_bsp-keil](https://www.keil.arm.com/packs/nucleo-f746zg_bsp-keil/overview).
