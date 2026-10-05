---
id: "ethu-driver-data-caching"
type: "concept"
domain: "edge-ai"
title: "Driver: Data caching"
summary: "Cache maintenance is required when the CPU and NPU share memory that is cached by the CPU. The driver provides weak no-op implementations of two hooks. If the ML runtime does not manage the cache, override both hooks:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/driver/src/main.md#data-caching"
license: "Apache-2.0"
mode: "V"
---

Cache maintenance is required when the CPU and NPU share memory that is cached
by the CPU. The driver provides weak no-op implementations of two hooks. If the
ML runtime does not manage the cache, override both hooks:

- ethosu_flush_dcache() is called before the NPU
  starts. It must clean cacheable base-address regions so that the NPU sees the data written by the CPU.
- ethosu_invalidate_dcache() is called when the
  driver finalizes the inference. It must invalidate cacheable base-address
  regions so that the CPU sees NPU writes.

The hooks receive the `base_addr` regions, but not the command stream. If the
command stream is in cached memory written by the CPU, the application or ML
runtime must clean it before invoking the inference. If the ML runtime already
performs all required cache maintenance, the default weak no-op functions are
sufficient.

For example, a platform can use the driver cache functions as follows:

```c
void ethosu_flush_dcache(const uint64_t *base_addr, const size_t *base_addr_size, int num_base_addr)
{
    for (int i = 0; i < num_base_addr; i++)
    {
        SCB_CleanDCache_by_Addr((uint32_t *)(uintptr_t)base_addr[i], base_addr_size[i]);
    }
}

void ethosu_invalidate_dcache(const uint64_t *base_addr, const size_t *base_addr_size, int num_base_addr)
{
    for (int i = 0; i < num_base_addr; i++)
    {
        SCB_InvalidateDCache_by_Addr((uint32_t *)(uintptr_t)base_addr[i], base_addr_size[i]);
    }
}
```

> [!Note]
>
> - The example maintains every complete `base_addr` region. This is
> conservative. A platform or ML runtime can reduce cache-maintenance overhead
> by maintaining only the tensor ranges accessed by the NPU when it knows those
> ranges and controls their ownership.
> - The cache-maintenance ranges must meet the CPU's cache-line alignment
> requirements. The CPU must not write an NPU-owned region between the clean
> and invalidate operations.
> - The NPU memory attributes must match the CPU MPU configuration. See
> Command stream regions
> and base pointers.
