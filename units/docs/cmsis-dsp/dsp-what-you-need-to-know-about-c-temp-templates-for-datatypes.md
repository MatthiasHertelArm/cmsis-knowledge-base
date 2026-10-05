---
id: "dsp-what-you-need-to-know-about-c-temp-templates-for-datatypes"
type: "concept"
domain: "optimization"
title: "What you need to know about C++ templates: Templates for datatypes"
summary: "C++ templates also apply to structs and classes."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/template.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/template.md#templates-for-datatypes"
license: "Apache-2.0"
mode: "V"
---

C++ templates also apply to structs and classes.

For instance, we could have a template `Vector<T>` and thus different types `Vector<float32_t>`, `Vector<Q15>` ...

There is another aspect of C++ templates that may be surprising : the types can contain numbers. 

For instance, one could have a type
`Vector<float32_t,10>` for a vector of `float` and of length `10`. The length being known at build time.

The types `Vector<float32_t,10>` and `Vector<float32_t,5>` should be considered as different types because they have different lengths. The length is part of the type.

What we said above for code generation applies. For a template algorithm using any kind of vector, the compiler would generate different code for different vector types. The code for a template algorithm using `Vector<float32_t,10>` would be different from the code for `Vector<float32_t,5>` because those two types are different.
