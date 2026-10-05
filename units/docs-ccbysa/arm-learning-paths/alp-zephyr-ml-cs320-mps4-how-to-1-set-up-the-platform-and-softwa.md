---
id: "alp-zephyr-ml-cs320-mps4-how-to-1-set-up-the-platform-and-softwa"
type: "concept"
domain: "edge-ai"
title: "Deploy a Zephyr-based machine learning application on Arm Corstone-320 MPS4 with ExecuTorch: Set up the Zephyr and ExecuTorch development environment: Set up th"
summary: "The Arm Corstone SSE-320 FPGA image for MPS4 (FI101) is an FPGA implementation that runs on the MPS4 board. The image includes an Arm Cortex-M85 processor, an Arm Ethos-U85 NPU, and a range of peripheral components."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_ml_cs320_mps4/how-to-1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_ml_cs320_mps4/how-to-1/#set-up-the-platform-and-software"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Arm Corstone SSE-320 FPGA image for MPS4 (FI101) is an FPGA implementation that runs on the MPS4 board. The image includes an Arm Cortex-M85 processor, an Arm Ethos-U85 NPU, and a range of peripheral components. It provides a practical hardware platform for developing and evaluating machine learning applications.

Download the latest Corstone-320 FPGA image and review the platform documentation:

- [Arm Corstone SSE-320 with Cortex-M85 and Ethos-U85: Example FPGA (FI101)](https://developer.arm.com/downloads/view/FI101)
- [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en)
- [Arm MPS4 FPGA Prototyping Board Technical Reference Manual](https://developer.arm.com/documentation/102577/latest/)
- [Arm Corstone SSE-320 Example Subsystem Software Programmers Guide](https://developer.arm.com/documentation/109759/latest/)


### Set up a Zephyr workspace and board target

To set up the Zephyr workspace for the Arm Corstone-320 MPS4 platform, complete the steps in [Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-1/). Use Zephyr version V4.3.0.

### ExecuTorch integration in the Zephyr tree

ExecuTorch is integrated into the Zephyr workspace as an external module located in `modules/lib/executorch`. The module provides the ExecuTorch runtime, the Arm backend, the Ethos-U delegate, build scripts, and sample applications. You can build the sample applications using the Zephyr build system.

To add ExecuTorch as a Zephyr module, create `executorch.yaml` in `zephyr/submanifests` with the following content:

```yaml
manifest:
  projects:
    - name: executorch
      url: https://github.com/pytorch/executorch
      revision: main
      path: modules/lib/executorch
```

Run the following commands to fetch the ExecuTorch repository and its submodules. The commands place the ExecuTorch source tree in `modules/lib/executorch`:

```bash
west update
cd modules/lib/executorch
git submodule sync
git submodule update --init --recursive
./install_executorch.sh
```


### Set up the Arm and Ethos-U toolchain

ExecuTorch includes a setup script that downloads the Arm GNU Toolchain, the Tensor Operator Set Architecture (TOSA) Serialization Library, the Ethos-U Vela graph compiler, and other utilities.
 

Run the following commands to download, install, and configure these tools on your system:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

With the development environment and toolchain configured, prepare the model for deployment.
