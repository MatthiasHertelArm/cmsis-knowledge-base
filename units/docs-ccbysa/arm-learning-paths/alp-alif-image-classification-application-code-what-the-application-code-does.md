---
id: "alp-alif-image-classification-application-code-what-the-application-code-does"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: What the application code does"
summary: "The application code initializes the Ethos-U85 NPU, loads the MobileNetV2 model through ExecuTorch, runs inference on an embedded test image, and prints the classification result over SEGGER RTT."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#what-the-application-code-does"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application code initializes the Ethos-U85 NPU, loads the MobileNetV2 model through ExecuTorch, runs inference on an embedded test image, and prints the classification result over SEGGER RTT.

Rather than building this code line by line, you download the complete `main.cpp` from a reference repository and walk through its key sections.
