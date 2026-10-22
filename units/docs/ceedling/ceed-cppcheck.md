---
id: "ceed-cppcheck"
type: "concept"
domain: "test"
title: "Cppcheck"
summary: "Adds Ceedling tasks to run [Cppcheck] static analysis. Cppcheck finds undefined behavior, dangerous code patterns, and style issues across your project or in a single file, without running your code."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/"
license: "MIT"
mode: "V"
---

Adds Ceedling tasks to run [Cppcheck] static analysis. Cppcheck finds undefined
behavior, dangerous code patterns, and style issues across your project or in a
single file, without running your code.

!!! note
    A `cppcheck:` task analyzes source. It builds and runs nothing, so it is not
    a [delta build](https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/../getting-started/builds.md) and shares no state with your
    `test:` builds.

---
