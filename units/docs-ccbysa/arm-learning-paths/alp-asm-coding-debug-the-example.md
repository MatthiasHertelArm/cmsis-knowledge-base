---
id: "alp-asm-coding-debug-the-example"
type: "concept"
domain: "project"
title: "Write Arm Assembler functions: Writing assembly functions: Debug the example"
summary: "Click the Debug icon to load the example to the FVP. The code will stop at main()."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/asm/coding.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/asm/coding/#debug-the-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Click the `Debug` icon to load the example to the FVP. The code will stop at `main()`.

Observe the values of `a` and `b` in the μVision `Call Stack + Locals` tab, or the Keil Studio `Watch` pane (click `+` to add to this view).

Initially they will have no meaningful data.

`Step` through the code and notice how the values of `a` and `b` change. Observe the string `Hello world!` copy to `b` and then capitalize.
