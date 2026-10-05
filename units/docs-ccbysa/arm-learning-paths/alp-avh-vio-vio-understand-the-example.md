---
id: "alp-avh-vio-vio-understand-the-example"
type: "concept"
domain: "edge-ai"
title: "Implement an example Virtual Peripheral with Arm Virtual Hardware: Create a peripheral using Virtual Input/Output (VIO): Understand the example"
summary: "The Virtual Hardware is launched with the -V option which specifies the Python implementation of the peripheral."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_vio/vio.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_vio/vio/#understand-the-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Virtual Hardware is launched with the `-V` option which specifies the Python implementation of the peripheral.

The Python scripts implement the [VIO Python interface](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vio__py.html) to communicate with the Virtual Hardware application.

In the application, signals are passed via the [VIO API](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vio__api.html) to/from the virtual peripheral.
