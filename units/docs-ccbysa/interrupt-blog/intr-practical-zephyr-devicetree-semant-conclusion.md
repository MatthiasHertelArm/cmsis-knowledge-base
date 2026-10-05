---
id: "intr-practical-zephyr-devicetree-semant-conclusion"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Conclusion"
summary: "In this article, we've learned about Devicetree bindings and how they are used by Zephyr's generator script to produce code that can, in turn, be used by the application using Zephyr's Devicetree API. We've seen:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article, we've learned about Devicetree _bindings_ and how they are used by Zephyr's generator script to produce code that can, in turn, be used by the application using Zephyr's Devicetree API. We've seen:

- How Devicetree nodes are associated with bindings,
- what macros are generated for all property types,
- and how to use the generated macros with Zephyr's Devicetree API.

We haven't used specific subsystems, such as `gpio`, which add yet another layer of complexity on top of the basic Devicetree API. There are also other, more advanced concepts in Devicetree still that we haven't seen, e.g., _nexus_ nodes.

However, with what you've learned from this and the previous article about _Devicetree_ and _bindings_, you should have no problems looking things up in [Zephyr's official documentation](https://docs.zephyrproject.org/latest/build/dts/index.html), without having to follow too many links due to the missing basics.

> **Note:** The full example application including all the Devicetree files that we've seen throughout this article is available in the [`03_devicetree_semantics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/03_devicetree_semantics).
