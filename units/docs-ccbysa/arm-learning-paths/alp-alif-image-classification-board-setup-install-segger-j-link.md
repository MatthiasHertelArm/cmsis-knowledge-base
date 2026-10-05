---
id: "alp-alif-image-classification-board-setup-install-segger-j-link"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Install SEGGER J-Link"
summary: "SEGGER J-Link provides the debug connection for RTT (Real-Time Transfer) output, which you use later to view inference results."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#install-segger-j-link"
license: "CC-BY-SA-4.0"
mode: "V"
---

SEGGER J-Link provides the debug connection for RTT (Real-Time Transfer) output, which you use later to view inference results.

Install it with Homebrew:

```bash
brew install --cask segger-jlink
```

Alternatively, download it from the [SEGGER website](https://www.segger.com/downloads/jlink/). Run J-Link Commander once after installation to update the on-board probe firmware if needed.
