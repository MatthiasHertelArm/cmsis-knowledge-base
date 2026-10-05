---
id: "avh-cmsis-support-software-layers"
type: "concept"
domain: "test"
title: "CMSIS Support: Software Layers"
summary: "The AVHFVP pack provides board support layers for Corstone FVP platforms in the board/ folder. Each board layer includes hardware-specific configurations, drivers, and setup for running applications on FVP simulation models."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/avh_fvp_cmsis.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/avh_fvp_cmsis.md#software-layers"
license: "Apache-2.0"
mode: "V"
---

The AVH_FVP pack provides board support layers for Corstone FVP platforms in the `board/` folder. Each board layer includes hardware-specific configurations, drivers, and setup for running applications on FVP simulation models.

| Folder                 | Description |
|:-----------------------|:------------|
| `./board/Corstone-300` | Board layer for Corstone-300 FVP with optional Ethos-U55/U65 |
| `./board/Corstone-310` | Board layer for Corstone-310 FVP with optional Ethos-U55/U65 |
| `./board/Corstone-315` | Board layer for Corstone-315 FVP with optional Ethos-U65 |
| `./board/Corstone-320` | Board layer for Corstone-320 FVP with optional Ethos-U85 |

Each folder contains a **README** with implementation details and multiple **CSolution layer files** (`*.clayer.yml`) that configure different hardware variants. The postfix in the `*.clayer.yml` filename determines the Ethos-U NPU configuration:

| Layer File | NPU Configuration | Description |
|:-----------|:------------------|:------------|
| `Board.clayer.yml` | None | Cortex-M system only, no Ethos-U NPU |
| `Board-U55.clayer.yml` | Ethos-U55 | Cortex-M system + Ethos-U55 NPU (256 MACs) |
| `Board-U65.clayer.yml` | Ethos-U65 | Cortex-M system + Ethos-U65 NPU |
| `Board-U85.clayer.yml` | Ethos-U85 | Cortex-M system + Ethos-U85 NPU |

Refer to [CMSIS-Toolbox - Software Layers](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#software-layers) for more information on using layers in projects.
