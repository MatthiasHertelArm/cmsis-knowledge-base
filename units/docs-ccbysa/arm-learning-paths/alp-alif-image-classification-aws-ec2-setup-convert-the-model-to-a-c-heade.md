---
id: "alp-alif-image-classification-aws-ec2-setup-convert-the-model-to-a-c-heade"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Convert the model to a C head"
summary: "The firmware embeds the model as a byte array in flash memory. Use xxd to generate a C header:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#convert-the-model-to-a-c-header"
license: "CC-BY-SA-4.0"
mode: "V"
---

The firmware embeds the model as a byte array in flash memory. Use `xxd` to generate a C header:

```bash
cd ~/alif/models
xxd -i mv2_ethosu85_256.pte > mv2_ethosu85_256_pte.h
```

Open `mv2_ethosu85_256_pte.h` and change the first line from:

```c
unsigned char mv2_ethosu85_256_pte[] = {
```

to:

```c
#include <stdint.h>
const uint8_t __attribute__((aligned(16))) mv2_ethosu85_256_pte[] = {
```

The `aligned(16)` attribute is required because the Ethos-U85 needs the Vela command stream data aligned to 16 bytes. Without it, the NPU driver will report an alignment error at runtime.
