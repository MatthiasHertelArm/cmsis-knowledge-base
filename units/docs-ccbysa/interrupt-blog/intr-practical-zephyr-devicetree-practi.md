---
id: "intr-practical-zephyr-devicetree-practi"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5)"
summary: "In the previous articles, we covered Devicetree in great detail: We've seen how we can create our own nodes, we've seen the supported property types, we know what bindings are, and we've seen how to access the Devicetree …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the previous articles, we covered _Devicetree_ in great detail: We've seen how we can create our own nodes, we've seen the supported property types, we know what bindings are, and we've seen how to access the Devicetree using Zephyr's `devicetree.h` API. In this fifth article of the _Practical Zephyr_ series, we'll look at how Devicetree is used in _practice_ by dissecting the _Blinky_ application.



Using a practical example, we'll see that our deep dive into Devicetree was really only covering the basics that we need to understand more advanced concepts, such as [pin control](https://docs.zephyrproject.org/latest/hardware/pinctrl/index.html) and device drivers.

👉 Find the other parts of the *Practical Zephyr* series [here](https://interrupt.memfault.com/tags#practical-zephyr-series).

> 🎬
> [Listen to Martin on Interrupt Live](https://www.youtube.com/watch?v=ls_Y45WsTiA?feature=share)
> talk about the content and motivations behind writing this series.
