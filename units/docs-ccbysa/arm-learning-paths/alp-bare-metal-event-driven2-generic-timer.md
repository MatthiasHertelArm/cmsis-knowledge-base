---
id: "alp-bare-metal-event-driven2-generic-timer"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (2): Generic Timer"
summary: "A Generic Timer is present in all Armv8-A processors."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2/#generic-timer"
license: "CC-BY-SA-4.0"
mode: "V"
---

A [Generic Timer](https://developer.arm.com/documentation/102379) is present in all Armv8-A processors.

Create `timer.s` defining the following functions:
* `setTimerPeriod()` which writes to [CNTPS_TVAL_EL1, Counter-timer Physical Secure Timer TimerValue register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/CNTPS-TVAL-EL1--Counter-timer-Physical-Secure-Timer-TimerValue-Register).
* `enableTimer()` and `disableTimer()` which write to [CNTPS_CTL_EL1, Counter-timer Physical Secure Timer Control register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/CNTPS-CTL-EL1--Counter-timer-Physical-Secure-Timer-Control-Register).

#### timer.s
```C
	.section  AArch64_GenericTimer,"ax"

	.global setTimerPeriod
	.type setTimerPeriod, "function"
setTimerPeriod:
	MSR     CNTPS_TVAL_EL1, x0
	ISB
	RET
// ------------------------------------------------------------
	.global enableTimer
	.type enableTimer, "function"
enableTimer:
	MOV    x0, #0x1            // Set Enable bit, and clear Mask bit
	MSR    CNTPS_CTL_EL1, x0
	ISB
	RET
// ------------------------------------------------------------
	.global disableTimer
	.type disableTimer, "function"
disableTimer:
	MSR    CNTPS_CTL_EL1, xzr // Clear the enable bit
	ISB
	RET
```
