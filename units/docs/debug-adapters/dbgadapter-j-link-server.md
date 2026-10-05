---
id: "dbgadapter-j-link-server"
type: "concept"
domain: "debug"
title: "Debug adapter J-Link Server: names, defaults and options"
summary: "Debug adapter J-Link Server (also J-Link, JLink Server): the names csolution accepts, the defaults cbuild writes into cbuild-run.yml, and its options."
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@d5ffe88:registry/debug-adapters.yml"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/d5ffe88/registry/debug-adapters.yml"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "Apache-2.0"
mode: "V"
triggers: ["J-Link Server", "J-Link", "JLink Server"]
---

Names accepted in `debugger: name:` of a csolution project: `J-Link Server`, `J-Link`, `JLink Server`.

Launch and task template of the CMSIS Solution extension: `JLink.adapter.json`.

## Defaults

What cbuild writes into `*.cbuild-run.yml` when the project sets nothing:

```yaml
gdbserver:
  active:
  port: 3333
telnet:
  active:
  port: 4444
  mode: false
protocol: swd
clock: 4000000
```

## Options

What the CMSIS Solution extension offers for this adapter (the YAML node under `debugger:`):

| Section | Option | Node | Type | Default | Values |
|---|---|---|---|---|---|
| Debug Interface | Clock (kHz) | `clock` | number | 4000 | 10 to 50000 |
| Debug Interface | Protocol | `protocol` | enum | swd | `jtag` (JTAG), `swd` (SWD) |
| Telnet | Telnet Mode | `telnet.mode` | enum | monitor | `server` (Telnet Server), `console` (Debug Console), `monitor` (Serial Monitor), `off` (Disabled) |

## Example

```yaml
debugger:
  name: J-Link
```
