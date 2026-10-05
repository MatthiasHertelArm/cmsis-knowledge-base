---
id: "tbx-pyocd-debugger-gdbserver"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Extended Options / `gdbserver:`"
summary: "gdbserver: | | Content :------------------------------|:-------------|:------------------------------------ - port: | Required | Set TCP/IP port number of GDB Server (default: 3333, 3334, ... incremented for each processor). &nbsp;&nbsp;&nbsp; pname: | Optional | Identifies the processor (not required for single core system)."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#gdbserver"
license: "Apache-2.0"
mode: "V"
---

_Part of: Extended Options_

`gdbserver:`                   |              | Content
:------------------------------|:-------------|:------------------------------------
`- port:`                      | **Required** | Set TCP/IP port number of GDB Server (default: 3333, 3334, ... incremented for each processor).
&nbsp;&nbsp;&nbsp; `pname:`    |   Optional   | Identifies the processor (not required for single core system).

!!! Note
    - When no `gdbserver` node is applied, the default mechanism of incrementing port number starting with `3333` is used.
