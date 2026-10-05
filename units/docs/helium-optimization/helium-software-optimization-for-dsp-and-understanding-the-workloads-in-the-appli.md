---
id: "helium-software-optimization-for-dsp-and-understanding-the-workloads-in-the-appli"
type: "concept"
domain: "optimization"
title: "Software optimization for DSP and ML - Making the most out of the memory system in microcontroller devices: Understanding the workloads in the applications"
summary: "When optimizing the chip designs and the software, one of the key tasks for designers is to understand the memory usages and the behaviours of the memory access in the workloads."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Memory/Software_optimization_for_memory_constrained_devices.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Memory/Software_optimization_for_memory_constrained_devices.md#understanding-the-workloads-in-the-applications"
license: "Apache-2.0"
mode: "V"
---

When optimizing the chip designs and the software, one of the key tasks for designers is to understand the memory usages and the behaviours of the memory access in the workloads. Some of the typical characteristics of DSP and ML processing codes are as follows:

### Low-level DSP processing functions

- The functions have a small code size. As a result, the program codes cache very well in the processor caches.
- The functions might need coefficients that are read-only data. In some cases, the coefficient data could require a considerable memory size.
- The data being processed is different in every iteration. As a result, designers cannot rely on the caching of input data. However, input data is often accessed sequentially and therefore after a cache miss, the cache linefill would cache the required data as well as the subsequence data within the same cacheline (which is 8 words in size). As a result, cache misses usually only take place at the beginning of a cacheline.

### Neural Network (NN) inference in ML applications

- The NN weights in a ML model can be quite large.  Although the model weight in each NN layer could be grouped together and arranged so that they are accessed sequentially, the overall size of the NN weight data could be much larger than the data cache and therefore the data might not fit into the cache. As a result, in each iteration, the previous cached weight data may have been evicted from the cache and resulted in cache misses at the beginning of each cacheline.
- Activation data can range from small to large depending on the ML model and application. For example, inference of images has a much larger memory usage than keyword spotting or vibration analysis.
- Potentially a large program size.  Some ML runtime libraries (e.g. TensorFlow Lite for microcontrollers) often contain a lot of code. This is because these libraries include many low-level functions for different ML operators, as well as the code for interpretating the ML models. However, this does not mean that we need a very big instruction cache. This is because during inference processing, only a few operators would be used for each layer and the code size for each operator can be quite small. As a result, most of the ML runtime libraries work very well with a cached program memory system.

In addition to the characteristics of the DSP and ML processing, designers should also look at the characteristics of other software components in the application. For example, software developers need to identify what data in the main system memory should be cached and what should not. For example, a bitmap image for a user interface might only need to be accessed once in a while and therefore should not be cached.
