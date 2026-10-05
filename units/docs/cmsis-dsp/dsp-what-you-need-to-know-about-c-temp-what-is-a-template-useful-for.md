---
id: "dsp-what-you-need-to-know-about-c-temp-what-is-a-template-useful-for"
type: "concept"
domain: "optimization"
title: "What you need to know about C++ templates: What is a template useful for ?"
summary: "Without unrolling, the scalar implementation is the same but is duplicated (two different source files to maintain although they are nearly the same)."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/template.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/template.md#what-is-a-template-useful-for"
license: "Apache-2.0"
mode: "V"
---

In CMSIS-DSP, you have functions like:

* `arm_add_f32`
* `arm_add_f64`

Without unrolling, the scalar implementation is the same but is duplicated (two different source files to maintain although they are nearly the same).

One could try to reuse the same source for both functions using C preprocessor. But we would still have two different functions with different names at the end (both generated from the same C + C preprocessor macros)

With C++ templates, we can achieve the same result in a better way since the C++ compiler will check the templates and typecheck them. In addition to that, both functions can share the same name.

With C++ template, we could have a *generic* function `arm_add` taking as argument a pointer `T *pSrc` where `T` is a type variable !

When the function is used with a `float32_t *`, the compiler would generate code for a function using `float32_t`.

And if the function is used with a `float64_t *`, the compiler would generate code for a function using `float64_t`.

The generic `arm_add` source code is a template used to generate different implementations. It is like a code generator.

And if the compiler is unable to generate an implementation because the type variable `T` is replaced by a type with no addition operator, then it would be detected by the compiler.

Note that in C++, you can also use overloading of functions. They'll use the same name (but different arguments) but they won't share the same source code.
