---
id: "cmlek-overview-platform-support-2"
type: "concept"
domain: "edge-ai"
title: "Overview: Platform Support"
summary: "The templates support via target names multiple Arm Cortex-M IP Subsystems. These target names support execution on AVH FVP simulation models which is useful during software development or with Contiguous Integration (CI) testing using GitHub actions."
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:overview/README.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/overview/README.md#platform-support"
license: "Apache-2.0"
mode: "V"
---

The templates support via _target names_ multiple [Arm Cortex-M IP Subsystems](https://www.arm.com/products/silicon-ip-subsystems#Products). These _target names_ support execution on [AVH FVP simulation models](https://arm-software.github.io/AVH/main/simulation/html/index.html) which is useful during software development or with [Contiguous Integration (CI)](https://github.com/Arm-Examples/cmsis-mlek/actions) testing using GitHub actions.

| Target Name  | IP Subsystem | Description  |
|:-------------|:-------------|:-------------|
| SSE-300      | [Corstone-300](https://developer.arm.com/Processors/Corstone-300) | Cortex-M55 optional with Ethos-U55 or Ethos-U65 |
| SSE-310      | [Corstone-310](https://developer.arm.com/Processors/Corstone-310) | Cortex-M85 optional with Ethos-U55 |
| SSE-315      | [Corstone-315](https://developer.arm.com/Processors/Corstone-315) | Cortex-M85 optional with Ethos-U65 |
| SSE-320      | [Corstone-320](https://developer.arm.com/Processors/Corstone-320) | Cortex-M85 optional with Ethos-U85 |

Adding a postfix to the _target name_ in the `*.csolution.yml` project file configures the neural network inference pipeline for Ethos-U. Without this prefix only the Cortex-M system is used as shown in the diagram below. Such a postfix can also be used for _target names_ that deploy to physical hardware.

| Postfix      | Description |
|:-------------|:------------|
| _none_       | Cortex-M system only, no Ethos-U NPU |
| `-U55-128`   | Cortex-M system + Ethos-U55 NPU (128 MACs) |
| `-U55`       | Cortex-M system + Ethos-U55 NPU (256 MACs) |
| `-U65`       | Cortex-M system + Ethos-U65 NPU |
| `-U85`       | Cortex-M system + Ethos-U85 NPU |

(figure: Neural Network Inference Pipeline)
