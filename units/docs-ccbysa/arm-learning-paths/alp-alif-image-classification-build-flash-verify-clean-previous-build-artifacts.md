---
id: "alp-alif-image-classification-build-flash-verify-clean-previous-build-artifacts"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Build, flash, and verify inference: Clean previous build artifacts"
summary: "If you've built other projects (like Blinky), delete the cached build files. CMSIS Toolbox caches aggressively and won't pick up YAML configuration changes unless you clean first:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify/#clean-previous-build-artifacts"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you've built other projects (like Blinky), delete the cached build files. CMSIS Toolbox caches aggressively and won't pick up YAML configuration changes unless you clean first:

```bash
cd ~/alif/alif_vscode-template
rm -rf tmp/ out/
```

You can also clean from VS Code: press **F1** and select **CMSIS: Clean all out and tmp directories**.
