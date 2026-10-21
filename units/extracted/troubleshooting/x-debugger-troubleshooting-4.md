---
id: "x-debugger-troubleshooting-4"
type: "troubleshooting"
domain: "debug"
title: "Could not read memory at an external-memory window"
status: "draft"
symptoms: ["Could not read memory"]
extracted_from: "proc-debugger-troubleshooting"
source: "debugger-troubleshooting/SKILL.md"
license: "Apache-2.0"
---

For XIP windows (OSPI, QSPI, HyperRAM, PSRAM) a debugger read fails until the firmware has configured the controller. Beyond that:
**Writes succeed while reads fail**: the controller is up but read capture timing is wrong. A write is posted and needs no reply; a read has to sample the device's read strobe. Check RXDS or DQS delay, wait cycles and the DDR drive edge in the board configuration against the vendor's values for that exact part.
A `read_memory` of such a window can hang the bus, after which the debug connection itself starts failing (section 3). If `check_target_connection` degrades right after you read an XIP address, that read is the cause.
