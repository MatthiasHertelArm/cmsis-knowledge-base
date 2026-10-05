---
id: "ceed-test-runner-test-runner-cmdline-args"
type: "concept"
domain: "test"
title: "`:test_runner`: `:test_runner` ↳ `:cmdline_args`"
summary: "Before Ceedling 1.0.0, the test runner option :cmdline_args was needed for certain advanced test suite features. This option is still needed, but Ceedling now automatically sets it for you in the scenarios requiring it."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/test-runner.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-runner/#test-runner-cmdline-args"
license: "MIT"
mode: "V"
---

Before Ceedling 1.0.0, the test runner option `:cmdline_args` was needed 
for certain advanced test suite features. This option is still needed, 
but Ceedling now automatically sets it for you in the scenarios requiring it.

!!! note "Environment limitations"
    Be aware that `:cmdline_args` works well in desktop, native testing but 
    is generally unsupported by emulators running test executables.
    
    The idea of command line arguments passed to an executable is generally 
    only possible with desktop command line terminals.
