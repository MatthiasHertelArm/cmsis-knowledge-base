---
id: "tbx-pyocd-debugger-load-setup"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `load-setup:`"
summary: "Configures the debug sequences executed during the load command of pyOCD."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#load-setup"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

Configures the debug sequences executed during the `load` command of pyOCD.

`load-setup:`                     |              | Description
:---------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `halt:`        |   Optional   | Halt core(s) before load: `on` (default), `off`.
&nbsp;&nbsp;&nbsp; `pre-reset:`   |   Optional   | Reset type before loading: `off`, `hardware`, `system`, `core`. Default: specified in DFP or defined with [`reset`](#reset).
&nbsp;&nbsp;&nbsp; `post-reset:`  |   Optional   | Reset type after loading: `off`, `hardware` (default), `system`, `core`.

**Examples:**

```yml
debugger:
  name: CMSIS-DAP@pyOCD     # default connect, halt and reset behavior
```

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  connect: under-reset      # connect under hardware reset
  reset:
    - type: system          # use system reset
  load-setup:
    halt: on                # halt core(s) before load
    post-reset: hardware    # use hardware reset after load
```

```yml
debugger:
  name: CMSIS-DAP@pyOCD
  connect: pre-reset        # apply hardware reset before connect
  reset:
    - pname: Core0          # for Core0
      type: hardware        # use hardware reset
    - pname: Core1          # for Core1
      type: system          # use system reset
  load-setup:
    pre-reset: system       # use system reset before load
    post-reset: off         # no reset after load
```
