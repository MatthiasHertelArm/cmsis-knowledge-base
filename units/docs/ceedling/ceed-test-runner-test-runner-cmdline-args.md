---
id: "ceed-test-runner-test-runner-cmdline-args"
type: "concept"
domain: "test"
title: "`:test_runner`: `:test_runner` ↳ `:cmdline_args`"
summary: "Enables command line arguments in generated test runners. Two Ceedling features select test cases through these arguments, and Ceedling enables this option automatically, with a notice, whenever either is in use:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/test-runner.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-runner/#test-runner-cmdline-args"
license: "MIT"
mode: "V"
---

Enables command line arguments in generated test runners. Two Ceedling 
features select test cases through these arguments, and Ceedling enables 
this option automatically, with a notice, whenever either is in use:

* `:project` ↳ `:use_backtrace` set to anything other than `:none`. 
  Backtraces rerun test cases by name.
* The command line test case filters `--test-case` and `--exclude_test_case`.

**Default**: FALSE

!!! note "Environment limitations"
    Be aware that `:cmdline_args` works well in desktop, native testing but 
    is generally unsupported by emulators running test executables.
    
    The idea of command line arguments passed to an executable is generally 
    only possible with desktop command line terminals.
