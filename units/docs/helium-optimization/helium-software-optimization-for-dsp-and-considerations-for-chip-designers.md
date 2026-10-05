---
id: "helium-software-optimization-for-dsp-and-considerations-for-chip-designers"
type: "concept"
domain: "optimization"
title: "Software optimization for DSP and ML - Making the most out of the memory system in microcontroller devices: Considerations for chip designers"
summary: "Unlike traditional control applications, DSP and ML applications often have a much larger data memory requirement."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Memory/Software_optimization_for_memory_constrained_devices.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Memory/Software_optimization_for_memory_constrained_devices.md#considerations-for-chip-designers"
license: "Apache-2.0"
mode: "V"
---

Unlike traditional control applications, DSP and ML applications often have a much larger data memory requirement. In addition, microcontrollers designed for IoT applications often include the TrustZone feature, which means the memories (including the TCMs) can be partitioned into Secure and Non-secure address ranges and be utilized by both secure firmware and normal applications. As a result, the cache and TCM size required are usually larger than traditional devices designed for control applications.

To enable efficient usage of the TCMs, chip designs should include DMA controller(s) to enable data transfers between the TCMs and the main memories and for traditional DMA usage. By having a DMA controller, data can be transferred between the main memories and the TCMs while the processor is handing other processing tasks.

For the best performance, TCM access should be designed as single cycle. That said, the TCM interfaces in Cortex-M85, Cortex-M55 and Cortex-M52 support waitstates. If necessary, to support a larger TCM size which cannot be single cycle at the maximum clock speed, it is possible to create a TCM memory system, with part of the TCM address range supporting single cycle access and the remaining address range(s) supporting multi-cycle access.

It is not necessary to keep the Instruction cache and Data cache the same size. In some instances, for certain DSP/ML applications, the whole program code can be copied into the I-TCM and when that is the case, there is no need for an Instruction cache. However, the program size for most microcontroller applications is larger than the Instruction TCM and therefore copying the whole program codes to the I-TCM is not feasible. At the same time, the non-volatile program storage (e.g. embedded flash) has a slow access speed. In such cases, both Instruction caches and Data caches are needed because the program codes contain various constant values that are cached via the Data cache.

For low-cost microcontrollers designed with the Cortex-M52 processor, there is a configuration option of having a unified cache. This is suitable for designs where R/W data is mostly placed in the SRAM connected to the D-TCM, and hence a full data cache could be overkill. When the unified cache configuration is used there is no data cache in the processor.
