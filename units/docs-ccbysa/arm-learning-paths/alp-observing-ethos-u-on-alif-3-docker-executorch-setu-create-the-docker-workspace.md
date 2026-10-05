---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-create-the-docker-workspace"
type: "concept"
domain: "edge-ai"
title: "3 docker executorch setup: Create the Docker workspace"
summary: "Create a folder for the Docker files, model scripts, and generated output:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#create-the-docker-workspace"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a folder for the Docker files, model scripts, and generated output:


  **macOS and Linux:**
cd ~/mnist_alif
mkdir -p executorch-alif/models executorch-alif/output
cd executorch-alif
  

  **Windows (PowerShell):**
cd ~\mnist_alif
New-Item -ItemType Directory -Force -Path .\executorch-alif\models, .\executorch-alif\output
cd .\executorch-alif
  


The directory will be used as follows:

```text
executorch-alif/
├── Dockerfile
├── start-dev.sh              # macOS/Linux
├── start-dev.ps1             # Windows
├── models/                   # mounted to /home/developer/models
└── output/                   # mounted to /home/developer/output
```
