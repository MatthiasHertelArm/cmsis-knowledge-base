---
id: "ceed-partial-directive-macros-directive-macros-example"
type: "concept"
domain: "test"
title: "Partial Directive Macros: Directive Macros Example"
summary: "Partial Directive Macros: Directive Macros Example"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/partials/directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/#directive-macros-example"
license: "MIT"
mode: "V"
---

```c
// Required before we can use the Partials directive macros
#include "ceedling.h"

// Mock all `static` and/or `inline` functions of `mymodule`
#include MOCK_PARTIAL_PRIVATE_MODULE(mymodule)

// But, remove `InternalHelper()` from the mocks
MOCK_PARTIAL_CONFIG(mymodule, -_InternalHelper)
```

!!! tip "Enable obnoxious level logging to inspect Partials generation"
    Add `--verbosity obnoxious` (or `-v 4`) to your `test:` command line invocation
    for detailed logging of the C extraction and Partials generations for your test
    build. The logged lists of functions and variables can help you fine tune or
    troubleshoot your Partials configuration.
