---
id: "mlek-testing-and-benchmarking-benchmarking"
type: "concept"
domain: "edge-ai"
title: "Testing and benchmarking: Benchmarking"
summary: "Profiling is enabled by default when configuring the project. Profiling enables you to display:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/testing_benchmarking.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/testing_benchmarking.md#benchmarking"
license: "Apache-2.0"
mode: "V"
---

Profiling is enabled by default when configuring the project. Profiling enables you to display:

- NPU event counters when the Arm® *Ethos™-U* NPU is enabled (see `ETHOS_U_NPU_ENABLED` in [Build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#build-options) )

  - Total cycle: The number of NPU cycles

  - Active cycles: number of NPU cycles that were used for computation

  - Idle cycles: number of cycles for which the NPU was idle

  - AXI0 read beats: The number of AXI beats with read transactions from AXI0 bus. AXI0 is the bus where
    *Ethos-U* NPU reads and writes to the computation buffers, activation buf, or tensor arenas.

  - AXI0 write beats: The number of AXI beats with write transactions to AXI0 bus.

  - AXI1 read beats: The number of AXI beats with read transactions from AXI1 bus. AXI1 is the bus where
   *Ethos-U* NPU reads the model. So, read-only.

- If CPU profiling is enabled, the CPU cycle counts and the time elapsed, in milliseconds, for inferences performed. For
  further information, please refer to the `CPU_PROFILE_ENABLED` in [Build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#build-options).

> **Note:** Only do this when running on a physical FPGA board as the FVP does not contain a cycle-approximate or
> cycle-accurate *Cortex-M* model.

For example:

- On the FVP:

```log
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 628122
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 135087
INFO - NPU AXI1_RD_DATA_BEAT_RECEIVED beats: 62870
INFO - NPU ACTIVE cycles: 1081007
INFO - NPU IDLE cycles: 626
INFO - NPU TOTAL cycles: 1081634
```

- For the MPS3 and MPS4 platforms, the time duration in milliseconds is also reported when `-DCPU_PROFILE_ENABLED=1` is added to
  CMake configuration command, like so:

```log
INFO - Profile for Inference:
INFO - NPU AXI0_RD_DATA_BEAT_RECEIVED beats: 628122
INFO - NPU AXI0_WR_DATA_BEAT_WRITTEN beats: 135087
...
INFO - Time ms: 210
```

The next section of the documentation refers to: [Memory Considerations](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/memory_considerations.md).
