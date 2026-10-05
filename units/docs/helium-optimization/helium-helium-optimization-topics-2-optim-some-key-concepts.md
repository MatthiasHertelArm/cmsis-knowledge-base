---
id: "helium-helium-optimization-topics-2-optim-some-key-concepts"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #2 - Optimizing C functions: Some key concepts"
summary: "Helium technology is based on SIMD (Single Instruction, Multiple Data) operations, this is also called vector processing as the instructions process vector of data element."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/optimizing_c_functions.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/optimizing_c_functions.md#some-key-concepts"
license: "Apache-2.0"
mode: "V"
---

Helium technology is based on SIMD (Single Instruction, Multiple Data) operations, this is also called vector processing as the instructions process vector of data element. The vector size is 128-bit and can contains:
- Four 32-bit data elements (integer or single precision floating-point data) 
- Eight 16-bit data elements (integer or half precision floating-point data)
- Sixteen 8-bit data elements (integer)

To get the best balance between performance and energy efficiency, the current Armv8.1-M processor implementations does not provide a 128-bit wide ALU. Instead, the data processing are handled over multiple clock cycles:

- Cortex-M52 processor provides a 32-bit data path (single beat implementation). So each vector operation take 4 clock cycles to compare.
- Cortex-M55 and Cortex-M85 processors provide 64-bit data path (dual beat implementation). So each vector operation take 2 clock cycles to compare.

To maximize the performance, the processor pipeline allows overlapping of operations in different instruction groups. For example, in a sequence of interleaving memory load and multiply-accumulate instructions, the processor can start processing the first half of the vector while reading the second half of the data. An illustration of the overlapping execution for a dual beat implementation is as follows:

(figure: Overlapping of instruction execution in Cortex-M55 pipeline)

More information about the Cortex-M55 processor can be found in this paper: [Introduction to the Arm Cortex-M55 Processor](https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/introduction-to-arm-cortex-m55-processor.pdf)

Generally, C compilers should be able to schedule instructions to interleave different types of instructions to maximize the overlapping. However, if you need to write optimized code at low-level (either using intrinsic functions or inline assembly), you need to take care to interleave different types of instructions by avoiding back-to-back memory accesses or back-to-back data processing that use the same ALU functions.
