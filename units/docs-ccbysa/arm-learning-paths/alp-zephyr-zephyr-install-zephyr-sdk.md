---
id: "alp-zephyr-zephyr-install-zephyr-sdk"
type: "concept"
domain: "rtos"
title: "Run the Zephyr RTOS on Arm Corstone-300: Build and run Zephyr applications: Install Zephyr SDK"
summary: "You need the Zephyr Software Development Kit (SDK) to build Zephyr applications."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr/zephyr.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr/zephyr/#install-zephyr-sdk"
license: "CC-BY-SA-4.0"
mode: "V"
---

You need the Zephyr Software Development Kit (SDK) to build Zephyr applications.

It contains the compiler, assembler, linker and other programs needed for building Zephyr applications. 

Download, verify, extract and setup the Zephyr SDK bundle, downloadable from the [Zephyr project on GitHub](https://github.com/zephyrproject-rtos/sdk-ng/releases). The instructions shown in this learning path are with version v0.16.0 of the SDK. 

```bash { env_source="/shared/zephyrproject/.venv/bin/activate" }
cd ~
wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.0/zephyr-sdk-0.16.0_linux-x86_64.tar.xz
tar -xf zephyr-sdk-0.16.0_linux-x86_64.tar.xz
cd zephyr-sdk-0.16.0
./setup.sh -t all
cd ~
```
