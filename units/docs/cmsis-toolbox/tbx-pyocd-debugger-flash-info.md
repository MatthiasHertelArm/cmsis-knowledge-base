---
id: "tbx-pyocd-debugger-flash-info"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `flash-info:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#flash-info"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains a list of target's flash memories information, which is used by pyOCD to determine which memory regions
should be treated as flash and how to program them using flash debug sequences.

`flash-info:`                                     |              | Content
:-------------------------------------------------|--------------|:------------------------------------
`- name:`                                         | **Required** | Name of the specified flash device.
&nbsp;&nbsp;&nbsp; `start:`                       | **Required** | Base address of the memory.
&nbsp;&nbsp;&nbsp; `page-size:`                   | **Required** | Page size. A page is the smallest unit that can be programmed.
&nbsp;&nbsp;&nbsp; `blocks:`                      | **Required** | List of blocks. A block is the smallest unit that can be erased.
&nbsp;&nbsp;&nbsp; `blank-val:`                   |   Optional   | 64-bit value in erased memory (default 0xFFFFFFFFFFFFFFFF). Value is truncated to match the access size.
&nbsp;&nbsp;&nbsp; `fill-val:`                    |   Optional   | 64-bit value that a debugger uses to fill the remainder of a page (default 0xFFFFFFFFFFFFFFFF).  Value is truncated to match the access size.
&nbsp;&nbsp;&nbsp; `ptime:`                       |   Optional   | Timeout in milliseconds for programming a page (default 300).
&nbsp;&nbsp;&nbsp; `etime:`                       |   Optional   | Timeout in milliseconds for erasing a block (default 300).
&nbsp;&nbsp;&nbsp; `pname:`                       |   Optional   | Executes programming only for a specific processor (default for all processors).

`blocks:`                                         |              | Content
:-------------------------------------------------|--------------|:------------------------------------
`- count:`                                        | **Required** | Number of blocks.
&nbsp;&nbsp;&nbsp; `size:`                        | **Required** | Block size in bytes. Total memory size (in bytes) is `size * count`.
&nbsp;&nbsp;&nbsp; `arg:`                         |   Optional   | Optional value that a debugger writes to the pre-defined debug access variable `__FlashArg` at start of a flash operation (default 0).

!!! Note
    - The [`gap` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_flashgap) is not used.

**Example:**

```yml
  flash-info:
    - name: Internal Flash (code) 64KB
      start: 0x00000000
      page-size: 0x00000040
      blocks:
        - count: 256
          size: 0x00000100
          arg: 0
      blank-val: 0x00000000FFFFFFFF
      ptime: 100000
      etime: 1000000
```
