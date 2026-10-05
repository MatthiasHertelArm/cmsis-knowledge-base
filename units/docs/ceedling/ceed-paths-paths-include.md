---
id: "ceed-paths-paths-include"
type: "concept"
domain: "test"
title: "`:paths`: `:paths` ↳ `:include`"
summary: "See these two important discussions to fully understand your options for header file search paths:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#paths-include"
license: "MIT"
mode: "V"
---

See these two important discussions to fully understand your options for header
file search paths:

* [Configuring Your Header File Search Paths][header-file-search-paths]
* [`TEST_INCLUDE_PATH(...)` build directive macro][test-include-path-macro]

[header-file-search-paths]: ../../testing-guide/conventions.md#test-build-search-paths
[test-include-path-macro]: ../../testing-guide/build-directives.md#test_include_path

This set of paths specifies the locations of your header files. If your header
files are intermixed with source files, you must duplicate some or all of your
`:paths` ↳ `:source` entries here.

In its simplest use, your include paths list can be exhaustive. That is, you
list all path locations where your project’s header files reside in this
configuration list.

However, if you have a complex project or many, many include paths that create
problematically long search paths at the compilation command line, you may treat
your `:paths` ↳ `:include` list as a base, common list. Having established that
base list, you can then extend it on a test-by-test basis with use of the
`TEST_INCLUDE_PATH(...)` build directive macro in your test files.

**Default**: `[]` (empty)
