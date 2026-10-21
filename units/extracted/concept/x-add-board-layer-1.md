---
id: "x-add-board-layer-1"
type: "concept"
domain: "project"
title: "A DFP with a configuration generator may ship no Device:Startup component"
status: "draft"
extracted_from: "proc-add-board-layer"
source: "add-board-layer/SKILL.md"
license: "Apache-2.0"
---

**Does the DFP ship startup, or a generator?** Check both: `grep -c 'Cgroup="Startup"' <DFP>.pdsc` and `grep -o '<generator id="[^"]*"' <DFP>.pdsc`. A DFP with a `<generator>` (STM32CubeMX, MCUXpresso Config Tools, Infineon Device Configurator, Microchip MCC, …) may ship **no classic `Device:Startup` component at all** — startup, `SystemInit`, clock and pin configuration exist only as generator output (components carrying `generator="<id>"`).
