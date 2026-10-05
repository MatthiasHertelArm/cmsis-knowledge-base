---
id: "dsp-what-you-need-to-know-about-c-temp-implicit-parameters"
type: "concept"
domain: "optimization"
title: "What you need to know about C++ templates: Implicit parameters"
summary: "A template can also have implicit parameters."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/template.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/template.md#implicit-parameters"
license: "Apache-2.0"
mode: "V"
---

A template can also have implicit parameters.

For instance one could use `Vector<float32_t>` or `Vector<float32_t,10>`.

In the first case, the length is an implicit parameter with a default value and it is equivalent to writing `Vector<float32_t,DYNAMIC>` where `DYNAMIC` could be a special value (negative for instance) used to tell the compiler that the length of the vector is not known at build time but only at runtime.

Both variants may use totally different implementations. The `DYNAMIC` variant may contain a `length` field in the `struct` definition whereas other variants do not need this field since the length is known at build time.
