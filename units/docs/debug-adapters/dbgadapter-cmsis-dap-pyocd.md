---
id: "dbgadapter-cmsis-dap-pyocd"
type: "concept"
domain: "debug"
title: "Debug adapter CMSIS-DAP@pyOCD: names, defaults and options"
summary: "Debug adapter CMSIS-DAP@pyOCD (also CMSIS-DAP, DAP-Link): the names csolution accepts, the defaults cbuild writes into cbuild-run.yml, and its options."
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@2692b50:registry/debug-adapters.yml"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/2692b50/registry/debug-adapters.yml"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "Apache-2.0"
mode: "V"
triggers: ["CMSIS-DAP@pyOCD", "CMSIS-DAP", "DAP-Link"]
---

Names accepted in `debugger: name:` of a csolution project: `CMSIS-DAP@pyOCD`, `CMSIS-DAP`, `DAP-Link`.

Launch and task template of the CMSIS Solution extension: `CMSIS-DAP-pyOCD.adapter.json`.

## Defaults

What cbuild writes into `*.cbuild-run.yml` when the project sets nothing:

```yaml
gdbserver:
  active:
  port: 3333
telnet:
  port: 4444
protocol: swd
clock: 10000000
```

## Options

What the CMSIS Solution extension offers for this adapter (the YAML node under `debugger:`):

| Section | Option | Node | Type | Default | Values |
|---|---|---|---|---|---|
| Debug Interface | Clock (kHz) | `clock` | number | 10000 | 10 to 30000 |
| Debug Interface | Protocol | `protocol` | enum | swd | `jtag` (JTAG), `swd` (SWD) |
| Telnet | Telnet Mode | `telnet.mode` | enum | monitor | `server` (Telnet Server), `console` (Debug Console), `monitor` (Serial Monitor), `file` (Text File), `off` (Disabled) |

## Example

```yaml
debugger:
  name: CMSIS-DAP
```
