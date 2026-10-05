---
id: "alp-bare-metal-event-driven2"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (2)"
summary: "Vector tables have a relatively small and fixed number of entries. A real system will likely require many different interrupts, triggered by different sources. An additional piece of hardware is needed to manage these interrupts."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Vector tables have a relatively small and fixed number of entries. A real system will likely require many different interrupts, triggered by different sources. An additional piece of hardware is needed to manage these interrupts. The [Arm Generic Interrupt Controller, GIC](https://developer.arm.com/Architectures/Generic%20Interrupt%20Controller) does exactly this.
