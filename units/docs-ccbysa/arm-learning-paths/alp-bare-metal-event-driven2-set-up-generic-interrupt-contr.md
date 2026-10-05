---
id: "alp-bare-metal-event-driven2-set-up-generic-interrupt-contr"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create event-driven application (2): Set up Generic Interrupt Controller (GIC)"
summary: "Create gic.s with the following code to initialize the GICv3 implemented in the FVP, and define the timer as a source of interrupts."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/event-driven2/#set-up-generic-interrupt-controller-gic"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create `gic.s` with the following code to initialize the GICv3 implemented in the FVP, and define the timer as a source of interrupts.

For detail on this code, see the [GICv3 and GICv4 Software Overview](https://developer.arm.com/documentation/dai0492).

#### gic.s
```C
	.section GIC,"ax"
	.global gicInit
	.type gicInit, "function"

gicInit:
	// Configure Distributor
	MOV      x0, #0x2f000000	// GIC Distributor, GICD
	// Set ARE bits and group enables in the Distributor
	ADD      x1, x0, #0x0	// GICD_CTLROffset
	MOV      x2,     #0x20  // GICD_CTLR.ARE_NS
	ORR      x2, x2, #0x10  // GICD_CTLR.ARE_S
	STR      w2, [x1]
	
	ORR      x2, x2, #0x01	// GICD_CTLR.EnableG0
	ORR      x2, x2, #0x04	// GICD_CTLR.EnableG1S
	ORR      x2, x2, #0x02	// GICD_CTLR.EnableG1NS
	STR      w2, [x1]
	DSB      SY
	
	// Configure Redistributor
	// Clearing ProcessorSleep signals core is awake
	MOV      x0, #0x2f100000	// GIC Redistributor, RD_base
	MOV      x1, #0x14		// GICR_WAKERoffset
	ADD      x1, x1, x0
	STR      wzr, [x1]
	DSB      SY

waiting:   // Wait for ChildrenAsleep to read 0
	LDR      w0, [x1]
	AND      w0, w0, #0x6
	CBNZ     w0, waiting

	// Configure CPU interface
	// Set the SRE bits for each EL to enable
	// access to the interrupt controller registers
	MOV      x0, #0x8		// ICC_SRE_ELn.Enable
	ORR      x0, x0, #0x1	// ICC_SRE_ELn.SRE
	MSR      ICC_SRE_EL3, x0
	ISB
	
	MSR      ICC_SRE_EL1, x0
	MRS      x1, SCR_EL3
	ORR      x1, x1, #1		// Set NS bit, to access Non-secure registers
	MSR      SCR_EL3, x1
	ISB
	
	MSR      ICC_SRE_EL2, x0
	ISB
	
	MSR      ICC_SRE_EL1, x0
	
	MOV      w0, #0xFF
	MSR      ICC_PMR_EL1, x0 // Set PMR to lowest priority
	
	MOV      w0, #3
	MSR      ICC_IGRPEN1_EL3, x0
	MSR      ICC_IGRPEN0_EL1, x0

	// Secure Physical Timer source defined
	MOV      x0, #0x2f110000	// GIC Redistributor, SGI_base

	ADD      x1, x0, #0x80		// GICR_IGROUPRoffset
	STR      wzr, [x1]          // Mark INTIDs 0..31 as Secure
	
	ADD      x1, x0, #0xD00		// GICR_IGRPMODRoffset
	STR      wzr, [x1]          // Mark INTIDs 0..31 as Secure Group 0
	
	ADD      x1, x0, #0x100		// GICR_ISENABLERoffset
	MOV      w2, #(1 << 29)     // Enable INTID 29
	STR      w2, [x1]           // Enable interrupt source
		
	RET
```
