---
id: "intr-pocket-article-how-to-implement-an"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM"
summary: "Imagine there's an embedded system that needs to persist some state when the processor restarts (either intentionally or due to a catastrophic error)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

Imagine there's an embedded system that needs to persist some state when the
processor restarts (either intentionally or due to a [catastrophic error](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug)).

This could be some external hardware information (what's the position of a motor
or actuator?) or a method to communicate the reset to the user (display some
information on the device's display).

A simple way to store information through a reboot is to use what's called
"non-initialized" memory.

> Note: this article applies to systems with Static Random-Access Memory (SRAM);
> systems with DRAM will likely need alternate strategies!



This pocket article will describe how a non-initialized region of memory works,
how to implement it, and how it can be used in a typical embedded system.
