---
id: "ceed-build-directive-macros-overview-of-build-directive-macros"
type: "concept"
domain: "test"
title: "Build Directive Macros: Overview of Build Directive Macros"
summary: "Ceedling supports a small number of build directive macros. At present, these macros are only for use in test files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/#overview-of-build-directive-macros"
license: "MIT"
mode: "V"
---

Ceedling supports a small number of build directive macros. At present,
these macros are only for use in test files.

By placing these macros in your test files, you may control aspects of an 
individual test executable’s build from within the test file itself.

These macros are actually defined in Unity, but they evaluate to empty 
strings. That is, the macros do nothing and only serve as text markers for 
Ceedling to parse. But, by placing them in your test files they 
communicate instructions to Ceedling when scanned at the beginning of a 
test build.

**_Notes:_**

- Since these macros are defined in _unity.h_, it’s essential to 
  `#include "unity.h"` before making use of them in your test file. 
  Typically, _unity.h_ is referenced at or near the top of a test file
  anyhow, but this is an important detail to call out.
- **`TEST_SOURCE_FILE()` and `TEST_INCLUDE_PATH()`, new in Ceedling 
  1.0.0, are incompatible with enclosing conditional compilation C 
  preprocessing statements.** See
  [Ceedling’s preprocessing documentation](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives/conventions.md#preprocessing-gotchas) 
  for more details.
