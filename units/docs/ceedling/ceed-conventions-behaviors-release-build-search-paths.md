---
id: "ceed-conventions-behaviors-release-build-search-paths"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Release build search paths"
summary: "Unlike test builds, release builds are relatively straightforward. Each source file is compiled into an object file. All object files are linked."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#release-build-search-paths"
license: "MIT"
mode: "V"
---

Unlike test builds, release builds are relatively straightforward. Each
source file is compiled into an object file. All object files are linked.
A Ceedling release build may optionally compile and link in CException
and can handle linking in libraries as well.

Search paths for release builds are configured with `:paths` ↳ `:include` 
in your project configuration. That's about all there is to it.
