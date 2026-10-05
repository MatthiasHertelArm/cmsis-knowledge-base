---
id: "alp-alif-image-classification-board-setup-configure-vs-code-settings"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Configure VS Code settings"
summary: "Press Fn+F1, select Preferences: Open User Settings (JSON), and add the following entries."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#configure-vs-code-settings"
license: "CC-BY-SA-4.0"
mode: "V"
---

Press Fn+F1, select **Preferences: Open User Settings (JSON)**, and add the following entries.

Update both paths for your system, including using your username:

```json
{
  "alif.setools.root": "/Users/username/alif/app-release-exec-macos",
  "cortex-debug.JLinkGDBServerPath": "/Applications/SEGGER/JLink/JLinkGDBServerCLExe"
}
```

If you have existing settings, add only the two lines of text inside the existing braces.
