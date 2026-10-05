---
id: "alp-bare-metal-exception-levels-modify-el3-initialization"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Switching Exception Levels: Modify EL3 initialization"
summary: "You'll also need to modify the EL3 initialization from before: Create an EL3 stack (as _main will now be called in EL1) Disable timer exceptions at EL3 Execute any privileged code (gicInit) Set EL1 execution state to be …"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/exception-levels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/exception-levels/#modify-el3-initialization"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll also need to modify the `EL3` initialization from before:
* Create an `EL3` stack (as `__main` will now be called in `EL1`)
* Disable timer exceptions at `EL3`
* Execute any privileged code (`gicInit`)
* Set `EL1` execution state to be `Aarch64` (before entering `EL1`)
* Switch to `EL1` level

### EL3 stack
Create a new execution region `STACK_EL3` in the scatter file for the EL3 stack.
##### scatter.txt
```
	STACK_EL3 0x04020000 EMPTY 0x10000{}
```
The linker will generate a symbol `Image$$STACK_EL3$$ZI$$Limit` which can be referenced in code as follows:
#### startup_el3.s
```C
boot:
	// Set EL3 Stack pointer
	ADRP x0, Image$$STACK_EL3$$ZI$$Limit
	MOV  sp, x0
```

### SCR_EL3
In the code to set up [SCR_EL3](https://developer.arm.com/documentation/ddi0595/2021-06/AArch64-Registers/SCR-EL3--Secure-Configuration-Register), set the `ST` bit to disable timer exceptions, and the `RW` bit so that `EL1` executes in `Aarch64` state.

Also, remove the code to set the `FIQ` bit, as you now want to trap this exception in `EL1`.
#### startup_el3.s
```C
	// Configure SCR_EL3
	MOV  w1, #0
	ORR  w1, w1, #(1 << 11)  // set ST bit (disable trapping of timer control registers)
	ORR  w1, w1, #(1 << 10)  // set RW bit (next lower EL in aarch64)
	MSR  SCR_EL3, x1
```
### Perform other EL3 tasks
The code to initialize the `GIC` must be executed in `EL3`. Call `gicInit()` function before leaving `EL3`. This function sets the `NS` bit in `SCR_EL3`. Clear it here to avoid issues with [security settings](https://developer.arm.com/documentation/den0024/a/Security), which is beyond the scope of this article.

#### startup_el3.s
```C
// Initialize GIC
	BL	gicInit
	MRS      x1, SCR_EL3
	BIC      x1, x1, #1  // Clear NS bit
	MSR      SCR_EL3, x1
```
Remove the call to `gicInit()` from your `main()` function.
#### hello.c
```C
  // gicInit();
```

### Switch to EL1
Rather than branching to `__main`, the `EL3` reset handler must instead perform an exception return (`ERET`) to `EL1`. Set this up by configuring the appropriate registers:

* Initialize [SCTLR_EL1, System Control Register (EL1)](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/SCTLR-EL1--System-Control-Register--EL1-) so that `EL1` is in a known state
* Set [SPSR_EL3, Saved Program Status Register (EL3)](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/SPSR-EL3--Saved-Program-Status-Register--EL3-) so that the code will return to `EL1` exception level.
* Set [ELR_EL3, Exception Link Register (EL3)](https://developer.arm.com/documentation/ddi0601/latest/AArch64-Registers/ELR-EL3--Exception-Link-Register--EL3-?lang=en) with the address of the `EL1` entry point.

#### startup_el3.s
```C
// Switch to EL1
	MSR		SCTLR_EL1, xzr	// Initialize state of EL1

	MOV		x1, #0x5
	MSR		SPSR_EL3,x1		// Set return level to EL1

	LDR		x0, =el1_entry
	MSR		ELR_EL3, x0		// Set return address to EL1 entry point

	ISB						// Ensure all above fully executes before...
	ERET					// Returning to EL1
```
Delete the call to `__main()` in `EL3`.
```C
	.global  __main
	B        __main
```
Save your `startup_el3.s` file.

**Note:**
The complete source for this file is provided as an [appendix](#appendix) below for reference.
