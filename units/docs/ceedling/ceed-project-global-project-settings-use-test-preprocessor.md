---
id: "ceed-project-global-project-settings-use-test-preprocessor"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:use_test_preprocessor`"
summary: "This option allows Ceedling to work with test files that contain tricky conditional compilation statements (e.g. #ifdef) as well as mockable header files containing conditional preprocessor directives and/or macros."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#use-test-preprocessor"
license: "MIT"
mode: "V"
---

This option allows Ceedling to work with test files that contain tricky
conditional compilation statements (e.g. `#ifdef`) as well as mockable header
files containing conditional preprocessor directives and/or macros.

See the [documentation on test preprocessing][test-preprocessing] for more.

!!! note
    With any preprocessing enabled, the `gcc` & `cpp` tools must exist in an
    accessible system search path.

[test-preprocessing]: ../../testing-guide/conventions.md#test-preprocessing

* `:none` disables preprocessing.
* `:all` enables preprocessing for all mockable header files and test C files.
* `:mocks` enables only preprocessing of header files that are to be mocked.
* `:tests` enables only preprocessing of your test files.

!!! note
    Enabling Partials (`:project` ↳ `:use_partials`) sets this option to `:all`,
    whatever value you give it, since Partials require preprocessing.

**Default**: `:none`
