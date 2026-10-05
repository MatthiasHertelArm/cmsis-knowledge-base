---
id: "alp-alif-dual-npu-vision-understand-architecture-how-the-application-separates"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: How the application separates the hardware responsibilit"
summary: "One Zephyr application owns two driver objects, two register windows, two interrupt handlers, and two timing records:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#how-the-application-separates-the-hardware-responsibilities"
license: "CC-BY-SA-4.0"
mode: "V"
---

One Zephyr application owns two driver objects, two register windows, two interrupt handlers, and two timing records:

| Resource | Ethos-U55 | Ethos-U85 |
| --- | ---: | ---: |
| MMIO base | `0x400E1000` | `0x49042000` |
| NVIC interrupt | 55 | 366 |
| Worker priority | 5 | 4 |
| Primary workload | SSD-Slim | MobileNetV2 |
| Method pool | 640 KiB in HP DTCM | 304 KiB in SRAM1 |
| Temporary pool | 3,686,400 bytes in SRAM0 | 1,509,968 bytes in SRAM1 |

The two interrupt service routines call `ethosu_irq_handler()` with the matching driver. A U85 completion therefore can't release the U55 wait object. A U55 completion can't change the U85 timing record.
