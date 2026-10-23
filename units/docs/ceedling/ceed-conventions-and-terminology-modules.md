---
id: "ceed-conventions-and-terminology-modules"
type: "concept"
domain: "test"
title: "Conventions and Terminology: Modules"
summary: "In Ceedling Partials, a module is a C source file, a C header file, or a matched source + header pair sharing the same base filename. The base filename — without its extension — is the module name."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/conventions/#modules"
license: "MIT"
mode: "V"
---

In Ceedling Partials, a _module_ is a C source file, a C header file, or a matched
source + header pair sharing the same base filename. The base filename —
without its extension — is the _module name_.

| Files present | Module name |
|---|---|
| `sensor.c` and `sensor.h` | `sensor` |
| `sensor.h` only | `sensor` |
| `sensor.c` only | `sensor` |

When both a source file and a header file share a name, Ceedling treats them
as a single unit. Both files are read when generating a Partial. When only 
one file is present, only that file is read.

All Partial directive macros take a module name — a bare filename stem with no
extension and no quotation marks:

```c
// Module name: 'sensor'
// Not "sensor.c" (no quotation marks) and not "path/to/sensor" (see below)
#include TEST_PARTIAL_PRIVATE_MODULE(sensor)
```

### Distinguishing a module by directory

A module name without path information, can ambiguously names multiple files 
whenever a project holds multiple modules of the same name in different 
directories. The `_AT` variant of every `_MODULE` macro takes that module's 
directory as a separate first argument:

```c
// Two sensors, each with its own Calibration module
#include TEST_PARTIAL_PRIVATE_MODULE_AT(sensors/soil, Calibration)
#include TEST_PARTIAL_PRIVATE_MODULE_AT(sensors/light, Calibration)
```

The directory is matched against the trailing end of a real file's path, so you
supply only as much of it as it takes to distinguish the module you mean.
`sensors/soil` and `soil` both reach `src/sensors/soil/Calibration.c` as long as
no other module's path also ends that way.

The directory is written as bare text, like the module name — no quotation marks
— and it is relative, never absolute. A Partial is generated relative to the
project root.

The directory must be the macro's own first argument. Writing a path inside the
module argument of a bare macro instead does not work, for reasons covered in
[Rules for the directory argument](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/conventions/directives.md#rules-for-the-directory-argument).

Naming a directory is optional. A bare module name using a non-`_AT` macros is
sufficient when no duplicate modules exist. And, when multiple modules are 
present, it continues to resolve the way a compiler's own header search does — 
the first match among the ordered search paths wins.

Naming two same-named modules by directory lets one test file **test** both, and
**mock** both, as covered under [Naming a module by directory](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/conventions/directives.md#naming-a-module-by-directory).

!!! tip "When Ceedling cannot tell two modules apart"
    A bare module name matching more than one module is reported with the
    candidates Ceedling found and the `_AT` macro that resolves it. The message
    names the modules as you would write them, not the generated files.
