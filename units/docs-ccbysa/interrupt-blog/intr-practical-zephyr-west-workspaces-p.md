---
id: "intr-practical-zephyr-west-workspaces-p"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6)"
summary: "In the previous articles, we used freestanding applications and relied on a global Zephyr installation. In this article, we'll see how we can use West to resolve global dependencies by using workspace applications."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the previous articles, we used _freestanding_ applications and relied on a global Zephyr installation. In this article, we'll see how we can use _West_ to resolve global dependencies by using _workspace_ applications. We first explore _West_ without even including _Zephyr_ and then recreate the modified **Blinky** application from the previous article in a _West workspace_.



After this article, you should know _West_ not as a meta-tool for `build` and `flash` commands, but as a powerful dependency manager for your Zephyr applications. Hopefully - after reading this article - you will no longer create _freestanding_ Zephyr applications but will use _West workspaces_ only.

👉 Find the other parts of the *Practical Zephyr* series [here](https://interrupt.memfault.com/tags#practical-zephyr-series).

> 🎬
> [Listen to Martin on Interrupt Live](https://www.youtube.com/watch?v=ls_Y45WsTiA?feature=share)
> talk about the content and motivations behind writing this series.
