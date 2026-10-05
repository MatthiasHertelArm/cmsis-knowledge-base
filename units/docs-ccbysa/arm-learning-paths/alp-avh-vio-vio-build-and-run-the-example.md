---
id: "alp-avh-vio-vio-build-and-run-the-example"
type: "concept"
domain: "edge-ai"
title: "Implement an example Virtual Peripheral with Arm Virtual Hardware: Create a peripheral using Virtual Input/Output (VIO): Build and run the example"
summary: "A makefile is provided to build the example project. To build the example:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_vio/vio.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_vio/vio/#build-and-run-the-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

A makefile is provided to build the example project. To build the example:
```console
make
```
You can now run the executable on the AVH FVP by executing the following script:
```console
./run.sh
```
You can interact with the Virtual LEDs. If they're not displayed you may need to implement a [VNC connection](https://learn.arm.com/install-guides/avh/#vnc) to the AVH instance.
