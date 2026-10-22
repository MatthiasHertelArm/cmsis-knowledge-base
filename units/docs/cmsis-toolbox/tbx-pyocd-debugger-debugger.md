---
id: "tbx-pyocd-debugger-debugger"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `debugger:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#debugger"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains the user's debugger configuration settings. The available options are described in detail in the
CSolution Project Format section [Debugger Configuration: pyOCD](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-Input-Format.md#debugger-for-pyocd)
and pyOCD Debugger [Extended Options](#extended-options).

**Example:**

```yml
  debugger:
    name: CMSIS-DAP@pyOCD
    protocol: swd
    clock: 10000000
    start-pname: M55_HP
    connect: attach
    reset:
      - type: system
        pname: M55_HP
      - type: core
        pname: M55_HE
    gdbserver:
      - port: 3333
        pname: M55_HP
      - port: 3334
        pname: M55_HE
    stdio:
      - mode: console
        pname: M55_HE
        port: 4445
      - mode: monitor
        pname: M55_HP
        port: 4444
```
