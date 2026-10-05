---
id: "alp-bare-metal-exception-levels"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Switching Exception Levels"
summary: "So far, everything has been at the most privileged EL3 exception level, which the processor starts in at reset."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/exception-levels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/exception-levels/"
license: "CC-BY-SA-4.0"
mode: "V"
---

So far, everything has been at the most privileged `EL3` exception level, which the processor starts in at reset.

In general, you would want your application code to run at a lower level so that it cannot corrupt system settings, maliciously or otherwise.

Switching between levels is performed by the `ERET` exception return instruction.
