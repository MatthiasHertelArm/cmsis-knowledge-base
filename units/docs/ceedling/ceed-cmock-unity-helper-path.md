---
id: "ceed-cmock-unity-helper-path"
type: "concept"
domain: "test"
title: "`:cmock`: `:unity_helper_path`"
summary: "A Unity helper is a simple header file used by convention to support your specialized test case needs. For example, perhaps you want a Unity assertion macro for the contents of a struct used throughout your project."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/cmock.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/#unity-helper-path"
license: "MIT"
mode: "V"
---

A Unity helper is a simple header file used by convention to support your
specialized test case needs. For example, perhaps you want a Unity assertion
macro for the contents of a struct used throughout your project. Write the macro
you need in a Unity helper header file and `#include` that header file in your
test file.

When a Unity helper is provided to CMock, it takes on more significance, and
more magic happens. CMock parses Unity helper header files and uses macros of a
certain naming convention to extend CMock’s handling of mocked parameters.

See the [Unity and CMock documentation](https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/../../testing-guide/frameworks.md) 
for more details.

`:unity_helper_path` may be a single string or a list. Each value must be a
relative path from your Ceedling working directory to a Unity helper header file
(these are typically organized within containing Ceedling `:paths` ↳ `:support`
directories).

**Default**: `[]` (empty)
