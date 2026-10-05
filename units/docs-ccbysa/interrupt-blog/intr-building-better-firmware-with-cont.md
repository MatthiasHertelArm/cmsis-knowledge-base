---
id: "intr-building-better-firmware-with-cont"
type: "concept"
domain: "debug"
title: "Building Better Firmware with Continuous Integration"
summary: "Larger firmware projects sometimes have tens, even hundreds of engineers working in a single code base. This introduces new challenges: builds break, lesser used features get forgotten about, new features miss support for older hardware platforms."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-17-continuous-integration-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/continuous-integration-for-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Larger firmware projects sometimes have tens, even hundreds of engineers working
in a single code base. This introduces new challenges: builds break, lesser used
features get forgotten about, new features miss support for older hardware
platforms. Without solid tooling and processes, this can slow development to a
grind.

In the software world, the established solution is Continuous Integration. A
hallmark of engineering at large tech companies like Facebook and Google,
continuous integration has found its way into firmware projects[^1].



In this post, we introduce Continuous Integration as a modern technique to allow
larger teams to move fast without breaking things. We’ll explain what Continuous
Integration is, why you may want to use it, and walk you through setting up
CircleCI on a firmware project step by step.



This is the first post in our [Building Better Firmware series](). Future posts will
cover testing techniques, test driven development, fuzzing, and continuous
deployment.
