---
id: "ceed-sanitize-plugin-overview"
type: "concept"
domain: "test"
title: "Sanitize: Plugin overview"
summary: "Enabling this plugin on a platform without sanitizers does not affect your other builds. Only a sanitize: task requires them."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#plugin-overview"
license: "MIT"
mode: "V"
---

!!! note "Linux and macOS"
    The sanitizers run on Linux with GCC or Clang and on macOS with Clang.
    Leak detection is Linux only. The plugin is not supported on Windows.

    Enabling this plugin on a platform without sanitizers does not affect your
    other builds. Only a `sanitize:` task requires them.

The Sanitize plugin compiles and links your tests with the sanitizers, then
runs each test executable with the sanitizers’ runtime options set for it
alone. Each sanitizer reports what it finds as the test runs.

The plugin provides invocation modes mirroring standard `test:` tasks.

- **Whole test suite**: `ceedling sanitize:all` builds and runs every test
  executable with sanitizers.
- **Single test file**: `ceedling sanitize:<filename>` builds and runs one.

By default a sanitizer stops a test at its first finding, and any finding fails
the build. Each test’s sanitizer reports are saved to a log file of its own.

Sanitizer flags only reach the builds this plugin instruments. Builds from
other plugins, such as `gcov:` and `valgrind:`, are never instrumented.
