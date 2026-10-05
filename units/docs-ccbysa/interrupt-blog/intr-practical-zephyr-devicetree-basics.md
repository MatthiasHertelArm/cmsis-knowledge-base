---
id: "intr-practical-zephyr-devicetree-basics"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3)"
summary: "In the previous article, we configured software using the kernel configuration tool Kconfig, and we've silently assumed that there's a UART interface on our board that is configurable and used for logging."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_kconfig), we configured _software_ using the [kernel configuration tool Kconfig](https://docs.zephyrproject.org/latest/build/kconfig/index.html#configuration-system-kconfig), and we've silently assumed that there's a UART interface on our board that is configurable and used for logging.



In this third article of the "Practical Zephyr" series, we'll see how we configure and use _hardware_. For this, Zephyr borrows another tool from the Linux kernel: [**Devicetree**](https://docs.zephyrproject.org/latest/build/dts/index.html).

In contrast to _Kconfig_, the *Devicetree* syntax and its use are more intricate. Therefore, we'll cover *Devicetree* in two articles. In this article, we'll see what Devicetree is and how we can write our own Devicetree source files. In the next article, we'll look at so-called Devicetree _bindings_, which add semantics to our Devicetree. Be prepared for a fair bit of theory, but as usual, we'll use an example project to follow along.




👉 Find the other parts of the *Practical Zephyr* series [here](https://interrupt.memfault.com/tags#practical-zephyr-series).

> **Disclaimer:** This article covers Devicetree in _detail_ and from first principles. If you're already familiar with Devicetree or don't want to know how it works in detail, this article may not be for you. Instead, consider tuning in for the next article!

> 🎬
> [Listen to Martin on Interrupt Live](https://www.youtube.com/watch?v=ls_Y45WsTiA?feature=share)
> talk about the content and motivations behind writing this series.
