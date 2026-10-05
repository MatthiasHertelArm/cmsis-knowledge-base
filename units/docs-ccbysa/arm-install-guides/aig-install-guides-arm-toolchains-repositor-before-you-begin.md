---
id: "aig-install-guides-arm-toolchains-repositor-before-you-begin"
type: "concept"
domain: "project"
title: "Arm Toolchains repository: Before you begin"
summary: "You need root or sudo permissions to install system packages."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/arm-toolchains-repository.md"
doc_source: "https://learn.arm.com/install-guides/arm-toolchains-repository/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

You need root or `sudo` permissions to install system packages.

Confirm you are using an Arm Linux system by running:

```bash
uname -m
```

The output is similar to:

```output
aarch64
```

Use the native package manager for your distribution:

- `apt` for Ubuntu LTS releases from 22.04
- `dnf` or `yum` for RHEL 8 or later and Amazon Linux 2023
- `zypper` for SLES 15 or 16
