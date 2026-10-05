---
id: "intr-practical-zephyr-devicetree-practi-conclusion"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Conclusion"
summary: "In this article, we made use of what we've learned about the Devicetree and its bindings and had a detailed look at advanced Devicetree concepts in Zephyr."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article, we made use of what we've learned about the Devicetree and its bindings and had a detailed look at advanced Devicetree concepts in Zephyr. I really hope that this article made up for all the theory that I've put you through!

Some of you might have expected a bit more of a "practice" article, but looking at APIs and drivers in Zephyr, I see no point in writing an article when there are so many [samples and demos](https://docs.zephyrproject.org/latest/samples/index.html) that do a much better job - and are maintained by the awesome Zephyr contributors.

Instead, we had a look at _some_ of Zephyr's APIs and device drivers to learn that _Devicetree_ is much more than just simple macro pasting for obtaining property values. The section on _pin control_ showed us a more advanced concept in Devicetree that you'll for sure need for even simple applications. At the same time, it also showed us that _Devicetree_ concepts in Zephyr are still evolving, since the `pinctrl` feature was not available prior to Zephyr 3.0 - and that's very good news!

> **Note:** The full example application including all the Devicetree files that we've seen throughout this article is available in the [`04_practice` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/04_practice).
