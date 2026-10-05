---
id: "dsp-vector-vectorview"
type: "concept"
domain: "optimization"
title: "Vector: VectorView"
summary: "A vector view is a virtual vector : a view of a vector."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/vector.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/vector.md#vectorview"
license: "Apache-2.0"
mode: "V"
---

A vector view is a virtual vector : a view of a vector.

One can define a `VectorView` with:

```cpp
auto subD = d.sub(2);
```

This is creating a virtual vector starting at index `2` (3rd element) of vector `d`.

You can then operate with this virtual vector:

```cpp
subD = subD + 2.0f;
```

If you display the vector `d`, you'll see that `2.0f` has been added to all elements starting from the 2nd one.

`VectorView` do not own their memory. It is owned by the original vector. 

If you write:

```cpp
x = y
```

and `x` and `y` are `VectorView`, no copy will occur. `x` will just reference the same data as `y`. If you want to copy you have to be explicit and write:

```cpp
x = copy(y)
```

It is advised to always use the `copy` operator (even with normal vectors).

Virtual vectors can have a stride:

```cpp
d.sub<2>(1) = 0.0f;
```

This line sets the odd elements of the vector to `0.0f`. It is creating a virtual vector with stride `2` and starting at index `1` of first vector.

Then, all elements of this virtual vector are set to `0.0f`.

The `sub` API is:

```cpp
template<int S=1>
VectorView<P,S> sub(const index_t start=0,const index_t stop=L)
```

You can define:

* The stride `S` : statically known and by default `1`.
* The start of the view (`0` by default)
* The end of the view (`L` by default : the length known at build time). Note that it is the first index **after** the end of the vector.
