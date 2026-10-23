---
id: "dbgadapter-st-link-arm-debugger"
type: "concept"
domain: "debug"
title: "Debug adapter ST-Link@Arm-Debugger: names, defaults and options"
summary: "Debug adapter ST-Link@Arm-Debugger (also ST-Link@armdbg): the names csolution accepts, the defaults cbuild writes into cbuild-run.yml, and its options."
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@2692b50:registry/debug-adapters.yml"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/2692b50/registry/debug-adapters.yml"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "Apache-2.0"
mode: "V"
triggers: ["ST-Link@Arm-Debugger", "ST-Link@armdbg"]
---

Names accepted in `debugger: name:` of a csolution project: `ST-Link@Arm-Debugger`, `ST-Link@armdbg`.

Launch and task template of the CMSIS Solution extension: `STLink-Arm-Debugger.adapter.json`.

## Defaults

What cbuild writes into `*.cbuild-run.yml` when the project sets nothing:

```yaml
protocol-armdbg: auto
clock-armdbg: auto
```

## Options

What the CMSIS Solution extension offers for this adapter (the YAML node under `debugger:`):

| Section | Option | Node | Type | Default | Values |
|---|---|---|---|---|---|
| Debug Interface | Clock | `clock-armdbg` | enum | auto | `auto` (auto), `` (50MHz), `` (33MHz), `` (25MHz), `` (20MHz), `` (10MHz), `` (5MHz), `` (2MHz), `` (1MHz), `` (500kHz), `` (200kHz), `` (100kHz), `` (50kHz), `` (20kHz), `` (10kHz), `` (5kHz) |
| Debug Interface | Protocol | `protocol-armdbg` | enum | auto | `auto` (auto), `JTAG` (JTAG), `SWD` (SWD) |

## Example

```yaml
debugger:
  name: ST-Link@armdbg
```
