---
id: "x-cmsis-debugger-setup-3"
type: "concept"
domain: "project"
title: "At -Og a readback can show the old value right after a store"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
---

**At `-Og` the line table can be one volatile store early.** Right after stepping past a store, a readback may still show the old value. Let the code run on and read again before you suspect the hardware.
