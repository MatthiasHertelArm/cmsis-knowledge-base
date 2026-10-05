---
id: "intr-practical-zephyr-west-workspaces-p-conclusion"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Conclusion"
summary: "In this article, we've seen how we can use West to manage our dependencies, including some of its pitfalls and limitations."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article, we've seen how we can use _West_ to manage our dependencies, including some of its pitfalls and limitations. Exploring the Zephyr application we have also seen, that managing dependencies can still be complicated in case you're dealing with projects that have the same dependencies, e.g., other SDKs that use different versions of Zephyr as dependency.

We also managed to build an application for MCUs from different vendors: This is possible in Zephyr, though it may take a bit more effort than advertised - at least in case you're dealing with a professional application. Personally, I still think that _Zephyr_ is a great step forward: Switching MCUs or supporting multiple targets _always_ includes efforts, but with Zephyr, the efforts are predictable and manageable.

This article marks the **end of the _Practical Zephyr_ series**: I hope that I could get you past the steep section of Zephyr's learning curve, towards a more enjoyable and reasonable experience. There's still a ton to explore!

A big **Thank You** to the team at [Memfault](https://memfault.com/) for their patience, the reviews, the invaluable feedback for these articles, and for maintaining the [Interrupt](https://interrupt.memfault.com/) blog!
