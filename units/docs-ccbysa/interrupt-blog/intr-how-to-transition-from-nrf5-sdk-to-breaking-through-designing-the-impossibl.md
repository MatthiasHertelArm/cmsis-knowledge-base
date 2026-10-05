---
id: "intr-how-to-transition-from-nrf5-sdk-to-breaking-through-designing-the-impossibl"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: Breaking Through: Designing the Impossible Solution"
summary: "We approached the migration with a clear strategy:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#breaking-through-designing-the-impossible-solution"
license: "CC-BY-SA-4.0"
mode: "V"
---

We approached the migration with a clear strategy:

### 1\. BLE Bonding Fix

The BLE bonding issue became our highest priority. After extensive analysis, we
discovered that the bonding information format in FreeRTOS and Zephyr differed
significantly. Bonding data stored on the FreeRTOS firmware was incompatible
with Zephyr’s stack, causing pairing failures.

Our breakthrough solution involved **copying the bonding information** from the
FreeRTOS firmware during the migration. We restructured this data to align with
Zephyr's bonding format and injected it into the Zephyr-based application during
the OTA update. This meant that after migration, the device retained all bonding
information, enabling it to connect seamlessly without requiring users to unpair
or re-pair their devices.

### 2\. Modular Architecture

Zephyr’s component-driven design allowed us to break the application into
smaller, testable modules. This helped in isolating issues during testing and
enabled easier debugging.

### 3\. BLE Enhancements

Leveraging Zephyr's BLE stack, we fine-tuned the connection parameters, reducing
packet loss and improving reconnection times. These changes dramatically
enhanced the BLE experience, especially for iOS users.

### 4\. Rigorous Testing Framework

We developed a hybrid testing setup combining hardware-in-the-loop (HIL)
simulations and real-world scenarios. Our emulation tools, like
[Renode](https://renode.io/), were instrumental in replicating edge cases that
might otherwise go unnoticed.

### 5\. Future Possibilities

The migration wasn’t just about solving today’s problems; it was about paving
the way for future innovations. Zephyr’s modularity and scalability opened new
doors for product development.
