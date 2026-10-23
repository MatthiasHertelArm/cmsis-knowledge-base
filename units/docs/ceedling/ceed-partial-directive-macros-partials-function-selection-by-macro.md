---
id: "ceed-partial-directive-macros-partials-function-selection-by-macro"
type: "concept"
domain: "test"
title: "Partial Directive Macros: Partials function-selection by macro"
summary: "Each test or mock Partial is independently configured by exactly one MODULE macro call. The macro determines the base set of functions that Ceedling collects towards generating a Partial."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/partials/directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/directives/#partials-function-selection-by-macro"
license: "MIT"
mode: "V"
---

Each test or mock Partial is independently configured by exactly
one `_MODULE` macro call. The macro determines the _base set_ of
functions that Ceedling collects towards generating a Partial. Once
the base set of functions is determined, explicit additions or 
subtractions can be applied with `_CONFIG` macros.

This scheme gives you the, test author, full control of which functions
are injected into which type of Partial while avoiding laboriously
listing each function individually.

### Partials base function filters

* `[TEST/MOCK]_PARTIAL_ALL_MODULE()`
* `[TEST/MOCK]_PARTIAL_PUBLIC_MODULE()`
* `[TEST/MOCK]_PARTIAL_PRIVATE_MODULE()`
* `[TEST/MOCK]_PARTIAL_MODULE()`

Each has an `_AT` variant taking the module’s directory, documented in
[Naming a module by directory](#naming-a-module-by-directory). The filter and
the function-list rules below apply identically to both forms.

| Macro | Base set of functions | Additions | Subtractions |
|---:|---|---|---|
| `_ALL_MODULE` | All functions | Forbidden | Any function |
| `_PUBLIC_MODULE` | All public functions | Add private | Remove public |
| `_PRIVATE_MODULE` | All private functions | Add public | Remove private |
| `_MODULE` | Empty | Any function (at least one) | Forbidden |

#### Example base sets of function by filter

| Functions | `ALL` | `PUBLIC` | `PRIVATE` | None |
|---:|---|---|---|---|
| void foo(void) | ✅ | ✅ |  | |
| static void bar(void) | ✅ | | ✅ | |
| int baz(void) | ✅ | ✅ | | |
| inline int oof(int) | ✅ | | ✅ | |

**Notes:**

* `*_PARTIAL_MODULE` requires at least one addition via `*_PARTIAL_CONFIG` 
  (see next section).
* `*_PARTIAL_ALL_MODULE` with no subtractions adds every module function to
  base set of functions.
* Each module can appear in **at most one** `TEST_PARTIAL_*_MODULE` and 
  `MOCK_PARTIAL_*_MODULE` macro within a given test file. Two same-named modules
  in different directories are two modules, and each may have its own pair.

### Partials function list configuration macros

`TEST_PARTIAL_CONFIG` and `MOCK_PARTIAL_CONFIG` refine the base set of functions
filtered by the corresponding `_MODULE` macro. Both `_CONFIG` macros require at 
least one function name argument beyond the module name.

Note that no quotation marks are needed.

```c
TEST_PARTIAL_CONFIG(module, func1, func2, ...)
MOCK_PARTIAL_CONFIG(module, func1, func2, ...)
```

Similar to the convenion in Ceedling‘s `paths:` and `files:` YAML configuration 
sections, each function name argument is treated as an **addition** or a 
**subtraction** depending on an optional prefix character:

| Prefix | Meaning |
|---:|---|
| _(none)_ or `+` | Add this function to the Partial
(`<function>` or `+<function>`) |
| `-` | Exclude this function from the Partial
(`-<function>`) |

```c
TEST_PARTIAL_CONFIG(module, +func1, +func2, -func3)
MOCK_PARTIAL_CONFIG(module,  func1,  func2, -func3)
```

#### Addition & subtraction rules by mode

| Macro | Filter | Subtraction target | Addition target |
|---:|---|---|---|
| `_PUBLIC_MODULE` | Public | Public functions only | Private functions |
| `_PRIVATE_MODULE` | Private | Private functions only | Public functions |
| `_MODULE` | Accumulate | Forbidden | Any function (one required) |
| `_ALL_MODULE` | Deduct | Any function | Forbidden |
