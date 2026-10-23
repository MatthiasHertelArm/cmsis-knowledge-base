---
id: "mlek-coding-standards-and-guidelines-language-version"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Language version"
summary: "The project was originally implemented to conform to the C++14 standard for C++ code and the C99 standard for C code."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/coding_guidelines.md#language-version"
license: "Apache-2.0"
mode: "V"
---

The project was originally implemented to conform to the `C++14` standard for C++ code and the `C99` standard
for C code.
However, the project is now compiled with the `C++17` and `C11` standards so we can make use of newer language features.

Software components written in C/C++ may use the language features allowed and is encouraged.
