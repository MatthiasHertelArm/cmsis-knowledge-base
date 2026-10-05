---
id: "x-cmsis-debugger-setup-4"
type: "pattern"
domain: "project"
title: "Diagnose a silent UART"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
---

**A silent UART**: halt, and read the UART's status, control and baud-rate registers with `read_peripheral_register`. A status register at its reset value means the peripheral is alive and its configuration is wrong; all zeros, or the same value in every register, means its clock was never enabled.
