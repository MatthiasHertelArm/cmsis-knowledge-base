---
id: "aig-install-guides-cmsis-toolbox-before-you-begin"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox: Before you begin"
summary: "On Linux, you'll need to install CMake and Ninja. For steps to install CMake, see the CMake install guide."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/cmsis-toolbox.md"
doc_source: "https://learn.arm.com/install-guides/cmsis-toolbox/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

On Linux, you'll need to install `CMake` and `Ninja`. For steps to install `CMake`, see the [CMake install guide](https://learn.arm.com/install-guides/cmake/).

To install `Ninja`, run:

```command
sudo apt update
sudo apt install ninja-build -y
```

Check the versions of each tool:

```command
cmake --version
ninja --version
```

Ensure that the version of `CMake` is at least `3.25.2`, and `Ninja` is at least `1.10.2`.

You can also download installers for all supported hosts:

* [CMake](https://cmake.org/download/)
* [Ninja](https://github.com/ninja-build/ninja/releases)
