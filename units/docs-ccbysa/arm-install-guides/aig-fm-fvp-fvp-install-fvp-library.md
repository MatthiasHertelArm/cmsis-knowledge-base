---
id: "aig-fm-fvp-fvp-install-fvp-library"
type: "concept"
domain: "project"
title: "Fixed Virtual Platforms (FVP): Install FVP library"
summary: "Unzip the downloaded installation archive."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fm_fvp/fvp.md"
doc_source: "https://learn.arm.com/install-guides/fm_fvp/fvp/#install-fvp-library"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Windows

Unzip the downloaded installation archive.

It is easiest to run the installation wizard (`setup.exe`), and follow on-screen instructions.

### Linux
Unpack the downloaded package, and install the FVP library with the supplied script.
```command
./FVP_ARM_Std_Library.sh --i-agree-to-the-contained-eula --no-interactive
```
For full list of available options, use:
```command
./FVP_ARM_Std_Library.sh --help
```
