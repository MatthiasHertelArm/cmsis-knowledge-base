---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-set-up-the-alif-visual-studio"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Set up the Alif Visual Studio Code template"
summary: "Next, you'll need to set up the Alif Visual Studio Code (VS Code) template."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#set-up-the-alif-visual-studio-code-template"
license: "CC-BY-SA-4.0"
mode: "V"
---

Next, you'll need to set up the Alif Visual Studio Code (VS Code) template.

To start, clone the Alif VS Code template repository and check out a known-working commit: 

```bash
cd ~/mnist_alif
git clone https://github.com/alifsemi/alif_vscode-template.git
cd alif_vscode-template
git checkout 8b1aa0b09eacf68a28850af00c11f0b5af03c100
git submodule update --init
```

By checking out a known commit, you can avoid breakage if the template gets updated.

After cloning, open the project in VS Code:

```bash
code .
```
VS Code might prompt you to install the recommended extensions for this workspace. If it does, install the following:

  - Arm CMSIS Solution
  - Arm Tools Environment Manager
  - Cortex-Debug
  - Microsoft C/C++ Extension Pack

When prompted, select **Always Allow** or **Allow for Selected Workspace**.

**Note:**
The recommended VS Code extensions are listed in `.vscode/extensions.json`. If you don’t get an automatic trigger to enable them, you can open the **Extensions** view and look for a **Workspace Recommendations** section to install or enable them manually.


Restart VS Code if prompted.
