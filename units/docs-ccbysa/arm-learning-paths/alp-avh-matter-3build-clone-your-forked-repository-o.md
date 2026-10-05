---
id: "alp-avh-matter-3build-clone-your-forked-repository-o"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Build and run Matter examples on Arm Virtual Hardware: Clone your forked repository on your Raspberry Pi 4 AVH ins"
summary: "Return to the Console tab of each of your Virtual Hardware instances, and clone your fork of the repository."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/3build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/3build/#clone-your-forked-repository-on-your-raspberry-pi-4-avh-instances"
license: "CC-BY-SA-4.0"
mode: "V"
---

Return to the `Console` tab of each of your Virtual Hardware instances, and clone your fork of the repository.
```console
git clone https://github.com/YOUR_GITHUB_USERNAME/connectedhomeip
cd connectedhomeip
```
A number of submodules must also be cloned, which can be done with a provided script:
```console
./scripts/checkout_submodules.py --shallow --platform linux
```
Repeat on other Virtual Hardware instance. You can set up each instance in parallel.
