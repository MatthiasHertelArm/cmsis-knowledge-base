---
id: "ethu-overview"
type: "concept"
domain: "edge-ai"
title: "Overview"
summary: "The Arm CMSIS Ethos-U pack provides the low-level driver for Arm Ethos-U55, Ethos-U65, and Ethos-U85 neural processing units (NPUs). The driver connects an ML inference runtime to the NPU and supports initialization, neural-network command-stream execution, interrupt handling, and performance monitoring."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:overview/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/overview/README.md"
license: "Apache-2.0"
mode: "V"
---

The **Arm CMSIS Ethos-U pack** provides the low-level driver for Arm [Ethos-U55](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55),
  [Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65), and
  [Ethos-U85](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) neural processing units (NPUs). The driver connects an
ML inference runtime to the NPU and supports initialization, neural-network
command-stream execution, interrupt handling, and performance monitoring.

Before deployment, the [Vela compiler](https://arm-software.github.io/CMSIS-Ethos-U/main/vela/index.html)
optimizes a quantized ML model for the selected Ethos-U target. At runtime, the
Cortex-M application and ML inference runtime use this pack's driver to submit
the compiled command stream and model memory regions to the NPU.
