---
id: "dsp-matrix-matrix-operations"
type: "concept"
domain: "optimization"
title: "Matrix: Matrix operations"
summary: "In addition to the vector operations +,- and , matrixes are supporting more operations:"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/matrix.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/matrix.md#matrix-operations"
license: "Apache-2.0"
mode: "V"
---

In addition to the vector operations `+`,`-` and `*`, matrixes are supporting more operations:

* `dot` for vector / matrix products
* `diagonal` to create a diagonal matrix from a vector.
* `identity` to create an identity matrix
* `transpose` to create the transposed matrix
* `outer` for the outer product of two vectors

### dot

```cpp
result = dot(a,b);
```

The compiler may use the move semantic to copy the temporary result of the `dot` function to `result`.

In this case, no copy would occur and `result` after the assignment would be a vector allocated by `dot` so using the `TMP_ALLOC` .

### matvec

```cpp
result = bias + matvec(matrix, vector);
```

Unlike `dot(matrix, vector)`, `matvec(matrix, vector)` is lazy. It participates
in the normal one-dimensional fusion loop, so the matrix-vector result can be
combined with additions, multiplications, or accumulation without first being
stored in a temporary vector. Matrix-matrix products remain eager and continue
to use `dot`.

### diagonal

```cpp
result = Matrix<float32_t,ROWS,COLS>::diagonal(c);
```

### identity

```cpp
result = Matrix<float32_t,ROWS,COLS>::identity();
```

### transpose

```cpp
result = a.transpose();
```

or

```cpp
transposeTo(result,a);
```

### outer product

```cpp
result = outer(c,c);
```
