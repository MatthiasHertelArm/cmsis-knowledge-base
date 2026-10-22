---
id: "ceed-dependencies-building-dependencies"
type: "concept"
domain: "test"
title: "Dependencies: Building dependencies"
summary: "The heart of the plugin is the build process you specify for each dependency under :build, a list of steps Ceedling runs in order. Any tools those steps use must be installed."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#building-dependencies"
license: "MIT"
mode: "V"
---

The heart of the plugin is the build process you specify for each dependency under
`:build`, a list of steps Ceedling runs in order. Any tools those steps use must be
installed. A failing step stops the build with its error.

Each step is a command line, which runs from the dependency’s `:source` path exactly as
written, quoting and spacing included. The source, build, and artifact paths are created
first if they do not exist. A step can instead be `:build_lib`, which builds a static
library with Ceedling’s own compiler and archiver (see [Custom tools](#custom-tools)).
