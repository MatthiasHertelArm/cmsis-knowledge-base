---
id: "alp-observing-ethos-u-on-alif-8-flash-and-run-build-the-project-using-the-vs"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Flash and run the project on the Alif Ensemble E8 DevKit: Build the project using the VS"
summary: "First, clear any cached build files present from previous runs:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/8-flash-and-run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/8-flash-and-run/#build-the-project-using-the-vs-code-cmsis-extension"
license: "CC-BY-SA-4.0"
mode: "V"
---

First, clear any cached build files present from previous runs:


  **macOS and Linux:**
  cd ~/mnist_alif/alif_vscode-template
  rm -rf tmp/ out/
  

  **Windows (PowerShell):**
  cd "$HOME\mnist_alif\alif_vscode-template"
  Remove-Item -Recurse -Force .\tmp, .\out -ErrorAction SilentlyContinue
  


CMSIS Toolbox caches aggressively and won’t pick up YAML configuration changes unless you clean first.

Next, to build the project in VS Code:

1. Select the **CMSIS** icon in the left sidebar.
2. Select the gear icon.
3. Set **Active Target** to **E8-HP**.
4. Set **Active Project** to **mnist_executorch**.
5. Select the **Build** hammer icon.

A successful build prints a memory report similar to:

```output
Memory region         Used Size  Region Size  %age Used
            ITCM:      149232 B       256 KB     56.93%
            DTCM:        256 KB       256 KB    100.00%
           SRAM0:       2576 KB         4 MB     62.89%
           SRAM1:          2 MB         4 MB     50.00%
            MRAM:      291008 B         2 MB     13.88%
```
