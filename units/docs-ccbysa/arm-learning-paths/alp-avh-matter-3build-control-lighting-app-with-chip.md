---
id: "alp-avh-matter-3build-control-lighting-app-with-chip"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Build and run Matter examples on Arm Virtual Hardware: Control lighting-app with chip-tool"
summary: "The lighting-app can now be controlled with chip-tool, simulating remote control of a light bulb."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/3build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/3build/#control-lighting-app-with-chip-tool"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `lighting-app` can now be controlled with `chip-tool`, simulating remote control of a light bulb.

In the `chip-tool` instance, send a message to turn the light ON, using the command:
```console
./out/debug/chip-tool onoff on 0x11 1
```
Observe in the `lighting-app` log (you may need to scroll back a little) that this state is reflected with:
```output
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Toggle ep1 on/off from state 0 to 1
[TIMESTAMP][INSTANCEID] CHIP:ZCL: On Command - OffWaitTime :  0
```
Similarly to turn the light OFF, in the `chip-tool` instance use:
```console
./out/debug/chip-tool onoff off 0x11 1
```
And observe in the `lighting-app` log:
```output
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Toggle ep1 on/off from state 1 to 0
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Setting on/off to OFF due to level change
```
Congratulations! You have successfully enabled two Virtual Hardware instances to communicate to each other via `Matter`.
