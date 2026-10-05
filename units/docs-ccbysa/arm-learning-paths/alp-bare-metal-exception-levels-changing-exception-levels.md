---
id: "alp-bare-metal-exception-levels-changing-exception-levels"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Switching Exception Levels: Changing exception levels"
summary: "Extend the example to make use of EL1."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/exception-levels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/exception-levels/#changing-exception-levels"
license: "CC-BY-SA-4.0"
mode: "V"
---

Extend the example to make use of `EL1`.

Create `startup_el1.s` as below. The `el1_entry` function will be the `EL1` entry point, and this function will call our application code starting from `__main()`.

#### startup_el1.s
```C
	.section  EL1_ENTRY,"ax"
	.global el1_entry
	.type el1_entry, "function"

el1_entry:
	LDR		x0, =vectors
	MSR		VBAR_EL1, x0	// Set EL1 Vector Table

	MOV		x0, #(0x3 << 20)
	MSR		CPACR_EL1, x0	// Disable instruction traps for EL1
	ISB

	.global  __main
	B        __main
```
