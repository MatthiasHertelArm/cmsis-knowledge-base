---
id: "alp-deploy-mobilesam-on-ethos-u-run-the-example-build-the-arm-executor-runner"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Build and run MobileSAM on the Corstone-320 FVP: Build the Arm executor runner"
summary: "Run the remaining commands from the ExecuTorch repository root."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/run-the-example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/run-the-example/#build-the-arm-executor-runner"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the remaining commands from the ExecuTorch repository root.

Load the Arm tools installed during environment setup:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

Build the standard Arm executor runner with the exported MobileSAM program:

```bash
backends/arm/scripts/build_executor_runner.sh \
  --pte=arm_test/mobilesam/export/mobilesam.pte \
  --target=ethos-u85-256 \
  --output=arm_test/mobilesam/runner \
  '--extra_build_flags=-DSEMIHOSTING=ON -DET_COMPILED_PTE=ON'
```

The script builds the required ExecuTorch libraries and the runner for Corstone-320. `ET_COMPILED_PTE=ON` embeds `mobilesam.pte` in the Executable and Linkable Format (ELF) file named `arm_executor_runner`, under `arm_test/mobilesam/runner/`.

`SEMIHOSTING=ON` lets the simulated target read input tensors from host files and write its output tensors back to the host.
