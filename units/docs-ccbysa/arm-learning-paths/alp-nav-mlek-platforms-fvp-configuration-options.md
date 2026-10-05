---
id: "alp-nav-mlek-platforms-fvp-configuration-options"
type: "concept"
domain: "edge-ai"
title: "Navigate Machine Learning development with Ethos-U processors: Development platforms: FVP configuration options"
summary: "These virtual platforms have some options to help you evaluate different configurations."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/nav-mlek/platforms.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/nav-mlek/platforms/#fvp-configuration-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

These virtual platforms have some options to help you evaluate different configurations.

### Number of MACs

Ethos-U55 and Ethos-U65 offer a configurable number of MACs (multiply-accumulate units). During IP evaluation and performance analysis you need to understand the numbers of MACs available in the hardware and create your software to use the same configuration.

| Ethos-U NPU | Number of MACs supported    |
| ----------- | -----------                 |
| Ethos-U55   | 32, 64, 128, 256            |
| Ethos-U65   | 256, 512                    |

FVPs can be configured with:
```console
-C ethosu.num_macs=128
```
### Fast mode

The Ethos-U model used in FVPs can run at a faster speed with less simulation detail.

Use this configuration parameter to enable fast mode:

```console
-C ethosu.extra_args="--fast"
```

### Hardware memory maps

A memory map is available for each configuration of the Corstone kits. For example, the Corstone-300 with Cortex-M55 and Ethos-U55 [memory map](https://developer.arm.com/documentation/100966/1118/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300/) describes the address ranges for memory and peripherals.

Refer to the reference guides for details about the hardware models:
- [Corstone-300 Reference Guide](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-300-FVP/)
- [Corstone-310 Reference Guide](https://developer.arm.com/documentation/100966/latest/Arm--Corstone-SSE-310-FVP/)
- [Corstone-315 Reference Guide](https://developer.arm.com/documentation/109395/latest)
- [Corstone-320 Reference Guide](https://developer.arm.com/documentation/109760/latest)

The memory map of FVPs is NOT configurable.
