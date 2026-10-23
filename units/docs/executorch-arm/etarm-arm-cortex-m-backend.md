---
id: "etarm-arm-cortex-m-backend"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend"
summary: ":::{note} This backend is in beta. It has been validated with a set of small models (e.g. MLPerf Tiny, MobileNetV2) and provides broad operator coverage through CMSIS-NN accelerated kernels with portable-ops fallback. :::"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
license: "BSD-3-Clause"
mode: "V"
---

:::{note}
This backend is in **beta**. It has been validated with a set of small models (e.g. MLPerf Tiny, MobileNetV2) and provides broad operator coverage through CMSIS-NN accelerated kernels with portable-ops fallback.
:::

The Arm® Cortex®-M backend accelerates quantized model execution on Arm Cortex-M CPUs using [CMSIS-NN](https://arm-software.github.io/CMSIS-NN/latest/) optimized kernels. Unlike delegate-based backends, it operates as an operator library: quantized subgraphs are replaced with CMSIS-NN accelerated kernels during the pass-lowering stage, while unsupported operators fall back to portable fp32 kernels.

The default AOT flow uses channels-last inputs and the existing dim-order representation. The experimental explicit-layout flow uses ordinary contiguous inputs, represents NCHW/NHWC conversions as graph operators, and selects the experimental `cortex_m::*_nhwc` kernels. Enable it with `--cortex-m-explicit-layout`. Layout modes are selected independently of the Cortex-M CPU target and never mix operator families.
