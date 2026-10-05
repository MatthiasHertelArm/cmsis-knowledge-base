---
id: "ethu-vela-read-the-vela-reports"
type: "concept"
domain: "edge-ai"
title: "Vela: Read the Vela reports"
summary: "After compilation, Vela prints a summary report and writes a CSV file in the output directory. The report reflects the selected accelerator configuration, system configuration, memory mode, and optimization strategy."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/vela/src/main.md#read-the-vela-reports"
license: "Apache-2.0"
mode: "V"
---

After compilation, Vela prints a summary report and writes a CSV file in the
output directory. The report reflects the selected accelerator configuration,
system configuration, memory mode, and optimization strategy.

| Report area | Meaning |
|---|---|
| Configuration | Selected accelerator, system and memory configurations, NPU clock, and design peak memory bandwidth. |
| Memory use | Required storage in each Vela memory type: `Sram`, `Dram`, `OnChipFlash`, or `OffChipFlash`. The selected system configuration and memory mode determine these memory types. |
| Operator placement | Number and percentage of operators assigned to the CPU and NPU. |
| Memory traffic | Estimated average bandwidth and bytes transferred for feature maps and weights. |
| MACs | Number of multiply-accumulate operations per batch. |

The CSV file uses `weights_storage_area` for the Vela memory type selected by
`const_mem_area` and `feature_map_storage_area` for the type selected by
`arena_mem_area`. It reports memory use as a total for each Vela memory type. In
`Dedicated_Sram_256KB`, both data roles resolve to `Dram`, so
`dram_memory_used` contains their combined requirement.
`total_npu_encoded_weights` covers only encoded weights, not the complete
constant area, so it cannot be used to derive the size of `arena_mem_area`.

Use `--verbose-cycle-estimate` to add estimated NPU and memory-access cycles,
total cycles, inference time, and inferences per second. Use
`--verbose-performance` to generate a per-layer CSV with memory use, cycle
estimates, MAC utilization, and the contribution of each layer to the network.
The summary report is normally sufficient for configuration comparison; use the
per-layer report to investigate the reason for a difference.

> [!CAUTION]
> Vela cycle counts and inference times are estimates, not measured
> performance. They are useful for estimating expected performance and comparing
> candidates, but the selected configuration must be validated on the target
> hardware.
