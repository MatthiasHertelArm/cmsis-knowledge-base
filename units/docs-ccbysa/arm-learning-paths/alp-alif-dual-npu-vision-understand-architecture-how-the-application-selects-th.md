---
id: "alp-alif-dual-npu-vision-understand-architecture-how-the-application-selects-th"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Understand the dual-NPU architecture: How the application selects the NPU from model metadata"
summary: "The application enables the Ethos-U core driver's multi-variant support with ETHOSU_MULTI_VARIANT. This support is part of the core-driver main branch. During initialization, ethosu_init_ex() registers both physical devices with their product descriptors."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/understand-architecture/#how-the-application-selects-the-npu-from-model-metadata"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application enables the Ethos-U core driver's multi-variant support with
`ETHOSU_MULTI_VARIANT`. This support is part of the core-driver `main`
branch. During initialization, `ethosu_init_ex()` registers both physical
devices with their product descriptors.

The motivation for this multi-variant driver support is to let one MCU
manage different Ethos-U products in the same system. Without multi-variant driver support, software
integration tends toward separate driver instances or separate processing
domains for each NPU variant. A common registry keeps device discovery,
interrupt handling, and workload dispatch in one Zephyr application. This
supports the lower-overhead system architecture described earlier.

Vela stores a COP1 optimizer record in each delegated program. The record identifies the target product and MAC configuration:

| Optimizer value | Selection |
| --- | --- |
| Product 0, log2 MACs 8 | Ethos-U55 with 256 MACs |
| Product 2, log2 MACs 8 | Ethos-U85 with 256 MACs |

The ExecuTorch backend parses this record and asks the registry for a compatible free driver. Device selection is therefore a property of the compiled PTE model rather than a hard-coded assumption in the worker thread.
