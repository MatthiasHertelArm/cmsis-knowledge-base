---
id: "aig-gcc-arm-gnu-verify-the-installation"
type: "concept"
domain: "project"
title: "Arm GNU Toolchain: Verify the installation"
summary: "To verify the installation is correct, enter:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/gcc/arm-gnu.md"
doc_source: "https://learn.arm.com/install-guides/gcc/arm-gnu/#verify-the-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

To verify the installation is correct, enter:
```console
arm-none-eabi-gcc -v
```

Additional examples are included in the toolchain installation. If you installed to `$HOME` using the example provided in this guide, you can find them at:
```console
$HOME/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi/share/gcc-arm-none-eabi/samples
```
You're now ready to use Arm GNU Toolchain.
