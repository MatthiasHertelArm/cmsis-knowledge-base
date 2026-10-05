---
id: "alp-visualizing-ethos-u-performance-8-evaluate-output-observe-the-ethos-u-performanc"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Evaluate Ethos-U Performance: Observe the Ethos-U Performance Monitoring Unit"
summary: "This output shows Ethos-U performance, from the Performance Monitoring Unit (PMU)"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/8-evaluate-output/#observe-the-ethos-u-performance-monitoring-unit"
license: "CC-BY-SA-4.0"
mode: "V"
---

This output shows Ethos-U performance, from the Performance Monitoring Unit (PMU)
```bash { output_lines = "1-7" }
I [executorch:arm_perf_monitor.cpp:180] Ethos-U PMU report:
I [executorch:arm_perf_monitor.cpp:181] ethosu_pmu_cycle_cntr : 4738932
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr0 : 1447178
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr1 : 420661
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr2 : 0
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr3 : 0
I [executorch:arm_perf_monitor.cpp:184] ethosu_pmu_cntr4 : 130
```

**Table of Ethos-U PMU Counters:**
|PMU Counter|Default Event Tracked|Description|Interpretation|
|-----------|---------------------|-----------|--------------|
|ethosu_pmu_cycle_cntr|Total NPU cycles|Counts the number of core clock cycles where the Ethos-U NPU was executing work.|High value = long runtime; use to compute throughput.|
|ethosu_pmu_cntr0|SRAM read data beats received(ETHOSU_PMU_SRAM_RD_DATA_BEAT_RECEIVED)|How many data beats (e.g., 64-bit words) the NPU read from local SRAM.|Indicates input + weight loading efficiency.|
|ethosu_pmu_cntr1|SRAM write data beats written(ETHOSU_PMU_SRAM_WR_DATA_BEAT_WRITTEN)|Number of data beats the NPU wrote back to SRAM (e.g., outputs or intermediate results).|Reflects output bandwidth usage.|
|ethosu_pmu_cntr2|External DRAM read beats(ETHOSU_PMU_EXT_RD_DATA_BEAT_RECEIVED)|Number of data beats read from off-chip memory (e.g., DRAM). Often 0 if Sram_Only is used.|If non-zero, may indicate cache misses or large model size.|
|ethosu_pmu_cntr3|External DRAM write beats(ETHOSU_PMU_EXT_WR_DATA_BEAT_WRITTEN)|Number of write data beats to external memory.|Helps detect offloading or insufficient SRAM.|
|ethosu_pmu_cntr4|Idle cycles(ETHOSU_PMU_NPU_IDLE)|Number of cycles where the NPU had no work scheduled (i.e., idle).|High idle count = possible pipeline stalls or bad scheduling.|
