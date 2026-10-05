---
id: "intr-practical-zephyr-devicetree-semant-prerequisites"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Prerequisites"
summary: "This article is part of the Practical Zephyr article series. In case you haven't read the previous articles, please go ahead and have a look."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

This article is part of the _Practical Zephyr_ article series. In case you haven't read the previous articles, please go ahead and have a look. In this article we're building up on what we've seen in the [Devicetree basics](https://interrupt.memfault.com/blog/practical_zephyr_dt): We'll add _bindings_ to the same nodes that we've created in the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_dt). If you have some experience with _Devicetree_ and Zephyr, you should be able to follow along just fine without reading the previous articles.

> **Note:** A full example application including all files that we'll see throughout this article is available in the [`03_devicetree_semantics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/03_devicetree_semantics).

We'll again be using the [development kit for the nRF52840](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk) as a reference and exploring its files in Zephyr, but you can follow along with any target - real or virtual.
