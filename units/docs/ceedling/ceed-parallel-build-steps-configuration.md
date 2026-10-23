---
id: "ceed-parallel-build-steps-configuration"
type: "concept"
domain: "test"
title: "Parallel Build Steps: Configuration"
summary: "To enable parallel builds, simply configure either or both of the following in your project configuration:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/parallel-builds.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/parallel-builds/#configuration"
license: "MIT"
mode: "V"
---

To enable parallel builds, simply configure either or both of the following in
your project configuration:

* [`:project` ↳ `:compile_threads`](https://throwtheswitch.github.io/Ceedling/configuration/parallel-builds/reference/project.md#compile_threads)
* [`:project` ↳ `:test_threads`](https://throwtheswitch.github.io/Ceedling/configuration/parallel-builds/reference/project.md#test_threads)

These two settings allow you to separate build step parallelism from test suite
execution parallelism. Why? A core reason is because some emulator setups
necessary for test suite execution do not allow multiple instances running
simultaneously.
