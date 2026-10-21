---
id: "x-debugger-troubleshooting-3"
type: "troubleshooting"
domain: "debug"
title: "Debug connection failures in increasing severity"
status: "draft"
symptoms: ["AP[n]: Skipped. Not an AHB-AP", "AP[n]: Skipped. Could not read AHB ROM register", "Could not find core in Coresight setup", "Failed to power up DAP"]
extracted_from: "proc-debugger-troubleshooting"
source: "debugger-troubleshooting/SKILL.md"
license: "Apache-2.0"
---

| Message | Meaning | Action |
|---|---|---|
| `AP[n]: Skipped. Not an AHB-AP` | The AP type is not declared (SoC-600 needs an explicit AP map) | The device pack's debug description, or for J-Link a script that declares the map; see section 8 |
| `AP[n]: Skipped. Could not read AHB ROM register` | The AP is typed correctly but reads fail: the bus hangs, or debug power-up is missing | Retry once; then power-cycle |
| `Could not find core in Coresight setup` | Consequence of the row above | As above |
| `Failed to power up DAP` | The SoC's debug power domain is down | Power-cycle the board |

`Failed to power up DAP` is not recoverable in software. The debug port answers while the domain behind it is off, so connecting under reset or at a lower clock fails too. Ask the user to unplug and replug power; the reset button is often not enough.

A hung bus transaction can take the debug port down with it. If the failure started right after the firmware stalled a bus master (a DMA or an NPU waiting for an external memory), suspect that, not the probe. `Could not read AHB ROM register` that recovers on a second or third `cmsis_action load_and_debug` is the signature.
