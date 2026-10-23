---
id: "etarm-introduction-conclusion"
type: "concept"
domain: "edge-ai"
title: "Introduction: Conclusion"
summary: "The ExecuTorch project already provides an Arm Ethos-U backend in executorch/backends/arm/runtime/ that you can reuse as is."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/ethos-u-porting-guide.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/ethos-u-porting-guide.md#conclusion"
license: "BSD-3-Clause"
mode: "V"
---

The ExecuTorch project already provides an Arm Ethos-U backend in `executorch/backends/arm/runtime/` that you can reuse as is. The key steps to bring up a new platform is to reuse the Ethos-U driver
and ensure that the NPU base address and interrupt assignment matches your SoC.  The `examples/arm/executor_runner/arm_executor_runner.cpp` is an example application running on the Corstone platform.
For the `arm_executor_runner.cpp` application, we are relying on the NPU initialization done in the core-platform project and we integrate core-platform in the
`backends/arm/scripts/corstone_utils.cmake` script. Then, we inherit the core-platform integration of the Ethos-U driver and the CMSIS boot code for the Cortex-M core.
