---
id: "alp-alif-image-classification-aws-ec2-setup-build-executorch-static-librar"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Build ExecuTorch static libra"
summary: "Your firmware needs to link against ExecuTorch's runtime libraries. Build them for bare-metal Cortex-M:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#build-executorch-static-libraries"
license: "CC-BY-SA-4.0"
mode: "V"
---

Your firmware needs to link against ExecuTorch's runtime libraries. Build them for bare-metal Cortex-M:

```bash
cd ~/alif/executorch
source ~/venv_executorch/bin/activate

rm -rf cmake-out
bash backends/arm/scripts/build_executorch.sh
```

This step takes several minutes. When complete, list the output libraries:

```bash
find arm_test/cmake-out -type f -name "*.a" | sort
```

The output lists approximately 13 libraries, including `libexecutorch.a`, `libexecutorch_core.a`, `libexecutorch_delegate_ethos_u.a`, `libcortex_m_ops_lib.a`, and `libcmsis-nn.a`.
