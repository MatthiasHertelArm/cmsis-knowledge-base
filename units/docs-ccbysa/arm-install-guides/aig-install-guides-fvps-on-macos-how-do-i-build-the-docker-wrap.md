---
id: "aig-install-guides-fvps-on-macos-how-do-i-build-the-docker-wrap"
type: "concept"
domain: "project"
title: "AVH FVPs on macOS: How do I build the Docker wrapper for AVH FVPs?"
summary: "Run the build script to create the Docker image and populate the bin folder with model wrappers:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fvps-on-macos.md"
doc_source: "https://learn.arm.com/install-guides/fvps-on-macos/#how-do-i-build-the-docker-wrapper-for-avh-fvps"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the build script to create the Docker image and populate the `bin` folder with model wrappers:

```sh
./build.sh
```


When this completes, inspect the created `bin` folder containing symlinks to `fvp.sh`.
These wrappers can be used exactly like any native model executable:

```sh
./bin/FVP_MPS2_Cortex-M3 --version
```
