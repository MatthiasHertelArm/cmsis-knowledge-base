---
id: "intr-reproducible-firmware-builds"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds"
summary: "If you have ever worked on a large scale embedded project before, you've probably run into situations where the build system or binary behaves differently depending on where it was compiled."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you have ever worked on a large scale embedded project before, you've probably run into situations where the build system or binary behaves differently depending on where it was compiled. For example, maybe the binary completely fails to compile on one computer and on another it compiles but crashes on boot!



In this article we will discuss what a **Reproducible Build** is, walk through the process of updating a firmware project so the build _is_ reproducible, and explore how we can leverage what we have learned for other aspects of development.
