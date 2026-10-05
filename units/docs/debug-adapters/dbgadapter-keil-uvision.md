---
id: "dbgadapter-keil-uvision"
type: "concept"
domain: "debug"
title: "Debug adapter Keil uVision: names, defaults and options"
summary: "Debug adapter Keil uVision: the names csolution accepts, the defaults cbuild writes into cbuild-run.yml, and its options."
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@d5ffe88:registry/debug-adapters.yml"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/d5ffe88/registry/debug-adapters.yml"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "Apache-2.0"
mode: "V"
triggers: ["Keil uVision"]
---

Names accepted in `debugger: name:` of a csolution project: `Keil uVision`.

Launch and task template of the CMSIS Solution extension: `uVision.adapter.json`.

## Defaults

What cbuild writes into `*.cbuild-run.yml` when the project sets nothing:

```yaml
uv4: ${env:LOCALAPPDATA}/Keil_v5/UV4/UV4.exe
```

## Options

What the CMSIS Solution extension offers for this adapter (the YAML node under `debugger:`):

| Section | Option | Node | Type | Default | Values |
|---|---|---|---|---|---|
| Debug Interface | uVision | `uv4` | file | ${env:LOCALAPPDATA}/Keil_v5/UV4/UV4.exe |  |

## Example

```yaml
debugger:
  name: Keil uVision
```
