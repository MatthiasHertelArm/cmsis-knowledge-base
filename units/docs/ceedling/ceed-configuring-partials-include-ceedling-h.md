---
id: "ceed-configuring-partials-include-ceedling-h"
type: "concept"
domain: "test"
title: "Configuring Partials: `#include \"ceedling.h\"`"
summary: "Every test file that uses Partials must include ceedling.h before any Partial directive macros:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/partials/configuration.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/#include-ceedling-h"
license: "MIT"
mode: "V"
---

Every test file that uses Partials must include `ceedling.h` before any Partial
directive macros:

```c
#include "unity.h"
#include "ceedling.h" // Required -- defines all Partial directive macros
```

`ceedling.h` defines the `TEST_PARTIAL_*`, `MOCK_PARTIAL_*`, `*_CONFIG`, and
`PARTIAL_LOCAL_VAR()` macros. Without this include, the macros are undefined.
