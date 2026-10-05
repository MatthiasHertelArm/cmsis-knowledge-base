---
id: "mlek-coding-standards-and-guidelines-introduction"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Introduction"
summary: "This document presents some standard coding guidelines to be followed for contributions to this repository. Most of the code is written in C++, but there is also some written in C."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/coding_guidelines.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document presents some standard coding guidelines to be followed for contributions to this repository. Most of the
code is written in C++, but there is also some written in C. There is a clear C/C++ boundary at the Hardware Abstraction
Layer (HAL). Both of these languages follow different naming conventions within this repository, by design, to:

- Have clearly distinguishable C and C++ sources.
- Make cross language function calls stand out. These are mainly C++ function calls to the HAL functions, that were
  written in C.

However, because we also issue function calls to third-party APIs, and they are not guaranteed to follow these
conventions, the intended outcome could be different for every case.
