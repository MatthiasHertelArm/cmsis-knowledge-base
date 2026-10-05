---
id: "dsp-vector"
type: "concept"
domain: "optimization"
title: "Vector"
summary: "The use of vectors has been explained in @ref dsppp_vector_example \"example with vector operations\" and focusing on float32_t."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/vector.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/vector.md"
license: "Apache-2.0"
mode: "V"
---

The use of vectors has been explained in @ref dsppp_vector_example "example with vector operations" and focusing on `float32_t`.

The vector template is defined as:

```cpp
template<typename P,
         int L=DYNAMIC,
         template<int> typename Allocator = TMP_ALLOC>
struct Vector:Vector_Base<P>
```

* `P` is the datatype of vector elements
* `L` is the static length of the vector (length known at build time). `L<0` when the length is dynamic and not known at build time. It is the default value.
* `Allocator` is the memory allocator. By default it is `TMP_ALLOC` that you can redefine since it is a macro
* `Vector_Base<P>` is providing the storage. A vector owns its storage buffer.
