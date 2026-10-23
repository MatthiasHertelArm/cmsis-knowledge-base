---
id: "ethu-vela-troubleshooting"
type: "concept"
domain: "edge-ai"
title: "Vela: Troubleshooting"
summary: "Vela: Troubleshooting"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#troubleshooting"
license: "Apache-2.0"
mode: "V"
---

| Symptom | Check |
|---|---|
| Most operations run on the CPU | Confirm integer quantization, inspect `--show-cpu-operations`, and generate `--supported-ops-report` to check every operator constraint. |
| Compilation succeeds but estimates look unrealistic | Use a platform-specific `System_Config`; verify clocks, AXI mappings, latency, bandwidth, and memory mode. Compare only builds with the same configuration. |
| Runtime allocation fails | Check the Vela compiler's peak-memory report and add firmware overhead. Align linker regions and the tensor arena with `cpu_tensor_alignment` and the chosen memory mode. |
| Performance degrades after reducing SRAM | A smaller cache can cause more AXI1 reads. Inspect the performance CSV/report and hardware PMU counters. |
| A wheel is unavailable | Install Python development headers, CMake, and C99/C++17 build tools, or use a supported host/Python combination. |
| Output does not run on the target | Recompile for the exact Ethos-U architecture/MAC configuration and keep `vela.ini`, driver, linker, and memory-region configuration consistent. |
