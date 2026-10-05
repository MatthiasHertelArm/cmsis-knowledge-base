---
id: "alp-alif-image-classification-board-setup-set-up-vs-code-and-the-alif-te"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Set up VS Code and the Alif template"
summary: "Open the project in VS Code from the alif_vscode-template/ directory:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#set-up-vs-code-and-the-alif-template"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Clone the Alif VS Code template repository

```bash
cd ~/alif
git clone https://github.com/alifsemi/alif_vscode-template.git
cd alif_vscode-template
git checkout 8b1aa0b09eacf68a28850af00c11f0b5af03c100
git submodule update --init
```

**Note:**
The `git checkout` command pins the template to a known-working commit. This avoids breakage if the upstream template is updated.


### Open the project in VS Code

Open the project in VS Code from the `alif_vscode-template/` directory:

```bash
code . &
```

### Install the recommended extensions when prompted

VS Code might prompt you to install the recommended extensions for this workspace. If it does, install the following:

   - Arm CMSIS Solution
   - Arm Tools Environment Manager
   - Cortex-Debug
   - Microsoft C/C++ Extension Pack

When prompted, select **Always Allow** or **Allow for Selected Workspace**.

The recommended VS Code extensions are listed in `.vscode/extensions.json`.

If you don't get an automatic trigger to enable them, you can open the Extensions view and look for a "Workspace Recommendations" section to install or enable them manually.

Restart VS Code if prompted.
