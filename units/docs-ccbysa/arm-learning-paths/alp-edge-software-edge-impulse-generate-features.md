---
id: "alp-edge-software-edge-impulse-generate-features"
type: "concept"
domain: "edge-ai"
title: "Learn how to run AI on Edge devices using Arduino Nano RP2040: Train and deploy a TinyML audio classifier with Edge Impulse: Generate features"
summary: "After saving the MFCC parameters, the next step is to generate features from your dataset. Click Generate features to begin. Edge Impulse will process your data using the MFCC configuration and create a feature set for training."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse/#generate-features"
license: "CC-BY-SA-4.0"
mode: "V"
---

After saving the MFCC parameters, the next step is to generate features from your dataset. Click **Generate features** to begin. Edge Impulse will process your data using the MFCC configuration and create a feature set for training.

When complete, you'll see a **2D feature plot** that shows how the data is distributed across the four labels: `on`, `off`, `noise`, and `unknown`. This helps visually confirm whether the classes are distinct and learnable.

(figure: Screenshot showing the feature explorer in Edge Impulse with a 2D visualization of four labeled audio classes alt-text#center)
