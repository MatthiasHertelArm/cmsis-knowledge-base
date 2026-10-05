---
id: "aig-gcc-arm-gnu-install-the-arm-gnu-toolchain"
type: "concept"
domain: "project"
title: "Arm GNU Toolchain: Install the Arm GNU Toolchain on Linux"
summary: "Unpack the downloaded file to the install directory. The exact file name will depend on the flavor selected and will be formatted as follows:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/gcc/arm-gnu.md"
doc_source: "https://learn.arm.com/install-guides/gcc/arm-gnu/#install-the-arm-gnu-toolchain-on-linux"
license: "CC-BY-SA-4.0"
mode: "V"
---

Unpack the downloaded file to the install directory. The exact file name will depend on the flavor selected and will be formatted as follows:

```console
tar xJf arm-gnu-toolchain-<version>-<host-arch>-<TRIPLE>.tar.xz -C /path/to/install/dir
```

Add the `bin` directory to the `PATH` environment variable (bash):
```console
export PATH=/path/to/install/dir/bin:$PATH
```

The following is an example of a specific version for an Arm Linux host and the AArch32 bare-metal target:

**Note:**
The following commands uses Arm GNU Toolchain version 15.2.Rel1. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Arm GNU Toolchain downloads](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).


```bash { target="ubuntu:latest" }
wget https://developer.arm.com/-/media/Files/downloads/gnu/15.2.rel1/binrel/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi.tar.xz
tar xJf arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi.tar.xz -C $HOME
echo 'export PATH="$PATH:$HOME/arm-gnu-toolchain-15.2.rel1-aarch64-arm-none-eabi/bin"' >> ~/.bashrc
source ~/.bashrc
```
