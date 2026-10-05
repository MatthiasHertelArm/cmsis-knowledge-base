---
id: "alp-bare-metal-event-driven1"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (1)"
summary: "Embedded systems typically monitor inputs waiting for an event, which then triggers a response by the system. You need to write code that listens for these events and acts on them."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Embedded systems typically monitor inputs waiting for an event, which then triggers a response by the system. You need to write code that listens for these events and acts on them. With Armv8-A, enable asynchronous exceptions (`IRQs`, `FIQs`, and `SErrors`) which are taken when the processor needs to handle an event outside to the current flow of execution.

For example, a thermostat might monitor room temperature until it drops below a specified threshold. When the threshold is reached, the system must turn on the heating system.
