---
id: "alp-bare-metal-hello-enable-single-core-simulation"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create and build a Hello World example project: Enable single core simulation"
summary: "The FVP can be configured so that only one processor is running at start up."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/hello.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/hello/#enable-single-core-simulation"
license: "CC-BY-SA-4.0"
mode: "V"
---

The FVP can be configured so that only one processor is running at start up.
```command
FVP_Base_AEMvA -a hello.axf -C pctl.startup=0.0.0.1
```
In this case, only one instance of the output is shown:
```output
Hello World!
```
In the next section you'll learn how to manage this in software.
