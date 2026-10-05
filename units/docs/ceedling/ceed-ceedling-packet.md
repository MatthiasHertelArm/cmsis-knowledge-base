---
id: "ceed-ceedling-packet"
type: "concept"
domain: "test"
title: "Ceedling Packet"
summary: "Ceedling is a fancypants build system that greatly simplifies building C projects. While it can certainly build release targets, it shines at running unit test suites."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/"
license: "MIT"
mode: "V"
---

Ceedling is a fancypants build system that greatly simplifies building 
C projects. While it can certainly build release targets, it 
shines at running unit test suites.

!!! tip "New to Ceedling?"
    

    Jump straight to the [Quick Start][quick-start] — installation,
    project set up, and your first build tasks all in one place.

In essence, Ceedling is a project configuration in YAML and a command line
tool that executes from it. Code conventions and supporting features produce 
executable test suites and/or release artifacts.
Plugins provide reporting, code coverage, static analysis, and more.

Ceedling and its suite of frameworks, including Unity and CMock, were developed 
for use on platforms from heavy duty workstations to teeny tiny microcontrollers. 
Features handy for low-level development have made these tools popular with 
embedded systems developers.

!!! feature "New in Ceedling 1.1.0 — Partials"
    A [_Partial_](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/index.md) is your C code sliced and diced
    to expose functional elements for testing that you could not otherwise 
    access without rewriting your source code. Think of Partials as a scalpel 
    for testing your code.

    👀 See the [Changelog](https://github.com/ThrowTheSwitch/Ceedling/blob/master/docs/Changelog.md)
    for all the new goodness in 1.1.0.

---
