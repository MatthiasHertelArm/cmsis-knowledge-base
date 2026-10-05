---
id: "intr-bluetooth-low-energy-a-primer-introduction"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Introduction"
summary: "You've probably heard the term IoT (Internet of Things) many times, and seen the hype in the media surrounding it. Simply stated, IoT refers to connecting devices to each other and to the Internet."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've probably heard the term IoT (Internet of Things) many times, and seen
the hype in the media surrounding it. Simply stated, IoT refers to connecting
devices to each other and to the Internet. IoT often depends on wireless
technologies, which have been used to add connectivity to a slew of devices that were
never connected before
(even [flip-flops](https://www.geek.com/tech/smart-flip-flops-keep-brand-buyers-connected-1694504/)!).


In today's post, we will be covering one of the most popular low-power IoT
technologies: Bluetooth Low Energy (BLE). We will give an overview of how BLE
works, dig into each protocol layer, and walk you through an example setting
up BLE on a Nordic nRF52 microcontroller.
