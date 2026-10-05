---
id: "alp-bare-metal-event-driven1-create-exception-vector-table"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (1): Create exception vector table"
summary: "The exception vector table tells the processor what code to run in the event of an exception. The format of this table is fixed and architecturally defined."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1/#create-exception-vector-table"
license: "CC-BY-SA-4.0"
mode: "V"
---

The [exception vector table](https://developer.arm.com/documentation/den0024/latest/AArch64-Exception-Handling/AArch64-exception-table) tells the processor what code to run in the event of an exception. The format of this table is fixed and architecturally defined.

Create `vectors.s` containing the following code.

**Note:**
You'll implement only the necessary FIQ exception for this example. A real system would need to implement all handlers.


#### vectors.s
```C
	.section VECTORS,"ax"
    .global vectors
	.balign 0x800
vectors:
	.space 0x100, 0x0		// Current EL with SP0
curr_el_sp0_fiq:
	B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x80, 0x0

	.space 0x100, 0x0		// Current EL with SPx
curr_el_spx_fiq:
	B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x80, 0x0

	.space 0x100, 0x0		// Lower EL using AArch64
lower_el_aarch64_fiq:
	B	fiqFirstLevelHandler
	.balign 0x80
	.space 0x80, 0x0

	.space 0x200, 0x0		// Lower EL using AArch32
```
