---
id: "ceed-dependencies"
type: "concept"
domain: "test"
title: "Dependencies"
summary: "This plugin fetches, builds, and links the libraries and modules your project depends on. It’s rare for an embedded project to be built completely free of other code."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/"
license: "MIT"
mode: "V"
---

This plugin fetches, builds, and links the libraries and modules your project depends
on. It’s rare for an embedded project to be built completely free of other code. Some of
it may be standard internal libraries, and some may be third-party libraries. Either way,
it becomes part of the project’s ecosystem.

For each dependency, you tell this plugin where to fetch it from, how to build it, and what
it produces. Ceedling fetches and builds it whenever those outputs are missing, then adds
its headers, sources, and libraries to your test and release builds.

Most third-party libraries already have a build process of their own. Make? CMake? A
custom series of scripts that only a mad scientist could possibly understand? No matter.
You list the commands, and Ceedling runs them.

See the [_Cookbook_ section](#cookbook) for real-world scenarios along with the example 
`:dependencies` configurations and `ceedling dependencies:...` command lines to make
use of this plugin.
