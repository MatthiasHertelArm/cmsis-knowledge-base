---
id: "vela-vela-cli-options-memory-modes"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Memory Modes"
summary: "The Vela configuration file defines three potential memory modes although other configurations are possible. Each memory mode is defined with respect to four attributes. If any of those attributes are not specified then an internal default value will be used."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#memory-modes"
license: "Apache-2.0"
mode: "V"
---

The Vela configuration file defines three potential memory modes although other configurations are possible.  Each
memory mode is defined with respect to four attributes.  If any of those attributes are not specified then an internal
default value will be used.  Note that this value may not be valid for the target embedded system.  Therefore, the user
is recommended to explicitly specify all settings.  
The three memory area attributes are each assigned to a virtual AXI port.  This assignment is used by the compiler to
map a memory area to a specific memory type (as defined in the System Configuration section).  It allows the System
Configuration sections to be reused with different Memory Mode sections.  It does not control the mapping of the
physical AXI ports of the hardware, which are pre-determined in the compiler and driver.

1. `const_mem_area` this is the memory area in which the compiler will store all constant data such as weights,
scales & biases, and constant value tensors.
1. `arena_mem_area` this is the memory area in which the compiler will look to access the TensorFlow Lite for
Microcontrollers Tensor Arena.
1. `cache_mem_area` this is the memory area in which the compiler uses as a cache memory if required by the selected
memory mode
1. `arena_cache_size` this is the size of the memory area available to the compiler for use by either the arena or cache
depending upon the memory mode

Please note that all of the above attributes must have values that correspond to the settings used by the Ethos-U Driver
and the TensorFlow Lite for Microcontrollers Application.  This is because the compiler does not have any direct control
over these other components.

The effect of `arena_cache_size` depends on the selected memory mode and optimisation strategy, as summarised below.  A
soft target guides performance optimisations but may be exceeded, while a hard limit is enforced during allocation.

| Memory mode | `--optimise Performance` | `--optimise Size` |
| --- | --- | --- |
| SRAM Only | Guides optimisation. May be exceeded. | Ignored. |
| Shared SRAM | Guides optimisation. May be exceeded. | Ignored. |
| Dedicated SRAM | Guides optimisation. Must not be exceeded. | Does not guide optimisation. Must not be exceeded. |

When `arena_cache_size` guides optimisation, Vela uses it when choosing options such as cascading, stripe sizes and
buffering.  Larger values may allow more memory-intensive performance optimisations, while smaller values encourage
memory-saving alternatives.

See [Arena Cache Size](#arena-cache-size) for the option description.

### Sram Only Mode

In this mode, the Embedded NPU only has access to SRAM memory.  The compiler will make use of two regions in the SRAM,
which may be separate or contiguous.  One region is used for the `const_mem_area` and the other region is used for the
`arena_mem_area`.  It is assumed that SRAM outside of these regions will be used by other software in the system (e.g.
TensorFlow Lite for Microcontrollers or an RTOS running on the Cortex-M CPU).  The `cache_mem_area` is not used.  The
`arena_cache_size` refers to the size of the `arena_mem_area`, but is not enforced as a hard allocation limit.  With
`--optimise Performance`, Vela uses it as a target but may produce a network requiring a larger arena.  With
`--optimise Size`, the value is ignored and the arena requirement is determined independently.  The TensorFlow Lite
for Microcontrollers Tensor Arena will contain all of the network input, output, and intermediate tensors, including
the Ethos-U scratch tensor which contains the NPU's internal working buffers.

### Shared Sram Mode

In this mode, the Embedded NPU has access to SRAM which is used for the `arena_mem_area`.  It also has access to some
other type of memory (e.g. Flash or DRAM) that is used for the `const_mem_area`.  The `cache_mem_area` is not used.  The
`arena_cache_size` refers to the size of the `arena_mem_area`, but is not enforced as a hard allocation limit.  With
`--optimise Performance`, Vela uses it as a target but may produce a network requiring a larger arena.  With
`--optimise Size`, the value is ignored and the arena requirement is determined independently.  It is assumed that SRAM
outside of the `arena_mem_area` will be used by other software in the system (e.g. TensorFlow Lite for Microcontrollers
or an RTOS running on the Cortex-M CPU).  The TensorFlow Lite for Microcontrollers Tensor Arena will contain all of the
network input, output, and intermediate tensors, including the Ethos-U scratch tensor which contains the NPU's internal
working buffers.

### Dedicated Sram Mode

In this mode, the Embedded NPU has access to SRAM which is used for the `cache_mem_area`.  It is assumed that use of
this memory is entirely dedicated to the Embedded NPU, as no support is provided for allocating parts of this at
run-time.  It also has access to some other type of memory (e.g. DRAM).  The compiler will make use of two regions in
this other type of memory, which may be separate or contiguous.  One region is used for the `const_mem_area` and
the other region is used for the `arena_mem_area`.  The `arena_cache_size` refers to the size of the `cache_mem_area`
and defines the maximum dedicated SRAM that Vela may allocate for cache/staging usage.  This value must not be exceeded.
With `--optimise Performance`, it also guides optimisation.  With `--optimise Size`, it does not guide optimisation.
It is assumed that memory outside of those regions will be used by other software in the system (e.g. TensorFlow Lite
for Microcontrollers or an RTOS running on the Cortex-M CPU).  The TensorFlow Lite for Microcontrollers Tensor Arena
will contain all of the network input, output, and intermediate tensors, including the Ethos-U scratch tensor which
contains the NPU's internal working buffers.
