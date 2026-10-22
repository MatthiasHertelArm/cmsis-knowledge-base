---
id: "etarm-getting-started-tutorial-running-on-corstone-fvp-platforms"
type: "concept"
domain: "edge-ai"
title: "Getting Started Tutorial: Running on Corstone FVP Platforms"
summary: "Finally, use the backends/arm/scripts/run_fvp.sh utility script to run the .elf-file on simulated Arm hardware."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md#running-on-corstone-fvp-platforms"
license: "BSD-3-Clause"
mode: "V"
---

Finally, use the `backends/arm/scripts/run_fvp.sh` utility script to run the .elf-file on simulated Arm hardware.
```
backends/arm/scripts/run_fvp.sh --elf=$(find ethos_u_minimal_example -name arm_executor_runner) --target=ethos-u55-128
```
The example application is by default built with an input of ones, so the expected result of the quantized addition should be close to 2.
