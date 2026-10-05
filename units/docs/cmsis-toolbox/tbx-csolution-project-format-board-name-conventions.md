---
id: "tbx-csolution-project-format-board-name-conventions"
type: "concept"
domain: "project"
title: "CSolution Project Format: Name Conventions / `board:` Name Conventions"
summary: "Evaluation Boards define a device indirectly via the related BSP. The following syntax is used to specify a board: value in the .yml files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#board-name-conventions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Name Conventions_

Evaluation Boards define a device indirectly via the related BSP. The following syntax is used to specify a `board:`
value in the `*.yml` files.

```yml
[vendor::] board_name [:revision]
```

Element      |              | Description
:------------|:-------------|:---------------------
`vendor`     |   Optional   | Name of the board vendor-defined in `<boards><board>` element of the board support pack (BSP).
`Bname`      | **Required** | Board name (name attribute) as defined in the `<board>` element of the BSP.
`revision`   |   Optional   | Board revision (revision attribute) as defined in the `<board>` element of the BSP.

!!! Note
    When a `board:` is specified, the `device:` specification can be omitted, however it is possible to overwrite the device setting in the BSP with an explicit `device:` setting.

**Examples:**

```yml
board: Keil::MCB54110                             # The Keil MCB54110 board (with device NXP::LPC54114J256BD64)
board: LPCXpresso55S28                            # The LPCXpresso55S28 board
board: STMicroelectronics::NUCLEO-L476RG:Rev.C    # A board with revision specification
```
