---
id: "helium-software-optimization-for-dsp-and-the-constraints-in-microcontrollers"
type: "concept"
domain: "optimization"
title: "Software optimization for DSP and ML - Making the most out of the memory system in microcontroller devices: The constraints in microcontrollers"
summary: "Typically, the following areas can be considered as key constraints in microcontroller applications:"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Memory/Software_optimization_for_memory_constrained_devices.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Memory/Software_optimization_for_memory_constrained_devices.md#the-constraints-in-microcontrollers"
license: "Apache-2.0"
mode: "V"
---

Typically, the following areas can be considered as key constraints in microcontroller applications:

- The size of the instruction and data caches inside the processors: In Cortex-M processors that support caches, the maximum size for the Instruction and data caches is 64KB. The typical cache size is between 16KB to 32KB.
- The size of the Tightly Coupled Memories (TCMs): TCMs are SRAM blocks that are connected directly to the processor to minimize the access latency (usually TCM accesses are single cycle). In the Cortex-M85, Cortex-M55 and Cortex-M52 processors, there are often Instruction and Data TCMs, which each have fixed address ranges in the memory map. Theoretically, the maximum TCM size supported by these processors is 16MB. However, because the maximum clock speed of large SRAM blocks is usually limited, typically the actual TCM size ranges from 128KB to 512KB.  In Cortex-M processors with TCMs, the processors also support an additional bus interface to allow other bus managers (e.g. a DMA controller) to access the TCMs. This feature avoids the need to copy data between the TCMs and other memories (e.g. main system memory) using software.
- The size of the on-chip system SRAM: On-chip system SRAMs are connected to the processor and other bus managers via bus interconnect components. Usually, the size of the system SRAM is larger than the caches and the TCMs.  For example, in microcontroller devices the on-chip system SRAM is usually in the range of 256KB to 2MB. Due to the larger memory size of the system SRAM, access to the SRAM blocks usually takes multiple processor clock cycles. Combining the multi-cycle access with the additional latency in the bus interconnect, the latency of a read access to the system SRAM could range from 4 to 10 clock cycles. However, because the processors support caches, the reads to the system SRAM only occurs when there is a cache miss or when the cache is disabled. Because of this cache feature, the average access cycle to the system SRAM is still close to single cycle.
- The lack of additional caches: In most cases, apart from level 1 caches inside the processor, the overall memory system does not have additional level 2 and level 3 caches. So, if there is a cache miss in the level 1 cache, the access would have to be carried out by the memory controller, which can take a longer time.
- Access latency in embedded flash memories and external serial flash memories. These types of memories are usually much slower than the processor speed.
- Memory access bandwidth. Helium technology is based on the Single Instruction Multiple Data (SIMD) concept with a vector (consisting of multiple data elements of the same data type) width of 128-bit. However, the memory interface of the buses, TCMs and RAM blocks are narrower than that, usually 64-bit or 32-bit. As a result, a bottleneck might be observed, caused by the memory bandwidth limitations.
- Many microcontrollers include a small retention memory. In applications where the device can sleep for a long period of time, the retention memory can be used to hold system states to allow the application to be resumed quickly, even though the rest of the memory system are powered down. Retention memories are optimized for low power, can be quite small in memory size, and are not optimized for performance. As a result, retention memories are less likely to be used by DSP and ML processing.

In addition to these constraints, designers also need to consider other factors such as:

- If appliable, real-time requirements of the applications.
- Optimizing the application(s) for low power.
