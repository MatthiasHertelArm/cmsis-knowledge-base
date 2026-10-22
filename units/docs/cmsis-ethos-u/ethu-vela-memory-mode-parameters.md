---
id: "ethu-vela-memory-mode-parameters"
type: "concept"
domain: "edge-ai"
title: "Vela: Create device-specific vela.ini file / Memory mode parameters"
summary: "Part of: Create device-specific vela.ini file"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#memory-mode-parameters"
license: "Apache-2.0"
mode: "V"
---

_Part of: Create device-specific vela.ini file_

| Parameter | Type or values | Description |
|---|---|---|
| `const_mem_area` | `Axi0` or `Axi1` | Location for read-only constants, including weights, scales, biases, and constant tensors. |
| `arena_mem_area` | `Axi0` or `Axi1` | Location for read/write feature maps, intermediate tensors, and Vela-managed working storage. |
| `cache_mem_area` | `Axi0` or `Axi1` | Staging or fast-scratch location. It is separate from the arena only when it resolves to a different memory type from `arena_mem_area`. |
| `arena_cache_size` | Integer, bytes | Scheduler's fast-memory budget: the arena target when arena and cache resolve to the same memory type, or the separate staging-cache size when they differ. The CLI `--arena-cache-size` overrides it for `Performance` optimization. |
| `inherit` | `Part.Name` | Parent section whose parameters are inherited. Child values take precedence. |

The memory-area mapping must be consistent with the Ethos-U driver, the ML
inference runtime tensor arena, the linker script, and the physical memory
system. These options guide compilation; they do not configure the hardware.

With `--optimise Size`, the Vela compiler minimizes SRAM use and does not use
the arena-cache size. With `--optimise Performance`, it uses the configured or
command-line arena-cache size. If neither is supplied, the compiler uses the
maximum addressable size for the selected Ethos-U target.
