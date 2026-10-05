---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-create-the-dockerfile"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: (Optional) Set up a Docker development environment: Create the Dockerfile"
summary: "Paste the following in the Dockerfile:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#create-the-dockerfile"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a file named `Dockerfile`:


  **macOS and Linux:**
touch Dockerfile
code Dockerfile
  

  **Windows (PowerShell):**
New-Item -ItemType File -Path .\Dockerfile
notepad .\Dockerfile
  


Paste the following in the `Dockerfile`:

```dockerfile
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y build-essential ca-certificates cmake curl git ninja-build python3 python3-pip python3-venv unzip vim wget xxd xz-utils && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash developer
USER developer
WORKDIR /home/developer
RUN python3 -m venv /home/developer/executorch-venv
RUN /bin/bash -c "source /home/developer/executorch-venv/bin/activate && pip install --upgrade pip setuptools wheel && pip install torch==2.9.0 torchvision==0.24.0 torchaudio==2.9.0 --index-url https://download.pytorch.org/whl/cpu && pip install ethos-u-vela==4.4.1"
ENV VIRTUAL_ENV=/home/developer/executorch-venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD ["/bin/bash"]
```
