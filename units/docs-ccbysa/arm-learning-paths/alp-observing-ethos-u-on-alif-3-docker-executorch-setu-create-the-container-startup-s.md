---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-create-the-container-startup-s"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: (Optional) Set up a Docker development environment: Create the container startup script"
summary: "After building the image, create the container startup script:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#create-the-container-startup-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

After building the image, create the container startup script:


  **macOS and Linux:**
cat > start-dev.sh << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
docker run -it --rm --name executorch-alif-dev -v "${SCRIPT_DIR}/models:/home/developer/models" -v "${SCRIPT_DIR}/output:/home/developer/output" -w /home/developer executorch-alif:latest /bin/bash
EOF
chmod +x start-dev.sh
  

  **Windows (PowerShell):**
@'
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
docker run -it --rm --name executorch-alif-dev -v "${ScriptDir}/models:/home/developer/models" -v "${ScriptDir}/output:/home/developer/output" -w /home/developer executorch-alif:latest /bin/bash
'@ | Set-Content -Encoding ascii .\start-dev.ps1
