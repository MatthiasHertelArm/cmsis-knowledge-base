---
id: "intr-practical-zephyr-west-workspaces-p-prerequisites"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Prerequisites"
summary: "This article is part of the Practical Zephyr article series. In case you haven't read the previous articles, please go ahead and have a look."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

This article is part of the _Practical Zephyr_ article series. In case you haven't read the previous articles, please go ahead and have a look. This article requires that you're able to build and flash a Zephyr application to the board of your choice and that you're familiar with _Devicetree_.

We'll be using the [development kit for the nRF52840](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk) and the [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-f411re.html), but you can follow along with any target - real or virtual.

> **Note:** This article uses two _manifest repositories_ that are available on GitHub:
> - [practical-zephyr-t2-empty-ws](https://github.com/lmapii/practical-zephyr-t2-empty-ws) contains an empty _manifest_ repository for creating a dummy _West_ workspace that we'll use to explore _West_ without Zephyr.
> - [practical-zephyr-manifest-repository](https://github.com/lmapii/practical-zephyr-manifest-repository) contains the _manifest repository_ of the Zephyr application that we're building in this article.

> **Note:** While writing this article series, I had to switch from STM's Nucleo-C031C6 to the Nucleo-F411RE since I broke my C031C6 development kit. Apologies for the subtle switch - but you should be able to follow along with any board.
