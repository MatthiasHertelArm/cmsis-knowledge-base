---
id: "alp-bare-metal-event-driven1-create-first-level-fiq-handler"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (1): Create first level FIQ Handler"
summary: "Each exception has a window of 0x80 bytes in the vector table area to use for its code. In this case you'll simply branch to fiqFirstLevelHandler, which preserves all registers, before calling fiqHandler() (which shall be implemented later)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1/#create-first-level-fiq-handler"
license: "CC-BY-SA-4.0"
mode: "V"
---

Each exception has a window of 0x80 bytes in the vector table area to use for its code. In this case you'll simply branch to `fiqFirstLevelHandler`, which preserves all registers, before calling `fiqHandler()` (which shall be implemented later).

When `fiqHandler()` returns, undo the register preservation, before returning to where the code was before the exception occurred, using the `ERET` instruction.

Add the following to your `vectors.s`:
#### vectors.s
```C
	.global fiqHandler
fiqFirstLevelHandler:
	STP	x29, x30, [sp, #-16]!
	STP	x18, x19, [sp, #-16]!
	STP	x16, x17, [sp, #-16]!
	STP	x14, x15, [sp, #-16]!
	STP	x12, x13, [sp, #-16]!
	STP	x10, x11, [sp, #-16]!
	STP	 x8,  x9, [sp, #-16]!
	STP	 x6,  x7, [sp, #-16]!
	STP	 x4,  x5, [sp, #-16]!
	STP	 x2,  x3, [sp, #-16]!
	STP	 x0,  x1, [sp, #-16]!
	
	BL	fiqHandler
	
	LDP	 x0,  x1, [sp], #16
	LDP	 x2,  x3, [sp], #16
	LDP	 x4,  x5, [sp], #16
	LDP	 x6,  x7, [sp], #16
	LDP	 x8,  x9, [sp], #16
	LDP	x10, x11, [sp], #16
	LDP	x12, x13, [sp], #16
	LDP	x14, x15, [sp], #16
	LDP	x16, x17, [sp], #16
	LDP	x18, x19, [sp], #16
	LDP	x29, x30, [sp], #16

	ERET
```
