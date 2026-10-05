---
id: "alp-bare-metal-event-driven1-configure-exception-routing-to"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (1): Configure exception routing to EL3"
summary: "This example will implement an FIQ. When this occurs, it will go to the highest exception level, EL3."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven1/#configure-exception-routing-to-el3"
license: "CC-BY-SA-4.0"
mode: "V"
---

This example will implement an FIQ. When this occurs, it will go to the highest exception level, `EL3`.

Modify `startup_el3.s` to extend the `boot` code to perform the following, before branching to `__main`.

### Enable exception routing to EL3

Configure the [SCR_EL3, Secure Configuration Register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/SCR-EL3--Secure-Configuration-Register?lang=en) to route FIQ exceptions to `EL3`.
#### startup_el3.s
```C
// Configure SCR_EL3
	MOV  w1, #0
	ORR  w1, w1, #(1 << 2)   // Set FIQ bit (FIQs routed to EL3)
	MSR  SCR_EL3, x1
```
### Point to the exception vector table
Set the [VBAR_EL3, Vector Based Address Register](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/VBAR-EL3--Vector-Base-Address-Register--EL3-) to the location of the exception vector table. You'll create `vectors` in the next section.
#### startup_el3.s
```C
// Install vector table
	.global vectors
	LDR  x0, =vectors
	MSR  VBAR_EL3, x0
	ISB
```
### Disable masking of exceptions at EL3 by PSTATE
Clear appropriate bits within [DAIF, Interrupt Mask Bits](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/DAIF--Interrupt-Mask-Bits).
#### startup_el3.s
```C
// Clear interrupt masks
	MSR  DAIFClr, #0xF
```
Save your `startup_el3.s` file.
