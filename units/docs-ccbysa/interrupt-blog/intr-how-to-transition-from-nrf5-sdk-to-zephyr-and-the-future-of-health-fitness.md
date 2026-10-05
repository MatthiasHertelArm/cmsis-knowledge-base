---
id: "intr-how-to-transition-from-nrf5-sdk-to-zephyr-and-the-future-of-health-fitness"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: Zephyr and the Future of Health & Fitness"
summary: "With Zephyr as our foundation, we’re building the next generation of Ultrahuman devices that will revolutionize how people engage with their health. Here’s what’s on the horizon:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#zephyr-and-the-future-of-health-fitness"
license: "CC-BY-SA-4.0"
mode: "V"
---

With Zephyr as our foundation, we’re building the next generation of Ultrahuman
devices that will revolutionize how people engage with their health. Here’s
what’s on the horizon:

### 1\. Continuous Health Monitoring

Zephyr’s real-time capabilities and seamless integration with third-party
libraries allow us to develop devices that monitor metabolic health, stress
levels, and sleep patterns with unprecedented accuracy.

The FreeRTOS version of Nordic’s SDK required more workarounds to ensure
compatibility with for third- party libraries compatibility compared to the
native support in Zephyr. RIt requireds manual integration of third-party
libraries, often necessitating copying files into the project and manually
adjusting build scripts (e.g., Makefiles).  
Additionally, Zephyr's **DeviceTree** and **Hardware Abstraction Layer (HAL)**
simplify configuring peripherals and sensors. Developers no longer need to
manually initialize or handle hardware registers — it’s all declaratively
defined in the DeviceTree.  
Zephyr also includes robust stacks for BLE, Wi-Fi, LoRa, Thread, CAN, and more.

Middleware such as **MCUboot**, **File Systems (e.g., FAT, LittleFS)**, and
**Networking Protocols** (MQTT, CoAP) are supported out of the box.

### 2\. Personalized Fitness Recommendations

Leveraging Zephyr's powerful processing capabilities, we’re integrating
AI-driven algorithms that analyze data trends to provide hyper-personalized
fitness plans. From dynamic workout adjustments to nutritional insights based on
real-time metabolic activity, the possibilities are endless.

### 3\. Accessibility and Scalability

Zephyr’s robust architecture allows us to develop cost-effective devices without
compromising on performance. The Zephyr- based stack offersprovides
**standardized, portable APIs**, while FreeRTOS relies onuses
**SoftDevice-specific APIs**., which These APIs are easier to use but less
flexible, limiting **more future-proof capabilities** such as(e.g., LE Audio
support and , open-source extensibility). Zephyr offers **more granular control
over power management.**

This means we can bring health-tracking technology to underserved populations,
promoting health equity and making advanced fitness tools accessible to
everyone.

### 4\. Environmental Impact

Zephyr’s energy-efficient architecture is enabling us to develop devices with
longer battery life and reduced energy consumption. In particular, Zephyr offers
**more granular control over power management.** This not only benefits users
but also reduces the environmental footprint of our products.

### 5\. Changing Lives

The potential societal impact is immense. Ultrahuman devices powered by Zephyr
will help users take control of their health in ways never before possible. By
enabling early detection of health issues, improving fitness outcomes, and
fostering healthier habits, we’re not just building products—we’re building
healthier communities.
