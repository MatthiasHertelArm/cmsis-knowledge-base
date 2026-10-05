---
id: "etarm-introduction-npu-initialization"
type: "concept"
domain: "edge-ai"
title: "Introduction: NPU initialization"
summary: "In order to initialize the NPU hardware, the software needs to provide correct information about: - The base address of the Ethos-U NPU on the memory map of the SoC. - The interrupt assignment for the Ethos-U."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/ethos-u-porting-guide.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/ethos-u-porting-guide.md#npu-initialization"
license: "BSD-3-Clause"
mode: "V"
---

In order to initialize the NPU hardware, the software needs to provide correct information about:
- The base address of the Ethos-U NPU on the memory map of the SoC.
- The interrupt assignment for the Ethos-U. You also need to provide interrupt priority.

In the `executorch/examples/arm/executor_runner/arm_executor_runner.cpp` sample application, we inherit the Corstone-300/Corstone-320 NPU initialization done in the [core-platform project](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-platform).
We include the core-platform project as a dependency in the `backends/arm/scripts/corstone_utils.cmake` script. Note that in [corstone_utils.sh](https://github.com/pytorch/executorch/blob/main/backends/arm/scripts/corstone_utils.cmake#L69)
depending on whether we target Ethos-U55 or Ethos-U85, we include the  corresponding target from core-platform. Then, inside core-platform, the NPU base address and interrupt assignment are defined in the
[target.cpp](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-platform/-/blob/main/targets/corstone-320/target.cpp?ref_type=heads#L44) as per the memory map of the Corstone-300/Corstone-320.
It's worth mentioning that the code in core-platform(code we reuse in the `examples/arm/executor_runner/arm_executor_runner.cpp`) also calls the `ethosu_init`
function to initialize the NPU. The `ethosu_init` function is [defined in the Ethos-U driver](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver/-/blob/main/src/ethosu_driver.c?ref_type=heads#L409). The ethos-u driver itself is
included within the core-platform CMake. In other words, to initialize the NPU in the ExecuTorch executor runner application, we reuse the Ethos-U initialization that has been done in the core-platform project.
Core-platform includes a [tutorial](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-platform/-/blob/main/PORTING.md?ref_type=heads) on porting a new target. If you port your target to
core-platform, you can then easily reuse it in the ExecuTorch runtime.

Also, as explained in the comments in `backends/arm/scripts/corstone_utils.cmake`, note that REGIONCFG register of the Ethos-U controls the memory(on-chip or external memory) used by the NPU to
access the the Ethos-U scratch buffer, ML model and Ethos-U fast scratch buffer. The REGIONCFG is defined in the Ethos-U driver and you need to configure it differently depending on the memory mode.
You can see in `backends/arm/scripts/corstone_utils.cmake` how we overwrite the register to the correct value depending on the memory mode.

For the Corstone platforms, we make use of the Timing Adapters to model different memory latencies. The Timing Adapter is only applicable to the Corstone targets and should not be included for another SoC.
