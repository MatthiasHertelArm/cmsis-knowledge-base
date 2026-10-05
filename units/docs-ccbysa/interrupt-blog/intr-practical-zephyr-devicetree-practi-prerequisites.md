---
id: "intr-practical-zephyr-devicetree-practi-prerequisites"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Prerequisites"
summary: "This article is part of the Practical Zephyr article series. In case you haven't read the previous articles, please go ahead and have a look."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

This article is part of the _Practical Zephyr_ article series. In case you haven't read the previous articles, please go ahead and have a look. This article requires that you're able to build and flash a Zephyr application to the board of your choice and that you're familiar with _Devicetree_.

We'll be mainly using the [development kit for the nRF52840](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk) but will also refer to example files from the [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html) towards the end of the article. You can follow along with any target - real or virtual.

> **Note:** A full example application including all files that we'll see throughout this article is available in the [`04_practice` folder of the accompanying GitHub repository](https://github.com/lmapii/practical-zephyr/tree/main/04_practice).
