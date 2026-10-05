---
id: "alp-avh-matter-3build-build-the-examples"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Build and run Matter examples on Arm Virtual Hardware: Build the examples"
summary: "In the first Virtual Hardware instance you'll build chip-tool, a Matter controller implementation that allows to commission a Matter device into the network and to communicate with it using Matter messages."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/3build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/3build/#build-the-examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

You're now ready to build the examples.

In the first Virtual Hardware instance you'll build `chip-tool`, a Matter controller implementation that allows to commission a Matter device into the network and to communicate with it using Matter messages.
```console
cd examples/chip-tool
gn gen out/debug
ninja -C out/debug
```
Full [documentation](https://github.com/project-chip/connectedhomeip/tree/master/examples/chip-tool) for `chip-tool` is provided in the repository.

In the other instance you'll build the reference `lighting-app` for Linux, which will be controlled by the above `chip-tool`.
```console
cd examples/lighting-app/linux
gn gen out/debug
ninja -C out/debug
```
Full [documentation](https://github.com/project-chip/connectedhomeip/tree/master/examples/lighting-app/linux) for `lighting-app` is provided in the repository.

Again, these builds can be performed in parallel. Confirm that both builds complete.
