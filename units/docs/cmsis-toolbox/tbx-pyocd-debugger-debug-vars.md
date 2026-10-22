---
id: "tbx-pyocd-debugger-debug-vars"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `debug-vars:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#debug-vars"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains the definition and default values for debug sequence variables. The default values can be overridden by corresponding key-value pairs under the `device-settings:` node under [`debugger:`](#debugger).

`debug-vars:`                                             |              | Content
:---------------------------------------------------------|--------------|:------------------------------------
    `vars:`                                |   Optional   | Initial values for variables used in [`debug-sequences:`](#debug-sequences).

**Example:**

```yml
  debug-vars:
    vars: |
      // Default values for variables in debug sequences. Can be configured with a *.dbgconf file in the user project
      __var SWO_Pin               = 0;                    // Serial Wire Output pin: 0 = PIO0_10, 1 = PIO0_8
      __var Dbg_CR                = 0x00000000;           // DBG_CR
      __var BootTime              = 10000;                // 10 milliseconds
```
