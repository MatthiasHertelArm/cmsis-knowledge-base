---
id: "ethu-vela-create-the-linker-script"
type: "concept"
domain: "edge-ai"
title: "Vela: Create device-specific vela.ini file / Create the linker script"
summary: "Part of: Create device-specific vela.ini file"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#create-the-linker-script"
license: "Apache-2.0"
mode: "V"
---

_Part of: Create device-specific vela.ini file_

The linker script places the generated model artifacts and runtime buffers in
the physical memories represented by the selected `System_Config` and
`Memory_Mode`. It does not use the logical names `Axi0` and `Axi1` directly.
Instead, it provides sections or memory regions for the Ethos-U I/O resources.

The linker section names are device- and runtime-specific. The examples provided with this pack use the following section names.

| Vela area | Linker section
in examples | Content | Access |
|---|---|---|---|
| `const_mem_area` | `ethos_model` | Compiled model, command stream, encoded weights, scales, and other constants | Read-only |
| `arena_mem_area` | `ethos_arena` | Input, output, intermediate activations, and scratch storage used by the ML inference runtime | Read-write |
| `cache_mem_area` | `ethos_cache` | Optional scratch-fast or staging buffer when it resolves to a different physical memory from `arena_mem_area` | Read-write |

Different section names can be used, the important
property is their physical placement. If `arena_mem_area` and `cache_mem_area`
resolve to the same memory type, a separate cache section is not required. If
they resolve to different memory types, reserve the configured
`arena_cache_size` in the fast memory used for `cache_mem_area`.

The linker script, MPU/SAU attributes, and CPU cache policy must make every
generated region accessible to both the ML inference runtime and the NPU as
required. When Cortex-M software and the NPU use different addresses for the
same memory, the driver must provide the corresponding address translation.
The driver's command-stream and region attributes must also select access paths
that match the linker placement.

Validate a new linker configuration by checking:

- the link map contains the compiled model and all runtime buffers in the
  intended physical memories;
- the allocated arena and optional scratch-fast buffer are at least as large as
  the compiler reports;
- all used command-stream base regions are accessible to the NPU;
- MPU/SAU and cache attributes match the driver cache-maintenance policy; and
- the optimized model runs correctly and meets its memory and performance goals
  on the device.
