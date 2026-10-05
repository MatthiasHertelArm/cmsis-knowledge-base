---
id: "ethu-arm-cmsis-ethos-u"
type: "concept"
domain: "edge-ai"
title: "Arm CMSIS Ethos-U"
summary: "This repository contains the source of the CMSIS software pack ARM::CMSIS-Ethos-U containing the Arm Ethos-U NPU core driver and supporting documentation. The driver supplies the low-level interface between embedded software and Arm Ethos-U55, Ethos-U65, and Ethos-U85 NPUs."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/README.md"
license: "Apache-2.0"
mode: "V"
---

This repository contains the source of the CMSIS software pack [`ARM::CMSIS-Ethos-U`](https://www.open-cmsis-pack.org/) containing the Arm Ethos-U NPU core driver and supporting documentation. The driver supplies the low-level interface between embedded software and Arm Ethos-U55, Ethos-U65, and Ethos-U85 NPUs.

The pack provides a single-variant driver component for each supported NPU
family and a multi-variant component containing support for all three families.
A single-variant build selects the NPU at compile time. A multi-variant build
selects the NPU product and MAC configuration for each driver instance at run
time.

Applications can use the driver to initialize an NPU, configure memory access,
invoke Vela-optimized ML models synchronously or asynchronously, handle
interrupts, and collect performance-monitoring data.

Refer to the [CMSIS-Ethos-U documentation](https://arm-software.github.io/CMSIS-Ethos-U/main/general/index.html) for architecture concepts, Vela configuration, driver usage, and system-integration guidance.
