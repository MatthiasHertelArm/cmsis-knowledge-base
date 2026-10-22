---
id: "mlek-coding-standards-and-guidelines-language-usage"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Language usage"
summary: "Include header statements in the following order:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/coding_guidelines.md#language-usage"
license: "Apache-2.0"
mode: "V"
---

- Minimize header `#include` statements: The inclusion of unnecessary headers slows down compilation. If the unnecessary
  header defining this subroutine is included, then it can also hide errors where a function calls a subroutine that it
  must not use.

  Include header statements in the following order:

  - If applicable, begin with the header file corresponding to the current source file,
  - Headers from the same component,
  - Headers from other components,
  - Third-party headers,
  - System headers.

  > **Note:** Leave one blank line between each of these groups for readability. Use quotes for headers from within the
  > same project and angle brackets for third-party and system headers. Do not use paths relative to the current source
  > file, such as `../Header.hpp`. Instead, configure your include paths in the project makefiles.

  For example:

  ```C++
  #include "ExampleClass.hpp"     // Own header

  #include "Header1.hpp"          // Header from same component
  #include "Header1.hpp"          // Header from same component

  #include "other/Header3.hpp"    // Header from other component

  #include <ThirdParty.hpp>       // Third-party headers

  #include <vector>               // System  header

  // [...]
  ```

- Use the template-styled case syntax for C++ casts:

  ```C++
  int a = 100;
  float b = (float)a; // Not OK
  float c = static_cast<float>(a); // OK
  ```

- Use the `const` keyword to declare constants instead of `define`.

- Use `nullptr` instead of `NULL`. C++11 introduced the `nullptr` type to distinguish null pointer constants from the
  integer 0.
