---
id: "x-cmsis-debugger-setup-5"
type: "pattern"
domain: "project"
title: "A silent UART"
status: "draft"
extracted_from: "proc-cmsis-debugger-setup"
source: "cmsis-debugger-setup/SKILL.md"
license: "Apache-2.0"
---

Halt, and read the UART's status, control and baud-rate registers with `read_peripheral_register`. A status register at its reset value means the peripheral is alive and its configuration is wrong; all zeros, or the same value in every register, means its clock was never enabled.
