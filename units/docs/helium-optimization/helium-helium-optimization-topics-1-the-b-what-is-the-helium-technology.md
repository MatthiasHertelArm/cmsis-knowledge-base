---
id: "helium-helium-optimization-topics-1-the-b-what-is-the-helium-technology"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #1 - the basics: What is the Helium Technology"
summary: "Arm Helium Technology is an optional architecture extension in the Armv8.1-M architecture."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/basic_optimization_topics.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/basic_optimization_topics.md#what-is-the-helium-technology"
license: "Apache-2.0"
mode: "V"
---

Arm Helium Technology is an optional architecture extension in the Armv8.1-M architecture. It contains a range of instructions to enable better signal processing and machine learning processing performance with a relatively small increase in the hardware cost of the processor design. The Helium technology is currently supported in the following processors:

- Arm Cortex®-M85
- Arm Cortex-M55
- Arm Cortex-M52

In Armv8.1-M architecture, Helium technology is referred as M-Profile Vector Extension (MVE). Helium is a brand name that is specific to Arm implementation of MVE.

MVE brings over 150 new instructions to Cortex-M processors, most of them are vector processing instructions. In the context of MVE, a vector is 128-bit wide and can contain data elements of either:

- sixteen 8-bit data (e.g. int8_t), or
- eight 16-bit data (e.g. int16_t, _Float16), or
- four 32-bit data (e.g. int32_t, float)

Using the concept of Single-Instruction, Multiple-Data (SIMD), MVE instructions allows more data to be processed in each instruction. But of course, having a 128-bit ALU in the Cortex-M processor can be a bit expensive in terms of power and silicon area. Therefore in both Cortex-M55 and Cortex-M85 processors, the MVE data path is only 64-bit wide. It means each vector processing takes two clock cycles.

To enable the best possible performance and efficiency, Armv8.1-M processors (e.g. Cortex-M55, Cortex-M85) allows the execution cycles of MVE instructions to be partially overlapped, providing that the instructions are in different instruction groups (i.e. no hardware resource conflict). By interleaving MVE instructions from different instruction groups, the processor can get to a processing bandwidth of 1 instruction per cycle.

In addition to vector processing instructions, MVE instruction set also cover various forms of memory read/write instructions, including variants of read/write with packing, unpacking, interleaving, etc. To enable best performance, Armv8.1-M also support a Low-Overhead-Branch (LOB) extension, which provide loop instructions that have minimal loop overhead.

To make the most out of an Arm Cortex-M processor with the Helium technology, we can start our journey with the following areas:

- Initialization of the processor’s hardware
- Toolchain
- Selection of data types
- Use of optimized software libraries
- Utilizing auto-vectorization feature in C compiler

If you are new to Helium technology and Armv8.1-M architecture, the following paper provides a good starting point:
[Introduction to Armv8.1-M Architecture](https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/introduction-to-armv8-1-m-architecture.pdf)
