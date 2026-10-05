---
id: "alp-armds-misc-use-a-different-compiler-versi"
type: "concept"
domain: "project"
title: "Get started with Arm Development Studio: Other compilers and project types: Use a different compiler version than the default"
summary: "Development Studio installs with the latest Arm Compiler for Embedded version available at the time of its release."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/armds/misc.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/armds/misc/#use-a-different-compiler-version-than-the-default"
license: "CC-BY-SA-4.0"
mode: "V"
---

Development Studio installs with the latest [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) version available at the time of its release. It may be that you need to use a specific compiler version for your project (particularly common if the [Arm Compiler for Embedded FuSa](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded%20FuSa) is needed).

Refer to the [Arm Compiler for Embedded install guide](https://learn.arm.com/install-guides/armclang/) to learn how to install different versions of the compiler.

To change the compiler version used for a project, right-click on the project, and select `Properties` (or from the menu, select `Project > Properties`), then `C/C++ Build > Tool Chain Editor`, and select the appropriate compiler version from the `Current toolchain` pulldown. Click `Apply and Close`, and rebuild the project.
