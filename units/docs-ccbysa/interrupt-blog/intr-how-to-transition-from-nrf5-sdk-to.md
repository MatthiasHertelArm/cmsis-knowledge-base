---
id: "intr-how-to-transition-from-nrf5-sdk-to"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey"
summary: "At Ultrahuman, innovation is at the core of everything we do. Our health devices, powered by the nRF52840 SoC for BLE functionality, rely on Nordic Semiconductor’s renowned wireless technology."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs"
license: "CC-BY-SA-4.0"
mode: "V"
---

At [Ultrahuman](https://www.ultrahuman.com/), innovation is at the core of
everything we do. Our health devices, powered by the nRF52840 SoC for BLE
functionality, rely on Nordic Semiconductor’s renowned wireless technology. For
years, the
[nRF5 SDK](https://www.nordicsemi.com/Products/Development-software/nRF5-SDK)
was the cornerstone of firmware development for these chipsets, but in 2018,
Nordic introduced the
[nRF-Connect SDK](https://www.nordicsemi.com/Products/Development-software/nRF-Connect-SDK)
(NCS), built on Zephyr RTOS, signaling a new era for BLE applications.

As a health tech company delivering cutting-edge metabolic and fitness insights,
we recognized the need to modernize. The challenge? Migrating devices already in
users’ hands from FreeRTOS-based firmware to a Zephyr-based application without
disrupting their experience. This transition wasn’t just a technical upgrade—it
was a critical step toward leveraging advanced BLE capabilities and third-party
algorithms to provide more accurate health data.



In this article, we’ll walk you through our journey, the challenges we faced,
and how this migration is shaping a better future for those who rely on our
technology to improve their health and fitness.
