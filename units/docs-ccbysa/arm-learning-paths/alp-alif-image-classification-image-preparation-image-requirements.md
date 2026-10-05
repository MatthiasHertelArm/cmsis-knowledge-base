---
id: "alp-alif-image-classification-image-preparation-image-requirements"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Prepare a test image: Image requirements"
summary: "MobileNetV2 expects a specific input format:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation/#image-requirements"
license: "CC-BY-SA-4.0"
mode: "V"
---

MobileNetV2 expects a specific input format:

- **Resolution**: 224 x 224 pixels
- **Color**: RGB (3 channels)
- **Normalization**: ImageNet mean/std
- **Layout**: NCHW at runtime (`1 x 3 x 224 x 224`). The generated header stores the image in CHW order.
- **Data type**: int8 (stored in the header, converted to float32 at runtime)

You use a Python script to convert any JPEG or PNG image into a C header that the firmware includes at compile time.
