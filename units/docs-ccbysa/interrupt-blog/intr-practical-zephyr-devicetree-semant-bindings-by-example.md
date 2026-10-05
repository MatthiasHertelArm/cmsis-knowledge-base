---
id: "intr-practical-zephyr-devicetree-semant-bindings-by-example"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Bindings by example"
summary: "This is it, we're finally there! We'll now add bindings for our extended example application to get some generated output for our node's properties. We've just seen that we can place our bindings in the dts/bindings directory."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#bindings-by-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is it, we're finally there! We'll now add bindings for our [extended example application](#extending-the-example-application) to get some generated output for our node's properties. We've just seen that we can place our bindings in the [`dts/bindings` directory](#bindings-directory).

> **Note:** A full example application including all files that we'll see throughout this article is available in the [`03_devicetree_semantics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/03_devicetree_semantics).
