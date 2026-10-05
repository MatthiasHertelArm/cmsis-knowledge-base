---
id: "etarm-arm-cortex-m-backend-quantization-support"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend: Quantization Support"
summary: "The Cortex-M backend currently implements symmetric INT8 (8w8a) quantization: - Per-channel quantization for convolution operators. - Per-tensor quantization for all other supported operators. - Shared quantization parameters for data-movement operators (e.g. reshape, permute) to avoid unnecessary requantization."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md#quantization-support"
license: "BSD-3-Clause"
mode: "V"
---

The Cortex-M backend currently implements **symmetric INT8 (8w8a)** quantization:
- **Per-channel** quantization for convolution operators.
- **Per-tensor** quantization for all other supported operators.
- **Shared quantization parameters** for data-movement operators (e.g. reshape, permute) to avoid unnecessary requantization.

CMSIS-NN also supports INT4 weights with INT8 activations (4w8a), INT8 weights with INT16 activations (8w16a), and per-channel quantization for fully connected layers, but the corresponding quantizer configurations and operator implementations are not yet integrated.
