---
id: "frb-4-task-management-4-7-3-the-ready-state"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.7 Expanding the *Not Running* State / 4.7.3 The Ready State"
summary: "Part of: 4.7 Expanding the Not Running State"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-7-3-the-ready-state"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.7 Expanding the *Not Running* State_

Tasks that are in the *Not Running* state and are not *Blocked* or *Suspended*
are said to be in the *Ready* state. They can run, and are therefore 'ready' to
run, but are not currently in the *Running* state.
