---
id: "alp-edge-software-edge-impulse-review-model-performance"
type: "concept"
domain: "edge-ai"
title: "Learn how to run AI on Edge devices using Arduino Nano RP2040: Train and deploy a TinyML audio classifier with Edge Impulse: Review model performance"
summary: "After training is complete, Edge Impulse displays key performance metrics, including accuracy, loss, and a confusion matrix."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/edge/software-edge-impulse/#review-model-performance"
license: "CC-BY-SA-4.0"
mode: "V"
---

After training is complete, Edge Impulse displays key performance metrics, including **accuracy**, **loss**, and a **confusion matrix**.

(figure: Screenshot showing training results in Edge Impulse, including a confusion matrix and accuracy/loss graph alt-text#center)

- **Accuracy**: how often the model correctly predicts labels  
- **Loss**: how far off the predictions are - lower values indicate better performance  
- **Confusion matrix**: shows how well the model classified each label and where it made errors

Review these results to evaluate how well your model learned. If needed, adjust the configuration or retrain to improve accuracy.

**On-device performance (EON Compiler – RAM optimized):**

| Metric           | Value   |
|------------------|---------|
| Inference time   | 6 ms    |
| Peak RAM usage   | 12.5 KB |
| Flash usage      | 49.7 KB |

(figure: Screenshot showing on-device model performance stats including RAM, flash, and latency alt-text#center)

You can also use the pre-trained model included in `ei-edge-ai-tutorials-arduino-1.0.1.zip` from the example repository.
