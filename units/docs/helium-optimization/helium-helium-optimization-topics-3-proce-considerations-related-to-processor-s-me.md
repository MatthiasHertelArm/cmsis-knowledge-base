---
id: "helium-helium-optimization-topics-3-proce-considerations-related-to-processor-s-me"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #3 - Processor specific details: Considerations related to processor’s memory systems"
summary: "Many processing tasks like DSP and NN are data intensive, as a result, it is crucial to select the right memory types for data storage to ensure high data access performance (including high bandwidth and low latency)."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/processor_specific.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/processor_specific.md#considerations-related-to-processor-s-memory-systems"
license: "Apache-2.0"
mode: "V"
---

### I-TCM bandwidth

Many processing tasks like DSP and NN are data intensive, as a result, it is crucial to select the right memory types for data storage to ensure high data access performance (including high bandwidth and low latency). Otherwise, the processing performance can degrade significantly. For example, the I-TCM interface on the Cortex-M55 processor is only 32-bit width and the processor can access 64-bit of data per clock cycle. As a result, it is not a good idea to put read-only data coefficients in the I-TCM if the data is to be read using vector load instructions, even though the data is a part of a DSP function – copying the data into the D-TCM or system memory can help resolve this memory bandwidth issue. This could be done by:

- Use linker script feature to place the coefficients in other memories, or
- Avoid declaring the coefficient table as “const” and declare it as “static”.

The I-TCM bandwidth issue could also affect general program codes (for example, control codes) if the code contains a lot of literal data accesses. Program code running from AXI connected memories do not have the same issue.

### Data prefetching

To help performance, the D-caches of the Cortex-M55 and Cortex-M85 processors support data prefetching. In the Cortex-M55, the data prefetcher in the D-cache can only detect a linear access pattern with a constant stride (-2, -1, +1, +2 of the data array). Since a data processing function can access more than one stream of data, other data streams need to be placed in TCMs or uncacheable buffer to make use of the data prefetching.

The data prefetcher in the Cortex-M85 supports an additional prefetching mode call next-line mode, which is more performant. The prefetcher behaviors in the Cortex-M55 and Cortex-M85 are programmable. For more information, please refer to the Prefetch Control Register (PFCR) in the processor’s Technical Reference Manual.

### Hazards due to D-TCM banking structure

In the Cortex-M55 and Cortex-M85 processors, the D-TCM is divided into 4 banks (selected by bit 2 and bit 3 of the address). Because these processors can handle two load or two store operations when executing scatter store/gather load instructions, if the two accesses are targeting the same D-TCM bank, there would be a conflict and causes delay. Therefore, when using scatter store/gather load instructions, you might need to optimize the data layout to avoid this issue. The bus interface of the Cortex-M52 processor can only handle one transfer at a time, so this consideration is not applicable to the Cortex-M52 processor.

### Read after-write in D-TCM (Cortex-M52, Cortex-M55)

Another side effect of the D-TCM banking in Cortex-M52 and Cortex-M55 is that right after a store to a D-TCM bank, the read to the same D-TCM could be delayed. To avoid this conflict, you can adjust data alignment so that such read after store does not reach the same D-TCM bank. This aspect does not affect memory accesses on AXI or D-TCM interface on Cortex-M85.

### Scatter gather instructions

In Cortex-M55 and Cortex-M85 processors, the bus interface can generate two accesses in a single clock cycle.  DSP codes that contain scatter and gather memory load and store could performance better when the data is in the D-TCM. This is because the processor allows two separate data accesses that are 32-bit or smaller to be carried out simultaneously providing that these accesses are not targeting different words in the same D-TCM banks (Note: In Cortex-M55 and M85 there are 4 D-TCM banks interleaved by bit 2 and bit 3 of the addresses). With data access with AXI, the D-cache look up can handle one address per cycle.
