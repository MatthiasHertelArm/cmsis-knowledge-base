---
id: "intr-beyond-error-codes-debugging-ill-d-step-3-utilize-all-mcu-error-reporting-c"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 3 - Utilize All MCU Error Reporting Capabilities"
summary: "Nearly every MCU I've worked with has some fault-reporting capability. A fantastic Interrupt article I find myself coming back to time and time again details hard fault handlers, specifically on Cortex-M platforms."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-3-utilize-all-mcu-error-reporting-capabilities"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

Nearly every MCU I've worked with has some fault-reporting capability. A
[fantastic Interrupt article](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug)
I find myself coming back to time and time again details hard fault handlers,
specifically on Cortex-M platforms.

Almost all of the problems I'll describe in my case studies eventually presented
themselves as triggering a hard fault (and thus ending up in a hard fault
handler). It is common for HAL code provided by a vendor to provide weakly
defined _default_ hard fault handlers like so:

```c
void Default_Handler()
{
  while (1) {
  }
}
void HardFault_Handler()   __attribute__((weak, alias("Default_Handler")));
```

At the very least, replacing these handlers with something that at least logs
what's happened can immediately point you in the direction of the problem:

```c
void HardFault_Handler()   {
  log("A hard fault occurred!");
  asm volatile ("bkpt #0");
  while(1) {};
}
```

Note the ARM-specific "breakpoint" instruction for allowing an automatic halt
when a debugger is connected.

The specificity of fault reporting will vary by MCU, but you should try to gain
as much knowledge as possible about the fault that's occurring. For example, on
a Cortex-M7-based MCU, you can learn if the fault was:

- Caused by an invalid memory access (and sometimes what the offending bad
  address was)
- An unaligned load or store
- A divide by zero
- An undefined instruction
- An MPU (memory protection unit) violation (trying to write to a region marked
  read-only, for instance)

Sometimes, you get lucky, and the information received lets you immediately
isolate the error. Otherwise, this gives you a clue for the general area to look
at. For instance, if I see a hard fault from trying to access a bad memory
address, I know to look for some form of memory "corruption". While this can
encompass a broad range of issues, I know at least the general problem I'm
looking for.

Having exhausted some minimal effort options, let's now take a more hands on
approach to isolating the problem.
