---
id: "tbx-csolution-project-format-add-memory"
type: "concept"
domain: "project"
title: "CSolution Project Format: Add Memory"
summary: "Hardware targets may have additional off-chip memory. The memory: node that can be added as additional information to a target type. This information is used for the Run and Debug Management and the Automatic Linker Script generation."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#add-memory"
license: "Apache-2.0"
mode: "V"
---

Hardware targets may have additional off-chip memory. The `memory:` node that can be added as additional information to a target type.
This information is used for the [Run and Debug Management](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/YML-CBuild-Format.md#run-and-debug-management) and the [Automatic Linker Script generation](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#automatic-linker-script-generation).

### `memory:`

`memory:`                       |              | Content
:-------------------------------|:-------------|:------------------------------------
`- name:`                       | **Required** | Identifier of the memory.
    `access:`    | **Required** | Access attribute string for the memory (see table below).
    `start:`     | **Required** | Base address of the memory.
    `size:`      | **Required** | Size of the memory.
    `pname:`     |   Optional   | Only accessible by the specified processor.
    `algorithm:` |   Optional   | Programming algorithm for download.
    `ram-start:` |   Optional   | Start address of the RAM region used to execute the programming algorithm.
    `ram-size:`  |   Optional   | Maximum RAM size available for executing the programming algorithm.

The `ram-start:` and `ram-size:` values apply when `algorithm:` specifies a custom flash programming algorithm. When they are omitted, CMSIS-Toolbox uses the first memory region marked as default with `rwx` access. If no such region exists, it uses the RAM settings of another programming algorithm defined by the DFP. An error is reported when no suitable default RAM region or algorithm RAM settings are available.

The table lists the letters and their meaning for use in the access attribute string.

`access:` | Description
:--------:|:------------------
r         | Readable
w         | Writable
x         | eXecutable
s         | Secure attribute
n         | Non-secure attribute
c         | non-secure Callable attribute

**Example:**

```yml
solution:
  :
  target-types:
    - type: MyHardware
      device: STMicroelectronics::STM32F746NGHx
      memory:                                  # Additional memory available in MyHardware
        - name: Ext-Flash                      # Identifier
          access: rx                           # access permission
          start: 0x40000000
          size: 0x200000
          algorithm: Flash/Ext-Flash.flm       # Programming algorithm
          ram-start: 0x20000000                # RAM used to execute the algorithm
          ram-size: 0x20000
```
