---
id: "alp-pqc-pqm4-setup-installation-configure-qemu"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Set up the pqm4 development environment: Configure QEMU"
summary: "If you're using QEMU instead of a physical board, follow these steps:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/setup-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/setup-installation/#configure-qemu"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you're using QEMU instead of a physical board, follow these steps:

### Install QEMU

Install QEMU to simulate a Cortex-M4 environment using the `mps2-an386` machine type.

On macOS:

```bash
brew install qemu
```

On Linux:

```bash
sudo apt-get install qemu-system-arm -y
```

### Build for a target platform

Build pqm4 by specifying the platform identifier for QEMU simulation using the `PLATFORM` variable:

```bash
make -j4 PLATFORM=mps2-an386
```

For a full list of supported platforms, see the [pqm4 README](https://github.com/mupq/pqm4).

Communication with QEMU is covered in the next section.
