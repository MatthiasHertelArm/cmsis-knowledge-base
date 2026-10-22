---
id: "tbx-pyocd-debugger-device"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `device:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#device"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

pyOCD uses the `device` node to name the target in the current debug session. The node value is structured as
`[<vendor>::]<device>[:<pname>]`, where only the `<device>` part is used to name the target. The default value
is an empty string.

**Example:**

```yml
  device: Alif Semiconductor::AE722F80F55D5LS
```
