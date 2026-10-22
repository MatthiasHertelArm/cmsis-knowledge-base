---
id: "ethu-integration-advanced-topics"
type: "concept"
domain: "edge-ai"
title: "Integration: Advanced topics"
summary: "Ethos-U65 and Ethos-U85 can use a memory mode in which arena_mem_area and cache_mem_area resolve to different memory types. The tensor arena can reside in external writable memory while a faster SRAM region is used for staging."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/integration/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/integration/src/main.md#advanced-topics"
license: "Apache-2.0"
mode: "V"
---

<!-- Future topics:
- CPU/NPU address remapping
- Multi-NPU or multi-variant configurations
- Cache-coherency strategies
- Run-time selection of driver regions
-->

### Use separate scratch-fast memory on Ethos-U65 and Ethos-U85

Ethos-U65 and Ethos-U85 can use a memory mode in which `arena_mem_area` and
`cache_mem_area` resolve to different memory types. The tensor arena can reside
in external writable memory while a faster SRAM region is used for staging.
This arrangement is not applicable to Ethos-U55 because its AXI1 interface is
read-only.

Select a compatible memory mode and set `arena_cache_size` to the available
scratch-fast capacity. Reserve the `cache_mem_area` in the linker script and
configure its MPU/SAU, cache, and driver region settings consistently. See
Understand arena cache and spilling
and Create the linker script.

### Move the tensor arena to external DRAM on Ethos-U65 and Ethos-U85

Assume that the selected target provides NPU-accessible external DRAM and that
the tensor arena currently resides in SRAM. Moving it to DRAM requires these
coordinated changes:

- **Vela:** Select a compatible `Memory_Mode` in which `arena_mem_area` resolves
  to the target's external DRAM access path. Keep the target's `System_Config`
  fixed.
- **Linker:** Move the `ethos_arena` section to the DRAM memory region, preserve
  its required alignment, and use the linker map to confirm that it fits.
- **MPU/SAU and cache policy:** Configure the DRAM attributes so that the
  runtime and NPU have the required access and the CPU cache policy is explicit.
- **Driver:** Set `NPU_REGIONCFG_1`, which represents `arena_mem_area`, to the
  target-specific external-memory access path. Override
  `ethosu_address_remap()` if the CPU and NPU use different DRAM addresses.
- **Cache hooks:** If the CPU mapping is cacheable and is not coherent with the
  NPU, implement `ethosu_flush_dcache()` before NPU reads and
  `ethosu_invalidate_dcache()` after NPU writes. Cache maintenance is not needed
  for a non-cacheable or hardware-coherent mapping.
- **Validation:** Rebuild and verify the linker-map placement, NPU access, model
  correctness, memory use, and performance on the target.
