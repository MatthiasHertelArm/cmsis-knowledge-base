---
id: "ceed-partial-directive-macros"
type: "concept"
domain: "test"
title: "Partial Directive Macros"
summary: "All Partial configuration is expressed through C macros placed in your test file. No separate configuration file is required. The macros require #include \"ceedling.h\" present in the test file above and before their use."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/"
license: "MIT"
mode: "V"
---

!!! note "Documentation convention"
    - `*` is a stand-in or wildcard to refer to all variations of a particular macro type.
    - For brevity, some classes of directive macros are referred to simply by their common
      suffix (e.g `_MODULE` refers to all the macros with this suffix.)

All Partial configuration is expressed through C macros placed
in your test file. No separate configuration file is required. The macros
require `#include "ceedling.h"` present in the test file above and before
their use.

The [Partial `_MODULE` macros](#partials-function-selection-by-macro) accomplish the following:

1. Expand to a filename for the preceding `#include` directive.
1. Provide a module name for Ceedling to process for the resulting Partial.
1. Assemble a base set of functions to test or mock.

The optional Partial `_CONFIG` macros modify the base set of functions 
from (3). Modifying a base set of functions is documented in detail in the
[Partials function list configuration macros](#partials-function-list-configuration-macros)
section.

!!! tip "Configuring Partials"
    For enabling and configuring Partials, see [Configuring Partials](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/configuration.md).
