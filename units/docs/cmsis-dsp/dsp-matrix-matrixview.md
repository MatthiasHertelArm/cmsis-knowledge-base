---
id: "dsp-matrix-matrixview"
type: "concept"
domain: "optimization"
title: "Matrix: MatrixView"
summary: "It is also possible to create a virtual matrix : a view onto a subset of the matrix."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/matrix.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/matrix.md#matrixview"
license: "Apache-2.0"
mode: "V"
---

It is also possible to create a virtual matrix : a view onto a subset of the matrix.

Let's add the bottom right corner of the matrix to itself:

```cpp
result.sub(4,8,4,8) = result.sub(4,8,4,8) + result.sub(4,8,4,8)
```

The API is:

```cpp
MatrixView<P,C> sub(const index_t rs,
                    const index_t re,
                    const index_t cs,
                    const index_t ce)
```

You specify the row start and row end, then column start and column end.

Note that the end is the first index **after** the end of your rows or columns.

No stride is supported for matrix view in this version of the library.
