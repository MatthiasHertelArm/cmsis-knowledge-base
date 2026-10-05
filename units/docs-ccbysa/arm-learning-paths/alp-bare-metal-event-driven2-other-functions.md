---
id: "alp-bare-metal-event-driven2-other-functions"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (2): Other functions"
summary: "Define these functions in your gic.s source:  readIAR0() reads the value of the Interrupt Controller Interrupt Acknowledge Register 0, ICC_IAR0_EL1. The lower 24 bits of this register give the interrupt identifier, INTID."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2/#other-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

Define these functions in your `gic.s` source:
* `readIAR0()` reads the value of the [Interrupt Controller Interrupt Acknowledge Register 0, ICC_IAR0_EL1](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/ICC-IAR0-EL1--Interrupt-Controller-Interrupt-Acknowledge-Register-0). The lower 24 bits of this register give the interrupt identifier, `INTID`.
* `writeEOIR0()` writes `INTID` to the [Interrupt Controller End of Interrupt Register 0, ICC_EOIR0_EL1](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/ICC-EOIR0-EL1--Interrupt-Controller-End-Of-Interrupt-Register-0), which tells the processor that that interrupt is complete.

#### gic.s
```C
// ------------------------------------------------------------
	.global readIAR0
	.type readIAR0, "function"
readIAR0:
	MRS       x0, ICC_IAR0_EL1  // Read ICC_IAR0_EL1 into x0
	RET

// ------------------------------------------------------------
	  .global writeEOIR0
	  .type writeEOIR0, "function"
writeEOIR0:
	MSR        ICC_EOIR0_EL1, x0 // Write x0 to ICC_EOIR0_EL1
	RET
```
These functions will be used in your `fiqHandler()` implementation (written in C).
