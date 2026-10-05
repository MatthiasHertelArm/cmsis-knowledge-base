---
id: "intr-practical-zephyr-kconfig-part-2"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2)"
summary: "In this second article of the \"Practical Zephyr\" series, we'll explore the kernel configuration system Kconfig by looking at the printk logging option in Zephyr."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this second article of the "Practical Zephyr" series, we'll explore the [kernel configuration system Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig) by looking at the `printk` logging option in Zephyr. We won't explore the logging service as such in detail but instead use it as an excuse to dive deep into [Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig). Finally, we'll create our own little application-specific _Kconfig_ configuration.



👉 Find the other parts of the *Practical Zephyr* series [here](https://interrupt.memfault.com/tags#practical-zephyr-series).

> 🎬
> [Listen to Martin on Interrupt Live](https://www.youtube.com/watch?v=ls_Y45WsTiA?feature=share)
> talk about the content and motivations behind writing this series.
