---
id: "dsp-matrix"
type: "concept"
domain: "optimization"
title: "Matrix"
summary: "Matrixes can be used similarly to vectors:"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/matrix.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/matrix.md"
license: "Apache-2.0"
mode: "V"
---

Matrixes can be used similarly to vectors:

```cpp
Matrix<float32_t,ROWS,COLS> a;
Matrix<float32_t,ROWS,COLS> b;
```

If the dimensions of the matrixes are not known at build time, you would instead write:

```
Matrix<float32_t> a(rows,cols);
Matrix<float32_t> b(rows,cols);
```

Once you have matrixes, you need to initialize them.  A matrix is also a vector, so you can initialize it by indexing into the vector:

```cpp
for(std::size_t i=0;i<ROWS*COLS;i++)
{
      a[i] = float32_t(i);
}
```

You can also use a bidimensional indexing:

```cpp
for(std::size_t row=0; row<ROWS; row++)
{
   for(std::size_t col=0; col<COLS; col++)
   {
            b(row,col) = float32_t(row*col);
   }
}
```

Once you have initialized matrixes, you can operate on them:

```cpp
Matrix<float32_t,ROWS,COLS> result = a * a + b;
```

The operators `+` and `*` are merged into the loop. `*` is the element-wise multiply. For eagerly evaluated vector / matrix products you should use the operator `dot`.

Note that fusion of operators will not work with `dot(Matrix, Matrix)` or
`dot(Matrix, Vector)`, since both operations return an owning, eagerly
evaluated result. Vector dot products return a scalar.

For a matrix times vector product that must be fused with vector operations,
use the lazy `matvec` operator:

```cpp
result += matvec(matrix, vector);
```

`matvec` returns a non-owning expression. In this example, the matrix-vector
product is accumulated directly into `result` without allocating a temporary
vector. The operands must remain alive until the complete expression is
evaluated. Use `dot(matrix, vector)` when an owning result is required.
