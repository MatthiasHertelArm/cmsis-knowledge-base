---
id: "alp-pqc-pqm4-setup-installation-download-and-install-dependenc"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Set up the pqm4 development environment: Download and install dependencies for pqm4"
summary: "In this section, you'll install all dependencies needed to build and run pqm4."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/setup-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/setup-installation/#download-and-install-dependencies-for-pqm4"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you'll install all dependencies needed to build and run pqm4. 

You'll need Python 3.8 or higher on your host machine. You'll also need one of the following to run pqm4:

- A physical Arm Cortex-M4 development board such as NUCLEO-L4R5ZI (the pqm4 default), NUCLEO-L476RG, or STM32F4 Discovery, plus stlink or OpenOCD for flashing
- QEMU, if you want to simulate a Cortex-M4 environment using the `mps2-an386` platform without physical hardware

After downloading and installing dependencies, follow the steps to configure either a physical board or QEMU. 

### Install the Arm GNU Toolchain

Follow the [Arm GNU Toolchain install guide](https://learn.arm.com/install-guides/gcc/arm-gnu/) to install `arm-none-eabi-gcc` on your host machine.

**Note:**
Use toolchain version 12.x. Other versions may work but have not been tested.


Verify the installation by running:

```bash
arm-none-eabi-gcc --version
```

The output is similar to:

```output
arm-none-eabi-gcc (Arm GNU Toolchain 12.3.Rel1) 12.3.1 20230626
Copyright (C) 2022 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
### Download pqm4 and submodules

Clone the pqm4 repository including all submodules:

```bash
git clone --recursive https://github.com/mupq/pqm4.git
cd pqm4
```

### Install Python dependencies

Create a virtual environment inside the pqm4 directory and install the required modules:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pyserial tqdm
```

Activate the virtual environment each time you open a new terminal before running pqm4 Python scripts:

```bash
source venv/bin/activate
```
