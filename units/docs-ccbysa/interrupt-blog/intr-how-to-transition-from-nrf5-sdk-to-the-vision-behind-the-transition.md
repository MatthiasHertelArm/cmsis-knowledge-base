---
id: "intr-how-to-transition-from-nrf5-sdk-to-the-vision-behind-the-transition"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: The Vision Behind the Transition"
summary: "When Ultrahuman launched its flagship health-tracking devices, FreeRTOS provided the lightweight real-time capabilities we needed. However, as our technology matured, so did our aspirations. We wanted to offer:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#the-vision-behind-the-transition"
license: "CC-BY-SA-4.0"
mode: "V"
---

When Ultrahuman launched its flagship health-tracking devices, FreeRTOS provided
the lightweight real-time capabilities we needed. However, as our technology
matured, so did our aspirations. We wanted to offer:

- **Superior BLE performance**: With Zephyr's robust BLE stack, we could achieve
  more stable connections and seamless interactions across various mobile
  platforms, especially iOS.
- **Improved health insights**: The integration of sophisticated third-party
  algorithms for metrics like heart rate variability, sleep patterns, and
  metabolic tracking demanded a more modular and scalable RTOS.
- **Future-proofing**: Zephyr's growing ecosystem and support for modern
  embedded hardware made it the ideal choice for long-term innovation.

But making the shift wasn’t going to be easy—especially with devices already out
in the wild.
