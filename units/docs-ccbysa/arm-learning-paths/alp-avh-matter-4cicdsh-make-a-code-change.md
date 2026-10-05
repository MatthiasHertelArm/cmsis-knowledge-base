---
id: "alp-avh-matter-4cicdsh-make-a-code-change"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Manage development in a CI/CD workflow with Self-Hosted Runner: Make a code change"
summary: "In the lighting-app console, make a code change, for example, editing the output message when light is toggled."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/4cicdsh/#make-a-code-change"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the `lighting-app` console, make a code change, for example, editing the output message when light is toggled.

This is in a source file named `on-off-server.cpp`.
```console 
cd ~/connectedhomeip
nano src/app/clusters/on-off-server/on-off-server.cpp
```
Locate the `Toggle on/off` message (if using `nano`, use `Ctrl+_` to jump to line `175`):
```C
    emberAfOnOffClusterPrintln("Toggle ep%x on/off from state %x to %x", endpoint, currentValue, newValue);
```
Edit to give a new output message, for example:
```C
    emberAfOnOffClusterPrintln("HELLO WORLD! Toggle ep%x on/off from state %x to %x", endpoint, currentValue, newValue);
```
Exit (`Ctrl+X`) and save your change.
