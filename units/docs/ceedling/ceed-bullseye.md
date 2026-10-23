---
id: "ceed-bullseye"
type: "concept"
domain: "test"
title: "Bullseye"
summary: "This plugin measures code coverage with the commercially available [Bullseye Coverage][bullseye] tool. It adds a set of bullseye: build tasks that mirror Ceedling's test: tasks."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/"
license: "MIT"
mode: "V"
---

This plugin measures code coverage with the commercially available 
[Bullseye Coverage][bullseye] tool. It adds a set of `bullseye:` build tasks 
that mirror Ceedling's `test:` tasks. These tasks instrument your code, 
run your tests, and report how much of your source the tests actually exercised.

!!! warning "Requires a commercial license"
    Bullseye Coverage is commercial software. You need your own licensed
    installation. See [Licensing](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing.md).

!!! note
    A `bullseye:` task is a [delta build](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../../getting-started/builds.md).
    This plugin maintains its own dependency cache. Test executables and source
    files are rebuilt the first time you run a `bullseye:` build. Coverage
    instrumentation must be applied at compile time, so `bullseye:` builds
    cannot share objects with `test:` builds. See
    [Understanding plugin build duplication](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../index.md#understanding-plugin-build-duplication).

---
