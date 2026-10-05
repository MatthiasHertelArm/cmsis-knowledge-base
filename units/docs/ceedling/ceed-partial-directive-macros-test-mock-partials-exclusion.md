---
id: "ceed-partial-directive-macros-test-mock-partials-exclusion"
type: "concept"
domain: "test"
title: "Partial Directive Macros: `TEST_` / `MOCK_` Partials exclusion"
summary: "Any function explicitly added on one side via a Partial CONFIG macro is automatically removed from the complementary function list (if it exists)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/partials/directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/#test-mock-partials-exclusion"
license: "MIT"
mode: "V"
---

Any function explicitly added on one side via a Partial `_CONFIG` macro is 
**automatically removed** from the complementary function list (if it exists).
This prevents the same function from accidentally appearing both in a Partial 
implementation and Partial mock, which would produce a duplicate symbol linker 
error.

```c
// `_InternalHelper()` added to the test side
// while automatically removed from the mock side.
#include TEST_PARTIAL_PRIVATE_MODULE(mymodule)
TEST_PARTIAL_CONFIG(mymodule, _InternalHelper)

// `_InternalHelper()` will NOT appear in the mock.
#include MOCK_PARTIAL_PUBLIC_MODULE(mymodule)
```
