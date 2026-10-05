---
id: "dbgadapter-arm-fvp"
type: "concept"
domain: "debug"
title: "Debug adapter Arm-FVP: names, defaults and options"
summary: "Debug adapter Arm-FVP: the names csolution accepts, the defaults cbuild writes into cbuild-run.yml, and its options."
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@d5ffe88:registry/debug-adapters.yml"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/d5ffe88/registry/debug-adapters.yml"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "Apache-2.0"
mode: "V"
triggers: ["Arm-FVP"]
---

Names accepted in `debugger: name:` of a csolution project: `Arm-FVP`.

Launch and task template of the CMSIS Solution extension: `FVP.adapter.json`.

## Defaults

What cbuild writes into `*.cbuild-run.yml` when the project sets nothing:

```yaml
model: FVP_MPS2_Cortex-M3
gdbserver:
  active:
  port: 3333
```

## Options

What the CMSIS Solution extension offers for this adapter (the YAML node under `debugger:`):

| Section | Option | Node | Type | Default | Values |
|---|---|---|---|---|---|
| Model | Model | `model` | enum | FVP_MPS2_Cortex-M3 | `` (FVP_Corstone_SSE-300), `` (FVP_Corstone_SSE-300_Ethos-U55), `` (FVP_Corstone_SSE-300_Ethos-U65), `` (FVP_Corstone_SSE-310), `` (FVP_Corstone_SSE-310_Ethos-U65), `` (FVP_Corstone_SSE-315), `` (FVP_Corstone_SSE-320), `` (FVP_MPS2_Cortex-M0), `` (FVP_MPS2_Cortex-M0plus), `` (FVP_MPS2_Cortex-M3), `` (FVP_MPS2_Cortex-M4), `` (FVP_MPS2_Cortex-M7), `` (FVP_MPS2_Cortex-M23), `` (FVP_MPS2_Cortex-M33), `` (FVP_MPS2_Cortex-M35P), `` (FVP_MPS2_Cortex-M52), `` (FVP_MPS2_Cortex-M55), `` (FVP_MPS2_Cortex-M85) |
| Model | Config File | `config-file` | file |  |  |
| Model | Misc | `args` | string |  |  |

## Example

```yaml
debugger:
  name: Arm-FVP
```
