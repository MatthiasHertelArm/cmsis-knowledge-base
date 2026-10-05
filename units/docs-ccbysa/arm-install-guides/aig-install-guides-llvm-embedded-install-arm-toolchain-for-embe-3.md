---
id: "aig-install-guides-llvm-embedded-install-arm-toolchain-for-embe-3"
type: "concept"
domain: "project"
title: "Arm Toolchain for Embedded: Install Arm Toolchain for Embedded on Linux"
summary: "The following steps assume Ubuntu Linux on an AArch64 host. Modify the filenames and paths as needed for other hosts or x86_64 systems."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/llvm-embedded.md"
doc_source: "https://learn.arm.com/install-guides/llvm-embedded/#install-arm-toolchain-for-embedded-on-linux"
license: "CC-BY-SA-4.0"
mode: "V"
---

The following steps assume Ubuntu Linux on an AArch64 host. Modify the filenames and paths as needed for other hosts or x86_64 systems.

Download the latest release using `wget`:

```command
wget https://github.com/arm/arm-toolchain/releases/download/release-22.1.0-ATfE/ATfE-22.1.0-Linux-AArch64.tar.xz
```

Use `tar` to extract the file:

```command
tar xfJ ATfE-22.1.0-Linux-AArch64.tar.xz -C $HOME
```

Add the ATfE `bin` directory to your `PATH`:

```command
export PATH=$HOME/ATfE-22.1.0-Linux-AArch64/bin:$PATH
```
