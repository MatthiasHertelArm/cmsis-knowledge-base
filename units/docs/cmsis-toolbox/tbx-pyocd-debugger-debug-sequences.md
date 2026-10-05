---
id: "tbx-pyocd-debugger-debug-sequences"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `debug-sequences:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#debug-sequences"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains [debug sequences](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_sequence)
from the DFP for the target. A sequence with no `blocks:` disables the default sequence; sequence names can override
default sequences from the DFP.

`debug-sequences:`                                        |              | Content
:---------------------------------------------------------|--------------|:------------------------------------
`- name:`                                                 | **Required** | Name of the sequence.
    `info:`                                |   Optional   | Descriptive text to display for example for error diagnostics.
    `blocks:`                              |   Optional   | A list of command blocks in order of execution.
    `pname:`                               |   Optional   | Executes sequence only for a specific processor; default is for all processors.

`blocks:`                                                 |              | Content
:---------------------------------------------------------|--------------|:------------------------------------
`- info:`                                                 |   Optional   | Descriptive text to display for example for error diagnostics.
    `blocks:`                              |   Optional   | A list of command blocks in the order of execution.
    `execute:`                             |   Optional   | Commands for execution.
    `atomic:`                              |   Optional   | Atomic execution of commands; cannot be used with `blocks:`.
    `if:`                                  |   Optional   | Only executed when expression is true.
    `while:`                               |   Optional   | Executed in loop until while expression is true.
    `timeout:`                             |   Optional   | Timeout value (integer) in milliseconds for while loop.

**Example:**

```yml
  debug-sequences:
    - name: DisableWarmResetHandshake
      blocks:
        - execute: |
            Write32(0x1A601024, 0);
      pname: M55_HE
    - name: DisableWarmResetHandshake
      blocks:
        - execute: |
            Write32(0x1A600024, 0);
      pname: M55_HP
    - name: DebugDeviceUnlock
      blocks:
        - execute: |
            DAP_Delay(500000);  // Delay for 500ms
    - name: ResetSystem
      blocks:
        - execute: |
            Sequence("DisableWarmResetHandshake");
        - execute: |
            // System Control Space (SCS) offset as defined in Armv6-M/Armv7-M.

            __var SCS_Addr   = 0xE000E000;
            __var AIRCR_Addr = SCS_Addr + 0xD0C;
            __var DHCSR_Addr = SCS_Addr + 0xDF0;

            // Execute SYSRESETREQ via AIRCR
            Write32(AIRCR_Addr, 0x05FA0004);
        - while: (Read32(DHCSR_Addr) & 0x02000000)
          timeout: 500000
```
