---
id: "ceed-what-is-a-partial-partials-creation-step-by-step"
type: "concept"
domain: "test"
title: "What Is a Partial?: Partials creation step-by-step"
summary: "What Is a Partial?: Partials creation step-by-step"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/overview/#partials-creation-step-by-step"
license: "MIT"
mode: "V"
---

When creating a Partial, Ceedling:

1. Runs your source code under test through the preprocessor to:
    1. Handle `#ifdef` blocks and strip comments.
    1. Collect the `#include` directives.
    1. Expand decorator macros (e.g. `STATICINLINE`) in function signatures.
1. Lexes the code under test to collect its individual C language elements
   (e.g. `typedef`s, macros, functions, variables, etc.).
1. Generates a new set of C files in a _partials/_ build directory. The 
   contents of these new files are:
    1. Reconstructed with the `#include` directives from (1) and elements 
       from (2).
    1. Reorganized and slightly altered so the C elements can be accessed by 
       assertions and mocks in your test cases. Functions are stripped of 
       `static` and `inline`. Variables are stripped of `static` and `extern`ed.
1. Structures the test build to omit the original source file from the 
   resulting test executable. Generated Partials are self-sufficient stand-ins 
   for the original C code from which the Partials are derived.
1. Maps the reorganized functions in generated Partials back to the 
   original source module's filepath and line numbers (using GCC's `#line` 
   directive) for correct test coverage reporting.

!!! tip "Walk-through example"
    See [Partials Walk-Through Example](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/overview/example.md) for a complete end-to-end
    demonstration of Test Partials and Mock Partials.
