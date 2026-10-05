---
id: "helium-helium-optimization-topics-2-optim-reworking-loops"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #2 - Optimizing C functions: Reworking loops"
summary: "In many cases we can improve the performance of data array processing by modifying the loops."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/optimizing_c_functions.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/optimizing_c_functions.md#reworking-loops"
license: "Apache-2.0"
mode: "V"
---

In many cases we can improve the performance of data array processing by modifying the loops.

The below pictures represents samples organized in a 2D array (it could be a matrix, a picture ...)

The gray rectangle represent the vector. In this example the vector have 4 lanes (they contain 4 samples) so the datatype of the samples in this example is either `float32` or `q31`.

In the first picture, the array width is much bigger than the array height. So it makes sense to slice the array horizontally and generate vectors from the horizontal slice of data.

At the end, often the final vector will not be full. So the end of the loop (the tail) will need to be handled differently. Helium provides tail predication for this and it is covered in the advanced section. You don't have to use tail predication and can only write a normal scalar code for the tail. It will be less efficient but simpler.

(figure: horizontal)

If the data is organized differently (for instance with height much bigger than the width) then you have to slice you data differently to be able to create enough vectors. In the below example the data is sliced vertically. It is ok from a compute point of view : you generate more vector per slice of data. But the problem is that the data is no more contiguous in memory. So loading the data into the vectors is requiring more data accesses and it can cancel the compute optimization. To know if slicing the data vertically is useful for the performances or not, you need to consider the memory accesses as explained in  next section.

(figure: vertical)

Another possibility to make more vectorization possible is to unroll a loop. If you compute 4 iterations of the loop at a time, then perhaps you may put the values of the different iterations in a vector.

It is possible to mix both ideas : vectorizing by slicing the data and adding more vectorization possibilities by unrolling the loop.

> **Note:** If the loop body is long/complex, unrolling the loop can make it harder for the compiler to spot opportunity for auto-vectorization.

In the above examples, we could work on several rows or several columns at the same time

If you work on several rows and columns of the data at the same time, it means you work of sub-rectangles. You may slice those sub-rectangles vertically or horizontally depending on what is making more sense for the algorithms.

In summary : to vectorize the algorithm you need to understand how the data can be covered by vectors. You may cover the data by vertical slices, horizontal slices, rectangles ...

At the end, you must be able to compute with the data you have in a vector and it depends on what you want to compute. Some slicing strategy may be good from a memory point of view but does not map very well on what you are trying to compute.
