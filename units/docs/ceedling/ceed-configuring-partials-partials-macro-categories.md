---
id: "ceed-configuring-partials-partials-macro-categories"
type: "concept"
domain: "test"
title: "Configuring Partials: Partials macro categories"
summary: "See the Partials Macros Reference for the complete listing."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/partials/configuration.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/#partials-macro-categories"
license: "MIT"
mode: "V"
---

See the [Partials Macros Reference](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/../../reference/partials-macros.md) for the complete listing.

### [Module selection](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/../../reference/partials-macros.md#module-selection-macros)

`TEST_PARTIAL_*_MODULE(module)` / `MOCK_PARTIAL_*_MODULE(module)`

Used as the argument to an `#include` directive to select which functions from a module 
are gathered into a Test Partial or Mock Partial and establish the base function set.
These macros also expand into the unique names of the generated Partials header files.

### [Function list configuration](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/../../reference/partials-macros.md#function-list-configuration-macros)

`TEST_PARTIAL_CONFIG(module, func...)` / `MOCK_PARTIAL_CONFIG(module, func...)`

Statements (not `#include` arguments) that add or subtract individual functions
from the base set established by the module selection macro.

### [Static variable access](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/../../reference/partials-macros.md#promoted-static-variable-access)

!!! note
    Module-scope static variables are automatically `extern`ed in a generated Partial
    and can be accessed directly in your test cases.

`PARTIAL_LOCAL_VAR(function_name, variable_name)`

Accesses a function-scoped `static` variable that Ceedling has promoted to
module scope in a generated Partial.
