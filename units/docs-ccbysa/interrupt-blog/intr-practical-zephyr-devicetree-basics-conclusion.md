---
id: "intr-practical-zephyr-devicetree-basics-conclusion"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Conclusion"
summary: "In this article, we've learned what a devicetree is, its most important syntax, and how it is used in Zephyr. We've seen:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article, we've learned what a _devicetree_ is, its most important syntax, and how it is used in Zephyr. We've seen:

- What a Devicetree actually is,
- how a Devicetree is structured and how it represents the hardware,
- all basic property types and `phandle`s, including `phandle-array`s,
- we've seen the standard nodes `/chosen` and `/aliases`,
- and we've learned about addressing within Devicetree.

Even without looking at _bindings_ yet, this is a lot to take in, especially if you've never worked with *Devicetree* before. If you feel overwhelmed, don't worry, we'll look into each property type again in the next article about _bindings_ and thus **semantics**. Practice is key!

> **Note:** The full example application including all the Devicetree files that we've seen throughout this article is available in the [`02_devicetree_basics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/02_devicetree_basics).

Just like _Kconfig_, in your future Zephyr projects, _Kconfig_ will become especially important once you're starting to build your own device drivers. With this article, I hope I can give you an easy start and I hope to see you in the next article about Devicetree _bindings_!
