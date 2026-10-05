---
id: "ceed-flags-flags-plugin-context"
type: "concept"
domain: "test"
title: "`:flags`: `:flags` ↳ `:<plugin context>`"
summary: "Some advanced plugins make use of build contexts as well. For instance, the Ceedling Gcov plugin uses a context of :gcov, surprisingly enough."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#flags-plugin-context"
license: "MIT"
mode: "V"
---

Some advanced plugins make use of build contexts as well. For instance, the
Ceedling Gcov plugin uses a context of `:gcov`, surprisingly enough. For any
plugins with tools that take advantage of Ceedling’s internal mechanisms, you
can add to those tools' flags in the same manner as the built-in contexts and
operations.
