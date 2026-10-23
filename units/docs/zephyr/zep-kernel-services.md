---
id: "zep-kernel-services"
type: "concept"
domain: "rtos"
title: "Kernel Services"
summary: "The Zephyr kernel lies at the heart of every Zephyr application. It provides a low footprint, high performance, multi-threaded execution environment with a rich set of available features."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/index.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr kernel lies at the heart of every Zephyr application. It provides
a low footprint, high performance, multi-threaded execution environment
with a rich set of available features. The rest of the Zephyr ecosystem,
including device drivers, networking stack, and application-specific code,
uses the kernel's features to create a complete application.

The configurable nature of the kernel allows you to incorporate only those
features needed by your application, making it ideal for systems with limited
amounts of memory (as little as 2 KB!) or with simple multi-threading
requirements (such as a set of interrupt handlers and a single background task).
Examples of such systems include: embedded sensor hubs, environmental sensors,
simple LED wearable, and store inventory tags.

Applications requiring more memory (50 to 900 KB), multiple communication
devices (like Wi-Fi and Bluetooth Low Energy), and complex multi-threading,
can also be developed using the Zephyr kernel. Examples of such systems
include: fitness wearables, smart watches, and IoT wireless gateways.
