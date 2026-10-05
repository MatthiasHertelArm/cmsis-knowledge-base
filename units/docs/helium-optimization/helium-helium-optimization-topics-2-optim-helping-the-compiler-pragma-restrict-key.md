---
id: "helium-helium-optimization-topics-2-optim-helping-the-compiler-pragma-restrict-key"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #2 - Optimizing C functions: Helping the compiler (pragma, restrict keyword ...)"
summary: "Once you have reworked your loops, the inner loop should be the one that the compiler can vectorize. It should work on contiguous data."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/optimizing_c_functions.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/optimizing_c_functions.md#helping-the-compiler-pragma-restrict-keyword"
license: "Apache-2.0"
mode: "V"
---

Once you have reworked your loops, the inner loop should be the one that the compiler can vectorize. It should work on contiguous data.

You should compile with options that enable the auto-vectorization in your compiler.

Note that auto-vectorization results are highly compiler and code dependent. The result may not be good and in that case you would need to manually vectorize the loop by using Helium intrinsics.

But the most difficult is to rework the loop to prepare them for the vectorization.

Some compiler provides pragma for more control on auto-vectorization and unrolling.

Use of `restrict` keyword in the API of the functions can help a lot the compiler to generate better vectorized code.

It is advised to compile with `-Ofast`

At this stage auto-vectorization support for Helium in GCC is still work in progress. For the time being, use Arm AC6 or LLVM based compiler for best results.
