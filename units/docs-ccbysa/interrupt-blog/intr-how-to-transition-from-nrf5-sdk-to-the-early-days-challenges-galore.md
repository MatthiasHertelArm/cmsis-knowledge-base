---
id: "intr-how-to-transition-from-nrf5-sdk-to-the-early-days-challenges-galore"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: The Early Days: Challenges Galore"
summary: "We knew this wouldn’t be a standard firmware update. Here’s why:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#the-early-days-challenges-galore"
license: "CC-BY-SA-4.0"
mode: "V"
---

We knew this wouldn’t be a standard firmware update. Here’s why:

### 1\. Complexity of Migration

FreeRTOS and Zephyr have entirely different architectures. From task scheduling
to memory management, porting the application logic was like translating a book
from one language to another—with no dictionary. Our team spent sleepless nights
understanding how to replicate FreeRTOS-based workflows in Zephyr, ensuring no
loss of functionality.

### 2\. Testing Under Real-World Conditions

Our devices were being used by tens of thousands of users in diverse
environments. From intense workouts to restful nights, every scenario had to be
accounted for. Early prototypes showed inconsistencies in BLE connections,
causing data loss—a nightmare for health trackers. Resolving these issues
required countless hours of debugging and field testing.

### 3\. BLE Bonding Crisis

Our most daunting challenge emerged after the initial migration release. After
updating to the Zephyr-based application, devices failed to connect to paired
phones. Users had to unpair the device, restart their phones, and reattempt
pairing. While this worked on some devices, certain Android phones stubbornly
refused to reconnect—even after following these steps.

This was a critical issue, as it not only disrupted user experience but also
risked eroding trust in our brand. We needed a solution that would restore
seamless connectivity across all devices.
