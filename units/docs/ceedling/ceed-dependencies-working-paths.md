---
id: "ceed-dependencies-working-paths"
type: "concept"
domain: "test"
title: "Dependencies: Working paths"
summary: "A dependency’s paths are collected under its :paths. Each path you leave out falls back to another, and with none configured every path is dependencies/<task name>."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#working-paths"
license: "MIT"
mode: "V"
---

A dependency’s paths are collected under its `:paths`. Each path you leave out falls back
to another, and with none configured every path is `dependencies/<task name>`.

| Path | Purpose | When left out |
|---|---|---|
| `:fetch` | Where the dependency is fetched to | `:source` |
| `:source` | Where build commands run from | `:fetch` |
| `:build` | Where the build places its files | `:source`, then `:fetch` |
| `:artifact` | Where the outputs listed under `:artifacts` are found | `:build` |
| `:deploy` | Where `dependencies:deploy` copies dynamic libraries and executables | Your release executable’s folder |

Cleaning a dependency never removes its `:deploy` path, which holds copies alongside your
project’s own files.

If the dependency is part of your repository (its fetch `:method` is `:none`), `:source`
is where its code already lives. Paths may lie outside your project, such as
`../shared/lib`, and headers found there work in test and release builds alike.

Every artifact is relative to the `:artifact` path. With several include directories,
choose the highest level and list the rest relative to it.
