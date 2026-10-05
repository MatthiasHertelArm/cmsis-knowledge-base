---
id: "dsp-matrix-vectorview"
type: "concept"
domain: "optimization"
title: "Matrix: VectorView"
summary: "We can create virtual vectors which are view of some slices of the matrix."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/matrix.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/matrix.md#vectorview"
license: "Apache-2.0"
mode: "V"
---

We can create virtual vectors which are view of some slices of the matrix.

### Row vector

To set the second row to `0.0f`, you can do:

```
result.row(1) = 0.0f;
```

To set the odd elements of the 3rd row to `0.0f` we can do:

```
result.row<2>(2,1) = 0.0f;
```

The first argument `2` is the row number (starting from `0`).

The second argument `1` is where is the row we start the view : element `1`.

`<2>` is the stride known at built time.

The `row` API is:

```cpp
template<int S=1>
VectorView<P,S> row(const index_t i,const index_t start=0,const index_t stop=C)
   
```

`stop` is the index of the first element **after** the end of the view.

`i` is the row index

### Column vector

There is a similar API for columns.

Let's set the odd elements of columns 3 to `5.0f`:

```
result.col<2>(2,1) = 5.0f;
```
