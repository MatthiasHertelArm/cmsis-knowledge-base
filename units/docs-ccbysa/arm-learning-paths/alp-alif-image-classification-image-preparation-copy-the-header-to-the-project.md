---
id: "alp-alif-image-classification-image-preparation-copy-the-header-to-the-project"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Prepare a test image: Copy the header to the project"
summary: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Prepare a test image: Copy the header to the project"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation/#copy-the-header-to-the-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

```bash
cp ~/alif/image/input_image.h \
   ~/alif/alif_vscode-template/mv2_runner/assets/
```

**Note:**
The image data is stored as int8 in the header, but the model expects float32 input. The application code handles this conversion at runtime. The model's first operator (`cortex_m::quantize_per_tensor`) then re-quantizes the float values back to int8 for the NPU. Storing as int8 in the header saves approximately 450 KB of flash compared to storing as float32.
