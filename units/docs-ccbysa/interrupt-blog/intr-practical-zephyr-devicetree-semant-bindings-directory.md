---
id: "intr-practical-zephyr-devicetree-semant-bindings-directory"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Towards bindings / Bindings directory"
summary: "Before we can go ahead and experiment using our own bindings, we need to know where to place them."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#bindings-directory"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Towards bindings_

Before we can go ahead and experiment using our own bindings, we need to know where to place them. Just like the `dts/bindings` in _Zephyr's_ root directory, the [build process](https://docs.zephyrproject.org/latest/build/dts/intro-input-output.html) also picks up any bindings in `dts/bindings` in the _application's_ root directory.

In contrast to overlays, however, detected bindings are not listed in the build output.
