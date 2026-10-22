---
id: "ceed-partial-directive-macros-include-conventions"
type: "concept"
domain: "test"
title: "Partial Directive Macros: `#include` conventions"
summary: "The MODULE macros each expand to a string literal that names a generated header file. This means you use them as the argument to #include:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/partials/directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/#include-conventions"
license: "MIT"
mode: "V"
---

The `_MODULE` macros each expand to a **string literal** that names a
generated header file. This means you use them as the argument to `#include`:

```c
// Must come first -- defines all Partial macros
#include "ceedling.h"

#include TEST_PARTIAL_*_MODULE(sensor)
// ↑ Expands to: #include "ceedling_partial_sensor_impl.h"
```

A `TEST_PARTIAL_*_MODULE` macro always names an implementation header.

```c
#include "ceedling.h"

#include MOCK_PARTIAL_*_MODULE(sensor)
// ↑ Expands to: #include "mock_ceedling_partial_sensor_interface.h"
```

A `MOCK_PARTIAL_*_MODULE` macro always names a mockable interface header.

The filters in place of `*` in the macro names — `PUBLIC`, `PRIVATE`, `ALL`, 
and none — tell Ceedling how to initialize internal function lists (that 
can be optionally modified) towards injecting the collected functions into 
each Partial.
