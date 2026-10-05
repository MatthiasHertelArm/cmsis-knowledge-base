---
id: "alp-deploy-mobilesam-on-ethos-u-prepare-the-environment-verify-the-environment"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Prepare the ExecuTorch and Arm environment: Verify the environment"
summary: "The output of the first command is similar to:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/#verify-the-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Confirm that Python imports ExecuTorch:

```bash
python -c "import executorch; print('ExecuTorch import succeeded')"
```

The output is similar to:

```output
ExecuTorch import succeeded
```

Check the target compiler and FVP:

```bash
arm-none-eabi-gcc -dumpmachine
command -v FVP_Corstone_SSE-320
```

The output of the first command is similar to:

```output
arm-none-eabi
```

The second command prints the path to the Corstone-320 FVP. On macOS, confirm that this path is inside the FVPs-on-Mac `bin` directory.
