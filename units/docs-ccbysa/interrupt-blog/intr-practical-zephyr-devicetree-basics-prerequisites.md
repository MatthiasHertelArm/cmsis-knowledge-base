---
id: "intr-practical-zephyr-devicetree-basics-prerequisites"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree basics (Part 3): Prerequisites"
summary: "This article is part of an article series. If you haven't read the previous articles, please have a look. The first article explains the required installation steps, and we'll follow along with our running UART example from the previous article."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-01-practical_zephyr_dt.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

This article is part of an article _series_. If you haven't read the previous articles, please have a look. The [first article](https://interrupt.memfault.com/blog/practical_zephyr_basics) explains the required installation steps, and we'll follow along with our running UART example from the [previous article](https://interrupt.memfault.com/blog/practical_zephyr_kconfig). If you're already familiar with Zephyr and have a working installation at hand, it should be easy enough for you to follow along with your own setup without reading the previous articles.

> **Note:** A full example application including all the Devicetree source files that we'll see throughout this article is available in the [`02_devicetree_basics` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/02_devicetree_basics).

We'll again be using the [development kit for the nRF52840](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk) as a reference and explore its files in Zephyr, but you can follow along with any target - even virtual ones.

A short heads-up: We will _not_ define our own custom _board_, and we will _not_ describe memory layouts. Those are more advanced topics and go beyond this series. With this article, we want to have a detailed look and familiarize ourselves with Devicetree and the syntax of its input files.
