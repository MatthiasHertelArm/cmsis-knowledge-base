---
id: "ceed-valgrind-plugin-overview"
type: "concept"
domain: "test"
title: "Valgrind: Plugin overview"
summary: "The Valgrind plugin integrates [Valgrind] dynamic analysis into Ceedling, building and then running test executables under Valgrind’s Memcheck tool."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#plugin-overview"
license: "MIT"
mode: "V"
---

!!! note "Linux only"
    Valgrind runs on Linux and other Unix-like systems. It is not available
    on Windows or macOS (ARM).

The Valgrind plugin integrates [Valgrind] dynamic analysis into Ceedling,
building and then running test executables under Valgrind’s Memcheck tool.

The plugin provides two invocation modes mirroring standard `test:` tasks.

- **Whole test suite**: By running `ceedling valgrind:all`, all test
  executables are built and then each is run under Valgrind. A separate log
  file is produced for each test executable in `build/artifacts/valgrind/`.
- **Single test file**: By running `ceedling valgrind:<filename>`, a single
  test executable is built and run under Valgrind, producing one log file.

The plugin triggers standard `test` task builds but hands each test fixture
executable off to Valgrind along with configurable arguments.

By default the build runs all test binaries to completion and is marked as
failed if any Valgrind memory errors are found. The optional `:fail_build:`
setting can be set to `false` to log errors without failing the build.
