---
id: "ceed-conventions-and-terminology-modules"
type: "concept"
domain: "test"
title: "Conventions and Terminology: Modules"
summary: "In Ceedling Partials, a module is a C source file, a C header file, or a matched source + header pair sharing the same base filename. The base filename — without its extension — is the module name."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/partials/conventions.md"
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

All Partial directive macros take a module name — a bare filename stem with
no extension, no path, and no quotation marks:

```c
// Module name: 'sensor'
// Not "sensor.c" (no quotation marks) or "path/to/sensor"
#include TEST_PARTIAL_PRIVATE_MODULE(sensor)
```
