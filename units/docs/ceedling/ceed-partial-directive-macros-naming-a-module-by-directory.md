---
id: "ceed-partial-directive-macros-naming-a-module-by-directory"
type: "concept"
domain: "test"
title: "Partial Directive Macros: Naming a module by directory"
summary: "Every MODULE and CONFIG macro has an AT variant that takes the module’s directory as a separate first argument."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/#naming-a-module-by-directory"
license: "MIT"
mode: "V"
---

Every `_MODULE` and `_CONFIG` macro has an `_AT` variant that takes the module’s
directory as a separate first argument. Use it when a module name alone is
ambiguous — that is, when your project holds two modules of the same name in
different directories.

```c
#include "ceedling.h"

#include TEST_PARTIAL_PRIVATE_MODULE_AT(sensors/soil, Calibration)
// ↑ Expands to: #include "sensors/soil/ceedling_partial_Calibration_impl.h"
```

The generated filename keeps the directory and takes its prefix on the basename
(mirroring your source tree inside the build directory). Two same-named modules
therefore generate two distinct files rather than overwriting one another.

| Macro family | Bare form | Directory-qualified form |
|---|---|---|
| Test module | `TEST_PARTIAL_*_MODULE(module)` | `TEST_PARTIAL_*_MODULE_AT(dir, module)` |
| Mock module | `MOCK_PARTIAL_*_MODULE(module)` | `MOCK_PARTIAL_*_MODULE_AT(dir, module)` |
| Test function list | `TEST_PARTIAL_CONFIG(module, ...)` | `TEST_PARTIAL_CONFIG_AT(dir, module, ...)` |
| Mock function list | `MOCK_PARTIAL_CONFIG(module, ...)` | `MOCK_PARTIAL_CONFIG_AT(dir, module, ...)` |

!!! tip "Two same-named modules in one test file"
    `TEST_PARTIAL_*_MODULE_AT()` and `MOCK_PARTIAL_*_MODULE_AT()` both work for two
    modules sharing a basename.

A `_CONFIG_AT` macro must name the same directory as the `_MODULE_AT` macro it
refines. The directory and module together identify which Partial a function
list belongs to.

```c
#include TEST_PARTIAL_MODULE_AT(sensors/soil, Calibration)
TEST_PARTIAL_CONFIG_AT(sensors/soil, Calibration, Soil__Clamp)
```

### How much path to supply

The directory is matched against the trailing end of a real file’s path. So,
supply only as much as it takes to distinguish the module you mean. Given
`src/sensors/soil/Calibration.c`, both of the following could reach it.
The amount of path information to provide changes depending on the depth of
duplicated subdirectories in path names.

```c
#include TEST_PARTIAL_PRIVATE_MODULE_AT(sensors/soil, Calibration)
#include TEST_PARTIAL_PRIVATE_MODULE_AT(soil, Calibration)
```

A Partials path that matches no file triggers a breaking test build early in
the build rather than a missing-include failure later in the build.

### Rules for the directory argument

* Written as bare text, like the module name. No quotation marks.
* Relative, never absolute. A Partial is generated relative to the project root.
* Optional. A bare module name using non`_AT` macros is entirely acceptable for
  modules without duplicated names elsewhere in your project.
* Supplied as the macro’s own first argument, never inside the module argument.

!!! warning "A path belongs in the directory argument, not the module argument"
    The directory must be the macro’s first argument. A path written inside the
    module argument of a bare macro does not work:

    ```c
    // Wrong
    #include TEST_PARTIAL_PRIVATE_MODULE(sensors/soil/Calibration)

    // Right
    #include TEST_PARTIAL_PRIVATE_MODULE_AT(sensors/soil, Calibration)
    ```

!!! note "A bare module name resolves like the compiler’s own search"
    Without a directory, Ceedling selects the first match among your ordered
    `:paths` search paths, the same way a compiler resolves a header. That is
    unambiguous in most projects and only needs an `_AT` macro when two modules
    share a name.
