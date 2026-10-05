---
id: "ceed-project-global-project-settings-test-threads"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:test_threads`"
summary: "The behavior of and values for :test_threads are identical to :compile_threads with one exception."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#test-threads"
license: "MIT"
mode: "V"
---

The behavior of and values for `:test_threads` are identical to
`:compile_threads` with one exception.

`test_threads:` specifically controls the number of threads used to run the
test executables comprising a test suite.

Why the distinction from `:compile_threads`? Some test suite builds rely not on
native executables but simulators running cross-compiled code. Some simulators
are limited to running only a single instance at a time. Thus, with this and
the previous setting, it becomes possible to parallelize nearly all of a test
suite build while still respecting the limits of certain simulators depended
upon by test executables.

**Default**: 1
