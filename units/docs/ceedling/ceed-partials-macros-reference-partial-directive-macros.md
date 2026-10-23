---
id: "ceed-partials-macros-reference-partial-directive-macros"
type: "concept"
domain: "test"
title: "Partials Macros Reference: Partial directive macros"
summary: "These macros expand to a string literal that names a generated header file to be used with #include. #include \"ceedling.h\" must precede their use."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/reference/partials-macros.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/partials-macros/#partial-directive-macros"
license: "MIT"
mode: "V"
---

!!! tip
    For detailed usage guidance, conventions, and examples, see [Partial Directive Macros](https://throwtheswitch.github.io/Ceedling/reference/partials-macros/../testing-guide/partials/directives.md).

### Module selection macros

#### Test Partials macros

These macros expand to a string literal that names a generated header
file to be used with `#include`. `#include "ceedling.h"` must precede
their use.

* **`TEST_PARTIAL_ALL_MODULE(module)`**
Select all functions in the module to be testable by Partial.
* **`TEST_PARTIAL_ALL_MODULE_AT(dir, module)`**
Select all functions in the module at `dir` to be testable by Partial.
* **`TEST_PARTIAL_PUBLIC_MODULE(module)`**
Select all public (non-`static`, non-`inline`) functions in the module to be testable by Partial.
* **`TEST_PARTIAL_PUBLIC_MODULE_AT(dir, module)`**
Select all public (non-`static`, non-`inline`) functions in the module at `dir` to be testable by Partial.
* **`TEST_PARTIAL_PRIVATE_MODULE(module)`**
Select all private (`static` and `inline`) functions in the module to be testable by Partial.
* **`TEST_PARTIAL_PRIVATE_MODULE_AT(dir, module)`**
Select all private (`static` and `inline`) functions in the module at `dir` to be testable by Partial.
* **`TEST_PARTIAL_MODULE(module)`**
Begin with an empty function set to be testable by Partial; functions must be added explicitly via `TEST_PARTIAL_CONFIG`.
* **`TEST_PARTIAL_MODULE_AT(dir, module)`**
Begin with an empty function set to be testable by Partial for the module at `dir`; functions must be added explicitly via `TEST_PARTIAL_CONFIG_AT`.

`TEST_PARTIAL_*` macros expand to an implementation header filename.

#### Mock Partials macros

* **`MOCK_PARTIAL_ALL_MODULE(module)`**
Select all functions in the module to be mockable by Partial.
* **`MOCK_PARTIAL_ALL_MODULE_AT(dir, module)`**
Select all functions in the module at `dir` to be mockable by Partial.
* **`MOCK_PARTIAL_PUBLIC_MODULE(module)`**
Select all public (non-`static`, non-`inline`) functions in the module to be mockable by Partial.
* **`MOCK_PARTIAL_PUBLIC_MODULE_AT(dir, module)`**
Select all public (non-`static`, non-`inline`) functions in the module at `dir` to be mockable by Partial.
* **`MOCK_PARTIAL_PRIVATE_MODULE(module)`**
Select all private (`static` and `inline`) functions in the module to be mockable by Partial.
* **`MOCK_PARTIAL_PRIVATE_MODULE_AT(dir, module)`**
Select all private (`static` and `inline`) functions in the module at `dir` to be mockable by Partial.
* **`MOCK_PARTIAL_MODULE(module)`**
Begin with an empty function set to be mockable by Partial; functions must be added explicitly via `MOCK_PARTIAL_CONFIG`.
* **`MOCK_PARTIAL_MODULE_AT(dir, module)`**
Begin with an empty function set to be mockable by Partial for the module at `dir`; functions must be added explicitly via `MOCK_PARTIAL_CONFIG_AT`.

`MOCK_PARTIAL_*` macros expand to a mockable interface header filename.

### Function list configuration macros

These macros are statements (not to be used with `#include` directives) 
that refine the set of functions selected by the use of any module selection 
macro above.

* **`TEST_PARTIAL_CONFIG(module, func...)`**
Add or subtract functions from the test Partial’s function set.
* **`TEST_PARTIAL_CONFIG_AT(dir, module, func...)`**
Add or subtract functions from the test Partial’s function set for the module at `dir`.
* **`MOCK_PARTIAL_CONFIG(module, func...)`**
Add or subtract functions from the mock Partial’s function set.
* **`MOCK_PARTIAL_CONFIG_AT(dir, module, func...)`**
Add or subtract functions from the mock Partial’s function set for the module at `dir`.

### Function list addition and subtraction

!!! tip
    For the full rules on which additions and subtractions are valid with 
    each `*_MODULE` variant, see
    [Partial directive macros](https://throwtheswitch.github.io/Ceedling/reference/partials-macros/../testing-guide/partials/directives.md#partials-function-list-configuration-macros).

* Prefix a function name with `-` (`-func`) to exclude it from the Partial.
* Use no prefix or `+` (`+func`) to include it.

A function explicitly added to one side is automatically removed from the 
complementary Partial to prevent duplicate symbol linker errors.

---
