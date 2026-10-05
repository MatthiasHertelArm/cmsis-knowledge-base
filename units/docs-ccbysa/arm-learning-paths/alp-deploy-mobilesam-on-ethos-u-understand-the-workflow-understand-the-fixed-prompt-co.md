---
id: "alp-deploy-mobilesam-on-ethos-u-understand-the-workflow-understand-the-fixed-prompt-co"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Understand the MobileSAM deployment workflow: Understand the fixed-prompt contract"
summary: "The exported .pte accepts an image tensor as its only runtime input. The runner embeds the .pte and reads the preprocessed image from input.bin through semihosting, which lets the FVP access files on your host."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow/#understand-the-fixed-prompt-contract"
license: "CC-BY-SA-4.0"
mode: "V"
---

The exported `.pte` accepts an image tensor as its only runtime input. The runner embeds the `.pte` and reads the preprocessed image from `input.bin` through semihosting, which lets the FVP access files on your host. It writes the output tensor to `output-0.bin` through the same mechanism.

You can supply a different image tensor with the same shape and preprocessing without exporting again or rebuilding the runner. The fixed point coordinates must still identify the intended object in the resized and padded image. Validation also needs the host quantized mask and visualization image for that same input. Changing the point coordinates requires a new export and a rebuild of the runner that embeds the program.

The example provides one tested configuration: MobileSAM `vit_t`, a `448x448` image, point `(219, 193)`, and Ethos-U85-256. The MobileSAM preparation, export, and visualization scripts use fixed settings and paths, so you invoke them without configuration arguments.

The example uses `multimask_output=False`. The target returns low-resolution mask logits; the host thresholds them at zero and resizes the binary mask for visualization.
