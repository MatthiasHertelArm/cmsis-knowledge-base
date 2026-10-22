---
id: "etarm-arm-cortex-m-backend-target-support"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend: Target Support"
summary: "The backend targets Arm Cortex-M CPUs via CMSIS-NN, which provides optimized kernel implementations for three instruction set variants:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md#target-support"
license: "BSD-3-Clause"
mode: "V"
---

The backend targets Arm Cortex-M CPUs via CMSIS-NN, which provides optimized kernel implementations for three instruction set variants:

| Variant         | Description                 | Example CPUs           | Supported |
|-----------------|-----------------------------|------------------------|-----------|
| MVE (Helium)    | M-profile Vector extensions | Cortex-M55, M85        | ✅        |
| DSP             | DSP extension instructions  | Cortex-M4, M7, M33     | ✅        |
| Scalar (Pure C) | Reference C implementation  | Any Cortex-M (M0–M85)  | ✅        |

The variant is selected from the target CPU's `-mcpu` flag. Build a test runner for a specific target with `backends/cortex_m/test/build_test_runner.sh --target=<cortex-mX>` and run tests against it with `pytest --cortex-m-target=<cortex-mX>`.
