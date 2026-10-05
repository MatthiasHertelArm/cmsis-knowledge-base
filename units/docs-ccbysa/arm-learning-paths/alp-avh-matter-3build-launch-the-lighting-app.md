---
id: "alp-avh-matter-3build-launch-the-lighting-app"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Build and run Matter examples on Arm Virtual Hardware: Launch the lighting-app"
summary: "In the lighting-app instance, run that application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/3build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/3build/#launch-the-lighting-app"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the `lighting-app` instance, run that application.
```console
./out/debug/chip-lighting-app
```
The application will initialize, and you'll see the boot log echoed in the console. You'll see in the log:
```output
[TIMESTAMP][INSTANCEID] CHIP:DL: PlatformBlueZInit init success
```
Confirming it's ready to use (other messages in the log can be ignored).

Leave the `lighting-app` application running on this instance.
