---
id: "intr-practical-zephyr-devicetree-semant-zephyr-s-devicetree-api"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Zephyr's Devicetree API"
summary: "Now that we've seen both, DTS files and their bindings, we'll wrap up this article by looking at how the generated macros are accessed in an application. We'll cover the most common macros from zephyr/include/zephyr/devicetree.h."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#zephyr-s-devicetree-api"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we've seen both, DTS files and their bindings, we'll wrap up this article by looking at how the generated macros are accessed in an application. We'll cover the most common macros from `zephyr/include/zephyr/devicetree.h`. Those macros are the basis for most Zephyr modules, e.g., `gpio`s, that in turn provide their own Devicetree API built on top of the mentioned macros.

Except for the macros used to access a node's identifier, in practice you'll use macros provided by the corresponding subsystem. E.g., the `gpio` subsystem has its own Devicetree macros. It is nevertheless important to understand the basics, especially if you're planning to write your own drivers. In the next article, we'll see some examples of practical, subsystem-specific Devicetree APIs.

> **Note:** For details, you'll always need to refer to the [official Devicetree API documentation](https://docs.zephyrproject.org/latest/build/dts/api/api.html) and to the corresponding subsystems. The documentation is really great and has **lots** of examples. We'll cover the basics here so that you can easily navigate the documentation. There are simply too many macros to cover them all!

In the following sections, we'll be accessing the properties of the nodes that we've created throughout this article. In case you didn't follow along but still would like to try it out yourself, use [the freestanding application in the reference repository](https://github.com/lmapii/practical-zephyr/tree/main/03_devicetree_semantics). It also contains most code snippets in its `main.c` file.
