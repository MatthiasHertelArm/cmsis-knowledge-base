---
id: "helium-helium-optimization-topics-2-optim-vectorize-a-data-processing-function"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #2 - Optimizing C functions: Vectorize a data processing function"
summary: "One of the first steps in Helium optimization is to ensure that the data processing task is vectorizable."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/optimizing_c_functions.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/optimizing_c_functions.md#vectorize-a-data-processing-function"
license: "Apache-2.0"
mode: "V"
---

One of the first steps in Helium optimization is to ensure that the data processing task is vectorizable. To utilize vector processing capability, the data processing in each vector lane must not have dependencies on the other results within each instruction.

(figure: Example operation sequences that can be vectorized and cannot be vectorized)

If your code has a sequence of operations that have data dependency (cannot be vectorized), but the sequence needs to be repeated a number of times, it might be possible to modify the code so that operations in different iterations can be grouped together into vectorized operations.

You can utilize auto-vectorization support in C compiler to check whether the code can be vectorized. With Arm Compiler 6 and LLVM compiler, vectorization diagnostic options are available:

```
-Rpass=loop-vectorize -Rpass-analysis=loop-vectorize -Rpass-missed=loop-vectorize
```

In some cases, program loops cannot be vectorized or can be difficult for the compiler to vectorized. These includes:

- Loops with interdependencies between different loop iterations.
- Loops with break clauses.
- Loops with complex conditions.
- Loops where the number of iterations is unknown at loop starts.
- Loops with double-precision floating point processing (low-overhead branch might still be used).
- Loops that involve operations that cannot be vectorized (for example, system operations like memory barriers).

Once you have codes that are vectorizable, you can optionally optimize the code in the loop body by introducing intrinsic functions.
