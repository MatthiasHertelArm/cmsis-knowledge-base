---
id: "helium-helium-optimization-topics-3-proce-instruction-alignment"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #3 - Processor specific details: Instruction alignment"
summary: "For best performance, Helium instructions (especially those inside a critical loop) should be aligned to 32-bit boundaries."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/processor_specific.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/processor_specific.md#instruction-alignment"
license: "Apache-2.0"
mode: "V"
---

For best performance, Helium instructions (especially those inside a critical loop) should be aligned to 32-bit boundaries. The software would still work if the Helium instructions were unaligned, but this can cause stall cycles in loops even when the Low Overhead Branch (LOB) extension is used. This is usually taken care by C compilers. But if you are creating inline assembly code, you need to handle the alignment manually.

Note: sometime C compilers insert a NOP in the being of the loop after DLS/WLS{TP}. This NOP is not a part of the loop, but a padding instruction to keep the instruction in the loop aligned. To determine the correct loop address, please using the negative offset in the LE instruction, and do not rely on the position of the WLS/DLS{TP} instruction.

    When creating hand optimized code with inline assembly, you can use directive “.p2align 2” to align instructions to 32-bit.
