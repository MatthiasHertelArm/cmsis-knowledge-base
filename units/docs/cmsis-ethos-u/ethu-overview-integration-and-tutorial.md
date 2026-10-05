---
id: "ethu-overview-integration-and-tutorial"
type: "concept"
domain: "edge-ai"
title: "Overview: Integration and tutorial"
summary: "The Integration guide describes the end-to-end workflow for creating an ML application for your target hardware."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:overview/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/overview/README.md#integration-and-tutorial"
license: "Apache-2.0"
mode: "V"
---

The [Integration guide](https://arm-software.github.io/CMSIS-Ethos-U/main/integration/index.html)
describes the end-to-end workflow for creating an ML application for your
target hardware. It covers selecting the device configuration, creating a CMSIS
solution project, compiling the model with Vela, placing the generated model
regions in physical memory, configuring the driver, and validating the complete
system.

The [tutorial](https://arm-software.github.io/CMSIS-Ethos-U/main/integration/index.html#tutorial)
uses Keil Studio for VS Code to start from an example that matches the target's
Ethos-U NPU. It shows how to obtain the resolved MLOps and Vela settings,
generate an NPU-optimized model, build the application, and extend the solution
with a board layer and configuration for the physical target hardware.

The pack includes three `Test-Ethos-U` CMSIS integration-test solutions. Each includes
an ML model and FVP simulator configuration for initial validation. You can extend an
example with other ML models and a configuration for the target hardware to
validate the system integration. Select the example that matches the target NPU:

| Example | NPU | FVP Simulation Model |
|---|---|---|
| `Test-Ethos-U55` | Ethos-U55 | V2M-MPS3-SSE-300 FVP |
| `Test-Ethos-U65` | Ethos-U65 | V2M-MPS3-SSE-300 FVP |
| `Test-Ethos-U85` | Ethos-U85 | SSE-320 FVP |

### Related examples

- [CMSIS-Ethos-Integration](https://github.com/Arm-Examples/CMSIS-Ethos-Integration) applies the integration workflow to a real-world device.
- [CMSIS-Ethos-Zephyr](https://github.com/Arm-Examples/CMSIS-Ethos-Zephyr) is the `Test-Ethos-U55` example ported to Zephyr.
