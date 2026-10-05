---
id: "alp-tfm-tfm-prerequisites"
type: "concept"
domain: "core"
title: "Configure, build and run the TF-M example application: Prerequisites"
summary: "TF-M can be built with Arm Compiler for Embedded or Arm GNU Toolchain."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tfm/tfm.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tfm/tfm/#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

Ensure the system is up to date:

```bash
sudo apt update
```

### Corstone-300 FVP
The Corstone-300 FVP is available from the [Arm Ecosystem FVP](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) page and can be installed following the instructions from the [install guide](https://learn.arm.com/install-guides/fm_fvp/).

### Compiler

TF-M can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

To install locally follow the instructions from:
- [Arm Compiler for Embedded](https://learn.arm.com/install-guides/armclang/) or
- [Arm GNU Toolchain](https://learn.arm.com/install-guides/gcc/arm-gnu/)

### Build system

TF-M uses `cmake` as the build system, and TF-M tests require `cmake` > 3.21 or higher.

On Ubuntu 22.04-LTS, `cmake` can be installed if necessary with:

```bash
sudo apt install -y cmake
```

### Clone the TF-M repositories

Clone the TF-M repositories that need and pin them to version `2.0.0` :

```bash
git clone -b TF-Mv2.0.0 https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git
git clone -b TF-Mv2.0.0 https://git.trustedfirmware.org/TF-M/tf-m-tests.git
git clone -b TF-Mv2.0.0 https://git.trustedfirmware.org/TF-M/tf-m-extras.git
```

### Python packages

Install `python 3` prerequisites for TF-M in a virtual environment in order not to clutter your system:

```bash
sudo apt install -y python3-venv python3-pip
python3 -m venv myvenv
myvenv/bin/pip3 install -r trusted-firmware-m/tools/requirements.txt
```
