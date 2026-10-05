---
id: "alp-deploy-mobilesam-on-ethos-u"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch"
summary: "Export, deploy, and validate a quantized MobileSAM prompt segmentation model on an Arm Ethos-U85 Fixed Virtual Platform using ExecuTorch."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Export, deploy, and validate a quantized MobileSAM prompt segmentation model on an Arm Ethos-U85 Fixed Virtual Platform using ExecuTorch.

**Who is this for:** This Learning Path is for embedded machine learning developers who want to evaluate transformer-based image segmentation on an Arm Ethos-U85 NPU with ExecuTorch.

**Learning objectives:**

- Identify how the MobileSAM example turns a fixed point prompt and an image into a quantized segmentation mask
- Set up ExecuTorch and the Arm Ethos-U development tools
- Export, build, and run the MobileSAM example on a Corstone-320 Fixed Virtual Platform (FVP)
- Validate quantization quality, Ethos-U delegation, and target mask agreement

**Prerequisites:**

- A Linux development machine with glibc 2.28 or later, or an Apple silicon Mac running macOS 15 or later
- Familiarity with PyTorch model export and embedded cross-compilation

**Steps:**

1. Understand the MobileSAM deployment workflow
2. Prepare the ExecuTorch and Arm environment
3. Export MobileSAM for Ethos-U85
4. Build and run MobileSAM on the Corstone-320 FVP
5. Validate the MobileSAM segmentation result

Time: about 45 minutes.
