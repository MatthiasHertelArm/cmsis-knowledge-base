---
id: "intr-practical-zephyr-devicetree-basics-basic-source-file-syntax"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Basic source file syntax"
summary: "Now we finally take a closer look at the Devicetree syntax and its files. We'll walk through it by creating our own Devicetree nodes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#basic-source-file-syntax"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now we finally take a closer look at the Devicetree syntax and its files. We'll walk through it by creating our own Devicetree nodes. This section heavily borrows from existing documentation such as the [Devicetree specification](https://www.devicetree.org/specifications/), [Zephyr's Devicetree docs](https://docs.zephyrproject.org/latest/build/dts/index.html) and the [nRF Connect SDK Fundamentals lesson on Devicetree](https://academy.nordicsemi.com/topic/devicetree/).

> **Note:** We won't explain _all_ syntactical aspects, but will focus on the most important ones. Have a look at the [Devicetree specification](https://www.devicetree.org/specifications/) for a full syntax description. Also, misplaced semicolons, etc., will also be caught by the Devicetree compiler in the future, so we won't talk about trivial details.
