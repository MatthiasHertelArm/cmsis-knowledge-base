---
id: "tbx-pyocd-debugger-system-resources"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `system-resources:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#system-resources"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains a list of memory regions that pyOCD uses to build the device memory map. A default Cortex-M memory map is used
as the baseline and is then updated with the information provided in the `memory:` node. If no memory regions are specified,
pyOCD falls back to the default Cortex-M memory map.

`system-resources:`                               |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
    `memory:`                      |   Optional   | Identifies the section for memory.

`memory:`                                         |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- name:`                                         | **Required** | Name of the memory region (when PDSC contains id, it uses the id as name).
    `access:`                      | **Required** | Access attribute string for the memory ([see `access:` table here](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-CBuild-Format.md#system-resources)).
    `start:`                       | **Required** | Base address of the memory.
    `size:`                        | **Required** | Size of the memory.
    `pname:`                       |   Optional   | Only accessible by a specific processor.
    `alias:`                       |   Optional   | Name of identical memory exposed at a different address.
    `default:`                     |   Optional   | Indicates a general purpose memory region.

**Default Cortex-M memory map:**

```yml
  system-resources:
    memory:
      - name: Code
        access: rx
        start: 0x00000000
        size: 0x20000000
      - name: SRAM
        access: rwx
        start: 0x20000000
        size: 0x20000000
      - name: Peripherals
        access: rwp
        start: 0x40000000
        size: 0x20000000
      - name: RAM1
        access: rwx
        start: 0x60000000
        size: 0x20000000
      - name: RAM2
        access: rwx
        start: 0x80000000
        size: 0x20000000
      - name: Devices-Shareable
        access: rwp
        start: 0xA0000000
        size: 0x20000000
      - name: Devices-NonShareable
        access: rwp
        start: 0xC0000000
        size: 0x20000000
      - name: System-Peripherals
        access: rwp
        start: 0xE0000000
        size: 0x20000000
```

**Example:**

```yml
  system-resources:
    memory:
      - name: ITCM_HE
        access: rwx
        start: 0x00000000
        size: 0x00040000
        pname: M55_HE
        alias: SRAM4
      - name: ITCM_HP
        access: rwx
        start: 0x00000000
        size: 0x00040000
        pname: M55_HP
        alias: SRAM2
      - name: MRAM
        access: rx
        start: 0x80000000
        size: 0x00580000
        default: true
      - name: SRAM2
        access: rwx
        start: 0x50000000
        size: 0x00040000
      - name: SRAM4
        access: rwx
        start: 0x58000000
        size: 0x00040000
```
