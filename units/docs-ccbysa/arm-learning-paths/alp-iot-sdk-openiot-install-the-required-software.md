---
id: "alp-iot-sdk-openiot-install-the-required-software"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Build and run Open-IoT-SDK examples: Install the required software"
summary: "In your AVH instance, install the required python software:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/openiot.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/openiot/#install-the-required-software"
license: "CC-BY-SA-4.0"
mode: "V"
---

In your AVH instance, install the required python software:

```console
sudo apt update
sudo apt install python3.8-venv -y
sudo cp /usr/local/bin/pip3.8 /usr/bin
```

Install Python packages:

```console
python3.8 -m pip install imgtool cbor2
python3.9 -m pip install imgtool cffi intelhex cbor2 cbor pytest click
```

Modify the `PATH` environment variable to make python user packages visible in the shell:

```console
export PATH=$PATH:/home/ubuntu/.local/bin
```
