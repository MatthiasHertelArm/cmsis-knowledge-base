---
id: "ceed-conventions-and-terminology-public-private-functions"
type: "concept"
domain: "test"
title: "Conventions and Terminology: Public / Private Functions"
summary: "C has no access modifiers. Every function with external linkage is — from the language's perspective — equally visible at link time."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/conventions/#public-private-functions"
license: "MIT"
mode: "V"
---

C has no access modifiers. Every function with external linkage is — from the
language's perspective — equally visible at link time. In the context of
Partials, Ceedling uses the more modern terms _public_ and _private_ to 
describe a practical distinction based on function decorators:

### Private functions

“Private” functions carry one or more of the following keywords anywhere in
their declaration or definition:

* `static`
* `inline`
* `__inline`
* `__inline__`
* `__forceinline`

A `static` function has internal linkage. It is invisible to the linker
outside its containing translation unit, and therefore cannot be called or 
mocked from a test build without special handling. `inline` functions may be 
folded away by the compiler entirely. Partials use decorators to organize
lists of functions for testing and mocking, but the decorators are stripped
in the resulting generated code.

!!! note "Because of preproccesing only the “private” keywords are recognized"
    The preprocesing steps that are part of generating Partials expand any
    macros (e.g. `INLINE` or `STATICINLINE`) to the actual keywords decorating
    function signatures. As such, only the keywords above must be handled.

### Public functions

“Public” functions are everything else — functions with no visibility-
restricting decorator and ordinary external linkage.

This public/private distinction is one set of filters for assembling a list
of functions each `_MODULE` macro selects. The filtering and collection is 
documented in detail in the 
[Partials function-selection by macro](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/conventions/directives.md#partials-function-selection-by-macro) section.
