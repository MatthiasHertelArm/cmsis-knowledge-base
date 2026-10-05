---
id: "alp-deploy-mobilesam-on-ethos-u-understand-the-workflow-what-you-ll-run"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Understand the MobileSAM deployment workflow: What you'll run"
summary: "MobileSAM is a compact variant of the Segment Anything Model. It takes an image and point prompts, then predicts a binary mask for the object selected by those points."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/understand-the-workflow/#what-you-ll-run"
license: "CC-BY-SA-4.0"
mode: "V"
---

MobileSAM is a compact variant of the Segment Anything Model. It takes an image and point prompts, then predicts a binary mask for the object selected by those points.

You'll run the ExecuTorch MobileSAM example on a Corstone-320 Fixed Virtual Platform (FVP). The system combines a Cortex-M85 processor with an Ethos-U85 neural processing unit (NPU). This lets you test the complete bare-metal deployment without a physical board.
