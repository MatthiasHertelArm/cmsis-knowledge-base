---
id: "ethu-vela-feature-overview"
type: "concept"
domain: "edge-ai"
title: "Vela: Feature overview"
summary: "The Vela compiler performs the offline, target-specific part of an Ethos-U deployment:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#feature-overview"
license: "Apache-2.0"
mode: "V"
---

The Vela compiler performs the offline, target-specific part of an Ethos-U
deployment:

- Reads quantized TFLite/LiteRT and TOSA ML models. Activations and weights must
  be quantized for Ethos-U acceleration.
- Detects operations supported by the selected NPU. In TFLite ML models,
  unsupported regions remain CPU operations; TOSA compilation has no CPU
  fallback.
- Rewrites, decomposes, packs, and fuses graph operations into Ethos-U work.
- Selects execution schedules and block configurations for the target MAC
  configuration.
- Compresses weights and uses cascading, striping, buffering, and tensor reuse
  to reduce storage and runtime tensor-memory demand.
- Allocates tensors among the constant, arena, and cache memory areas described
  by the selected system configuration and memory mode.
- Optimizes either for performance or for minimum peak SRAM use.
- Generates an optimized TFLite model or raw command-stream data.
- Reports operator placement, estimated cycles, bandwidth, and memory use.

Striping divides feature maps into smaller regions to reduce the active working
set. Cascading feeds each region directly through a sequence of compatible
operations, allowing Vela to use rolling buffers instead of storing complete
intermediate feature maps.

For the normal deployment flow, see the
system overview.

For TFLite output, supported regions become Ethos-U custom operators containing
the NPU command stream and related data. Unsupported TFLite operators remain in
the model for CPU execution, commonly using TensorFlow Lite Micro reference or
[CMSIS-NN](https://www.keil.arm.com/packs/cmsis-nn-arm) kernels.
Always review compiler warnings and `--show-cpu-operations`;
a successful compilation does not imply that every operation runs on the NPU.

The Vela compiler's cycle and bandwidth figures are cost-model estimates. Use
them to guide compiler decisions and compare like-for-like builds. Validate
final performance on an FPGA or target silicon; an
[Arm Fixed Virtual Platform (FVP)](https://www.arm.com/products/development-tools/simulation/fixed-virtual-platforms)
can provide approximate behavior.
