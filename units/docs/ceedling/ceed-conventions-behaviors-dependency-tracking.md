---
id: "ceed-conventions-behaviors-dependency-tracking"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Dependency tracking"
summary: "Ceedling only regenerates, compiles, links, or runs an element of the build pipeline if a change in the dependency tree requires it."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#dependency-tracking"
license: "MIT"
mode: "V"
---

Ceedling only regenerates, compiles, links, or runs an element of the build
pipeline if a change in the dependency tree requires it. This includes “deep
dependencies” wherein a change in a header file several nested layers deep in
`#include` statements correctly triggers a rebuild of every test executable
that depends on it, directly or indirectly.

This is called a delta build. Delta builds are automatic, need no
configuration, and complement Ceedling’s parallel build steps for further
build time speedups. See [Delta Builds](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../getting-started/builds.md) for the
full picture, including how test result caching works and the
`--force-test-rerun` flag.
