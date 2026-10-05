---
id: "alp-avh-matter-3build-pair-chip-tool"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Build and run Matter examples on Arm Virtual Hardware: Pair chip-tool"
summary: "On the chip-tool instance, pair chip-tool with the lighting-app instance, using:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/3build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/3build/#pair-chip-tool"
license: "CC-BY-SA-4.0"
mode: "V"
---

On the `chip-tool` instance, pair `chip-tool` with the `lighting-app` instance, using:
```console
./out/debug/chip-tool pairing onnetwork-long 0x11 20202021 3840
```
You'll see a long stream of messages echoed in the console of both instances. Wait for this command to complete and return.

If you wish to confirm success, you can see this in the logs (you'll need to scroll back).

In `chip-tool`, you will see:
```
[TIMESTAMP][INSTANCEID] CHIP:TOO: Device commissioning completed with success
```
In `lighting-app`:
```
[TIMESTAMP][INSTANCEID] CHIP:ZCL: Commissioning complete, notify platform driver to persist network credentials.
```
Other messages in the log(s) can be ignored.
