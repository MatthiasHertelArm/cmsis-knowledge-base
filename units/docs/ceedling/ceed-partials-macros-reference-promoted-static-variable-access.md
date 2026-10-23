---
id: "ceed-partials-macros-reference-promoted-static-variable-access"
type: "concept"
domain: "test"
title: "Partials Macros Reference: Promoted static variable access"
summary: "Access a function-scoped static variable that Ceedling has promoted to module scope in a generated Partial. The macro expands to the promoted identifier partial<function_name><variable_name>."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/reference/partials-macros.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/partials-macros/#promoted-static-variable-access"
license: "MIT"
mode: "V"
---

!!! tip
    For the full explanation of how Ceedling promotes function-scoped `static` 
    variables to module scope and when to use this macro, see
    [Accessing Static Variables](https://throwtheswitch.github.io/Ceedling/reference/partials-macros/../testing-guide/partials/variables.md).

**`PARTIAL_LOCAL_VAR(function_name, variable_name)`**

Access a function-scoped `static` variable that Ceedling has promoted to
module scope in a generated Partial. The macro expands to the promoted
identifier `partial_<function_name>_<variable_name>`.

- Defined in `ceedling.h`; requires `#include "ceedling.h"` above its use
- Both arguments must be literal C identifiers — not strings or runtime values
- Can appear anywhere a variable name is legal: expressions, assertions,
  assignments
