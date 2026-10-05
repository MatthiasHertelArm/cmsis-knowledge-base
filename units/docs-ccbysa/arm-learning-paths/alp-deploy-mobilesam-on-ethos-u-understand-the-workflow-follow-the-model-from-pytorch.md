---
id: "alp-deploy-mobilesam-on-ethos-u-understand-the-workflow-follow-the-model-from-pytorch"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Understand the MobileSAM deployment workflow: Follow the model from PyTorch to the target"
summary: "You'll run an ExecuTorch MobileSAM example that performs the following sequence:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow/#follow-the-model-from-pytorch-to-the-target"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll run an ExecuTorch MobileSAM example that performs the following sequence:

1. Downloads the pinned MobileSAM `vit_t` source and checkpoint.
2. Embeds the positive point `(219, 193)` into the exported model.
3. Calibrates post-training quantization with the example dog image.
4. Uses 8-bit activations and weights for most of the graph, with 16-bit activations and 8-bit weights for TinyViT attention.
5. Lowers the quantized graph to an Ethos-U85-256 delegate and writes an ExecuTorch `.pte` program.
6. Builds the standard Arm ExecuTorch runner, runs it on the Corstone-320 FVP, and compares its mask with the host quantized mask.

The default image tensor has shape `[1, 3, 448, 448]`. The model produces one mask-logit tensor with shape `[1, 1, 112, 112]`.
