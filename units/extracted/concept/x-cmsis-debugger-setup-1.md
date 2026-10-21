---
id: "x-cmsis-debugger-setup-1"
type: "concept"
domain: "project"
title: "CMSIS debug adapter name for each probe"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
license: "Apache-2.0"
---

| Probe | Adapter name |
|---|---|
| CMSIS-DAP, DAPLink, on-board CMSIS-DAP | `CMSIS-DAP@pyOCD` |
| ST-Link, on-board ST-Link | `ST-Link@pyOCD` |
| ULINKplus | `ULINKplus@pyOCD` |
| MCU-Link, Nu-Link, KitProg3, PICkit, Raspberry Pi Debug Probe | `MCU-Link@pyOCD`, `Nu-Link@pyOCD`, `KitProg3@pyOCD`, `PICkit@pyOCD`, `RPiDebugProbe@pyOCD` |
| SEGGER J-Link | `J-Link Server` |

Use a name exactly as `csolution list debuggers` prints it.
