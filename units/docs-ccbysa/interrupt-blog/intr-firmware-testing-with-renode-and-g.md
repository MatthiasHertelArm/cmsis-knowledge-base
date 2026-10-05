---
id: "intr-firmware-testing-with-renode-and-g"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions"
summary: "Automated firmware testing on real embedded hardware is what every hardware company strives to build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

Automated firmware testing on real embedded hardware is what every hardware
company strives to build. The mission is to repeatedly verify that changes to
firmware being merged into master and shipped to customers will not cause
catastrophic failures like power regressions or bootloops.

The problem with automated firmware testing with real hardware is that it's
**hard**. Not only does the system require a stable firmware to build on top of,
but it will also require extra hardware, like flashers and power supplies, and
software to orchestrate the tests and capture results.

An alternative to building a complicated orchestration system for automated
tests is to use the popular hardware emulator project, Renode, and its built-in
Robot Framework integration. By using Renode in conjunction with GitHub Actions,
we can ensure that every pull-request and commit to master passes all our tests.



In this post, I cover what it takes to build a simple firmware for use with
Renode, how to build and administer tests with Robot Framework, and how to run
these tests within GitHub's continuous integration system.
