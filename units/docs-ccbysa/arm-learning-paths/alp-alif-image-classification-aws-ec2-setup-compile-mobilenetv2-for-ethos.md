---
id: "alp-alif-image-classification-aws-ec2-setup-compile-mobilenetv2-for-ethos"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Compile MobileNetV2 for Ethos"
summary: "The flags are: - -m mv2: MobileNetV2 model - -q: quantize the model (int8) - -d: delegate computation to the NPU - -t ethos-u85-256: target the Ethos-U85 with 256 MAC configuration - -o: output path for the compiled .pte file"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#compile-mobilenetv2-for-ethos-u85"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the ahead-of-time compiler:

```bash
mkdir -p ~/alif/models

python -m examples.arm.aot_arm_compiler \
  -m mv2 \
  -q \
  -d \
  -t ethos-u85-256 \
  -o ~/alif/models/mv2_ethosu85_256.pte
```

The flags are:
- `-m mv2`: MobileNetV2 model
- `-q`: quantize the model (int8)
- `-d`: delegate computation to the NPU
- `-t ethos-u85-256`: target the Ethos-U85 with 256 MAC configuration
- `-o`: output path for the compiled `.pte` file

Verify the output:

```bash
ls -lh ~/alif/models/mv2_ethosu85_256.pte
```

The file should be approximately 3.7 MB. This `.pte` file contains the model graph, quantized weights, and the Vela-compiled command stream that the Ethos-U85 executes directly.
