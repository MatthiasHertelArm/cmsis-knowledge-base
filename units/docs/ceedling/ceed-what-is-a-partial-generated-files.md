---
id: "ceed-what-is-a-partial-generated-files"
type: "concept"
domain: "test"
title: "What Is a Partial?: Generated files"
summary: "Ceedling uses CMock to generate mocks from Partials interface header files just as it does for any other mockable header files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/partials/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/overview/#generated-files"
license: "MIT"
mode: "V"
---

| Partial | Purpose | Generated filename pattern |
|---|---|---|
| Testable header | 

- Declares functions
- `extern`s variables | `ceedling_partial_<module>_impl.h` |
| Testable source | 

- Defines functions
- Defines `static`-less variables | `ceedling_partial_<module>_impl.c` |
| Mockable header | 

- Declares function signatures | `ceedling_partial_<module>_interface.h` |

Ceedling uses CMock to generate mocks from Partials interface header files
just as it does for any other mockable header files.

!!! danger "Do not directly access generated Partials files"
    You as the test author will never directly interact with generated 
    Partials C files. Do not modify these generated files or 
    incorporate them into your tests except with the accompanying macros.
