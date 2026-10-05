---
id: "helium-helium-optimization-topics-2-optim-minimizing-memory-accesses-unrolling-dat"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #2 - Optimizing C functions: Minimizing memory accesses (unrolling, data grouping, temporary  copy)"
summary: "When data is not contiguous in memory, you cannot load it with one vector load and several accesses are needed."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/optimizing_c_functions.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/optimizing_c_functions.md#minimizing-memory-accesses-unrolling-data-grouping-temporary-copy"
license: "Apache-2.0"
mode: "V"
---

When data is not contiguous in memory, you cannot load it with one vector load and several accesses are needed.

If this data cannot be reused in lot of instructions you won't be able to amortize the cost of loading the data.

Let's take the example of a matrix multiply : you can do a dot product between 4 rows and one column to generate 4 samples of one column of the result. In that case, the data loaded from the column is reused 4 times with 4 different rows.

The overhead of loading the non contiguous data is amortized on the 4 computations.

Another possibility, when it makes sense, is to copy the non contiguous data into a temporary buffer where the copy will be contiguous. Then, the algorithm can work from this temporary copy.

Unrolling a loop can be useful to reuse some data in several computations. In the example of the matrix multiply, if we were working row per row it would not be efficient since we would be reloading the same column too many times. If we work per packet of 4 rows (so 4 loop iterations at a time), we can reuse the column data.

Unrolling a loop can be useful (as explained in previous section) to provide more flexibility in how you slice your data : sub-rectangles ...

In other cases, you might see no benefit with loop unrolling. Do not forget that Armv8.1-M supports Low-Overhead Branch extension so the loop overhead is already minimized. In such case, unrolling loops can increase code size (which might lead to more cache misses) and might make it harder for the compiler to spot opportunity for autovectorization. As a result, you should test the codes to check if loop unrolling can really bring benefit(s).
