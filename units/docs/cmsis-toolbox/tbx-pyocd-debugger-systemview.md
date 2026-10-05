---
id: "tbx-pyocd-debugger-systemview"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `systemview:`"
summary: "The systemview: node configures the .SVDat file capturing for SEGGER SystemView tool for analyzing the runtime behavior of embedded systems."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#systemview"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

The `systemview:` node configures the *.SVDat file capturing for [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) tool for analyzing the runtime behavior of embedded systems.

`systemview:`                                       |              | Description
:---------------------------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `file:`                          |   Optional   | SystemView capture file. Default: `./out/<solution-name>+<target-type>.SVDat` (derived from [`*.cbuild-run.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-CBuild-Format.md#run-and-debug-management)).
&nbsp;&nbsp;&nbsp; `auto-start:`                    |   Optional   | Send SystemView start command automatically: `true` (default), `false`.
&nbsp;&nbsp;&nbsp; `auto-stop:`                     |   Optional   | Send SystemView stop command automatically: `true` (default), `false`.

**Examples:**

Configure SystemView capture on channel 1:

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  protocol: swd
  rtt:
    - pname: Core0
      channel:
        - number: 1
          mode: systemview
  systemview:                      # explicit SystemView output file
    file: ./out/MyFile.SVDat
```
