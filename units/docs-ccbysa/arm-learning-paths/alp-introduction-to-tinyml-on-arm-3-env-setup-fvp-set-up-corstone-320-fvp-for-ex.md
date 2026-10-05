---
id: "alp-introduction-to-tinyml-on-arm-3-env-setup-fvp-set-up-corstone-320-fvp-for-ex"
type: "concept"
domain: "edge-ai"
title: "Introduction to TinyML on Arm using PyTorch and ExecuTorch: Set up the Corstone-320 FVP: Set up Corstone-320 FVP for ExecuTorch"
summary: "Run the FVP setup script in the ExecuTorch repository:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/3-env-setup-fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/3-env-setup-fvp/#set-up-corstone-320-fvp-for-executorch"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the FVP setup script in the ExecuTorch repository:

```bash
cd $HOME/executorch
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

When the script completes, it prints a command to finalize the installation by adding the FVP executables to your `PATH`:

```bash
source $HOME/executorch/examples/arm/ethos-u-scratch/setup_path.sh
```

Test that the setup was successful by running the `run.sh` script for Ethos-U85, which is the target device for Corstone-320:

```bash
 ./examples/arm/run.sh --target=ethos-u85-256
```

You will see a number of examples run on the FVP.

This confirms the installation, so you can now proceed to the Learning Path [Build a Simple PyTorch Model](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/4-build-model/).
