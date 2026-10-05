---
id: "alp-bare-metal-reset-write-a-reset-handler"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Write a reset handler: Write a reset handler"
summary: "Create a new file, startup_el3.s, with the following contents: #### startup_el3.s"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/reset.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/reset/#write-a-reset-handler"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a new file, `startup_el3.s`, with the following contents:
#### startup_el3.s
```C
  .section  BOOT,"ax"   // Define an executable ELF section, BOOT
  .global el3_entry
  .type el3_entry, "function"

el3_entry:
  MRS      x0, MPIDR_EL1      // Read Affinity register
  AND      x0, x0, #0xFFFF    // Mask off Aff0/Aff1 fields
  CBZ      x0, boot           // Branch to boot if Aff0/Aff1 are zero (Core 0 of Cluster 0)
sleep:                        // Else put processor to sleep
  WFI
  B        sleep

boot:
  MSR      CPTR_EL3, xzr       // Clear all trap bits

  // Branch to scatter loading and C library init code
  .global  __main
  B        __main
```
Build the startup code with:
```console
armclang -c -g --target=aarch64-arm-none-eabi -march=armv8-a startup_el3.s
```
**Note:**
The compiler identifies `.s` files as assembler source.



### Understanding the reset handler

The [MPIDR_EL1](https://developer.arm.com/documentation/ddi0595/latest/AArch64-Registers/MPIDR-EL1--Multiprocessor-Affinity-Register) register provides a CPU identification mechanism. The `Aff0` and `Aff1` bitfields let us check which numbered processor in a cluster the code is running on. This startup code sends all but one processor to sleep.

Setting [CPTR_EL3](https://developer.arm.com/documentation/ddi0595/2021-12/AArch64-Registers/CPTR-EL3--Architectural-Feature-Trap-Register--EL3-) to zero disables various instruction traps which allows the C library init code to proceed.
