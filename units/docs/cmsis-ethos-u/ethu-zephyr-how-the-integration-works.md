---
id: "ethu-zephyr-how-the-integration-works"
type: "concept"
domain: "edge-ai"
title: "Zephyr: How the integration works"
summary: "Zephyr provides the Ethos-U driver as a module and connects it to TensorFlow Lite for Microcontrollers (TFLM) as a custom operator. A Vela-compiled model contains the Ethos-U command stream."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/zephyr/src/main.md#how-the-integration-works"
license: "Apache-2.0"
mode: "V"
---

Zephyr provides the Ethos-U driver as a module and connects it to TensorFlow
Lite for Microcontrollers (TFLM) as a custom operator. A Vela-compiled model
contains the Ethos-U command stream. When the application invokes the model,
TFLM dispatches the custom operator to the Ethos-U driver.

The following configuration layers must agree:

| Layer | Responsibility |
|---|---|
| Vela | Compile the model for the exact Ethos-U architecture, MAC configuration, system configuration, and memory mode. |
| Devicetree | Describe the NPU register range, interrupt, security/privilege mode, and optional fast-memory region. |
| Kconfig | Enable TFLM and the Ethos-U integration. |
| Board support | Provide the physical addresses, interrupt specifier, memory regions, and required security attribution. |

See Vela for model compilation and
Integration for the end-to-end memory and driver
mapping.
