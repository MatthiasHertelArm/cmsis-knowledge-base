---
id: "alp-deploy-mobilesam-on-ethos-u-understand-the-workflow-know-what-the-validation-prove"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Understand the MobileSAM deployment workflow: Know what the validation proves"
summary: "Both comparisons enforce a minimum intersection over union (IoU) of 0.9. Export stops if the host comparison falls below that threshold. The visualization step checks the output tensor size and stops if the target comparison falls below 0.9."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow/#know-what-the-validation-proves"
license: "CC-BY-SA-4.0"
mode: "V"
---

The workflow performs two comparisons:

- Host validation compares the floating-point mask with the quantized mask before lowering.
- Target validation compares the mask produced by the FVP with the host quantized mask.

Both comparisons enforce a minimum intersection over union (IoU) of `0.9`. Export stops if the host comparison falls below that threshold. The visualization step checks the output tensor size and stops if the target comparison falls below `0.9`.

These checks validate agreement across the deployment stages for the example image. The same dog image is used for calibration and evaluation. For an application, use a representative calibration set and labeled test images to assess segmentation quality. The fast FVP mode used here validates correctness; use hardware measurements to assess real-device latency.
