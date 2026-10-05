---
id: "ceed-dependencies-building-dependencies"
type: "concept"
domain: "test"
title: "Dependencies: Building Dependencies"
summary: "The heart of the :dependencies plugin is the ability for you, the developer, to specify the build process for each of your dependencies. You will need to have any required tools installed before using this feature."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#building-dependencies"
license: "MIT"
mode: "V"
---

The heart of the `:dependencies` plugin is the ability for you, the developer, to specify the
build process for each of your dependencies. You will need to have any required tools installed
before using this feature.

The steps are specified as an array of strings. Ceedling will execute those steps in the order
specified, moving from step to step unless an error is encountered. By the end of the process,
the artifacts should have been created by your process... otherwise an error will be produced.
