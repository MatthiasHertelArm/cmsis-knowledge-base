---
id: "ceed-valgrind"
type: "concept"
domain: "test"
title: "Valgrind"
summary: "Adds Ceedling tasks to run test executables under [Valgrind] memory error detection to help find memory leaks, invalid memory accesses, and use-after-free bugs in your C code."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/"
license: "MIT"
mode: "V"
---

Adds Ceedling tasks to run test executables under [Valgrind] memory error
detection to help find memory leaks, invalid memory accesses, and
use-after-free bugs in your C code.

The Valgrind plugin creates a duplicate test build with `valgrind:` 
command line plugin tasks. [This is intentional and needed](https://throwtheswitch.github.io/Ceedling/plugins/valgrind/index.md#understanding-plugin-build-duplication).

!!! note
    A `valgrind:` task is a [delta build](https://throwtheswitch.github.io/Ceedling/plugins/valgrind/../getting-started/builds.md).
    This plugin maintains its own dependency cache. A test executable will be 
    rebuilt the first time you run a `valgrind:` build.

---
