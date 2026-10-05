---
id: "tbx-csolution-project-format-keil-uvision"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration / Keil uVision"
summary: "This section lists options that are specific for the uVision Debugger."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#keil-uvision"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger Configuration_

This section lists options that are specific for the uVision Debugger.

#### `debugger:` for Keil uVision

debugger:                  |              | Description
:--------------------------|:-------------|:-----------------------------------------------
    `name:` | **Required** | Identifies the debug adapter with `Keil uVision`.
    `uv4:`  |   Optional   | Path to the uVision executable; default: `C:/Keil_v5/UV4/UV4.exe`.

```yml
debugger:
  name: Keil uVision
```
