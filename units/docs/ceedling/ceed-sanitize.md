---
id: "ceed-sanitize"
type: "concept"
domain: "test"
title: "Sanitize"
summary: "Adds Ceedling tasks to build and run test executables with the compiler’s sanitizers. [AddressSanitizer] (ASan), [UndefinedBehaviorSanitizer] (UBSan), and [LeakSanitizer] (LSan) find memory errors, undefined behavior, and leaks while your tests run."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/"
license: "MIT"
mode: "V"
---

Adds Ceedling tasks to build and run test executables with the compiler’s
sanitizers. [AddressSanitizer] (ASan), [UndefinedBehaviorSanitizer] (UBSan),
and [LeakSanitizer] (LSan) find memory errors, undefined behavior, and leaks
while your tests run.

The Sanitize plugin creates a duplicate test build with `sanitize:` command
line plugin tasks. [This is intentional and needed](https://throwtheswitch.github.io/Ceedling/plugins/sanitize/index.md#understanding-plugin-build-duplication).

!!! note
    A `sanitize:` task is a [delta build](https://throwtheswitch.github.io/Ceedling/plugins/sanitize/../getting-started/builds.md).
    This plugin maintains its own dependency cache. A test executable will be
    rebuilt the first time you run a `sanitize:` build.

---
