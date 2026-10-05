---
id: "intr-beyond-error-codes-debugging-ill-d-step-7-vet-critical-peripherals"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 7 - Vet Critical Peripherals"
summary: "We are now entering a rather not-fun section of debugging, which could uncharitably be called \"grasping at straws\"."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-7-vet-critical-peripherals"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

We are now entering a rather not-fun section of debugging, which could
uncharitably be called "grasping at straws". At this point, you've gained a lot
of confidence about bad behavior you _aren't_ doing, and yet you're still
getting that hard fault, nonsensical memory access, etc. Now, you'll want to
turn a critical gaze toward "mission-critical" peripherals that could be
misconfigured. I'll go through a couple of categories of peripherals that fall
into this category and some common pitfalls for each.

#### Memory Mapped RAM/Flash

Memory Mapped RAM/Flash refers to an MCU that can map external RAM or Flash ICs
in memory. A common example many readers may have experience with is the
Raspberry Pi Pico. This chip (the RP2040 or new RP2350) has only immutable ROM
memory internally for persistent storage and instead executes code loaded on an
external flash IC. "Memory mapped" means that once appropriately configured, the
processor can treat memory locations on these external chips as lying in a
normal address space. As I will demonstrate in
[one of my case studies](#case-study-4---memory-faults-in-the-depths-of-hell),
misconfiguring one of these ICs can lead to VERY odd behavior. The configuration
of these devices and the peripherals that enable memory mapping should be
investigated using a fine-toothed comb.

#### DMA

DMA refers to direct memory access, a peripheral whose purpose is to perform
memory transfers in parallel while the processor does other things. The DMA
should be used _very_ carefully, as it is incredibly easy to corrupt memory
without careful usage. C and C++ do not know what the DMA is "doing" at any
given time, so take extra care to verify whether or not the DMA is currently
operating on a region of memory. Embedded engineers can do various dangerous
things with the DMA, including:

- Telling the DMA to copy memory from an array that is about to go out of scope,
  the DMA will happily keep copying memory out of a location that is no longer
  valid
- Trying to modify memory _in code_ that the DMA is already actively writing to,
  neither operation will succeed as intended
- Using the DMA with cached memory (see next topic)

#### Caching

As MCUs grow more complex, many are starting to come with instruction (ICache)
and data (DCache) caches. While caching can significantly speed up program
execution, it also brings several capital H headaches. To vastly oversimplify
it, a processor's cache stores a copy of commonly accessed data in a special
location that's much faster to access than getting it from RAM or flash storage.
Generally, the processor handles deciding when and what to fetch from the cache
(vs the actual memory location) for you. It gets complicated when you start
bringing in peripherals like the DMA. The DMA often operates without "letting
the processor know" that the cache needs to be refreshed, leading to fetching
stale/erroneous data. If you even slightly suspect the cache might be
contributing to your issue, try turning all caching off. Some processors even
allow you to manually flush the cache with a register write. So, a more nuanced
approach could be adding a call to flush the cache before a suspect operation.

#### MPU

Some MCUs come with a "Memory Protection Unit" or MPU. The MPU is used to
designate what is allowed in specific regions of memory. For instance, one
region might be read-only and allow code execution, while another might be
read/write but disallow code execution. The MPU can often be complicated to
configure, and misconfiguration can lead to unintentional hard faults. For
example, this kind soul provides an
[extremely detailed write-up](https://github.com/MisterHW/BSICS-SVR/blob/master/doc/readme_mpu.md)
on the trials and tribulations of configuring the MPU for Cortex-M7-based STM32
chips.

#### Interrupt Controller

I could dedicate far more than a paragraph to all the trials and tribulations of
configuring interrupts and interrupt handlers correctly, however, given the
already large scope of this article, I'll simply provide a couple of reminders:

- Do you have data that can be accessed in both interrupt and non-interrupt
  contexts? If so, ensure you protect against any potential data races.
  [This article](https://blog.regehr.org/archives/28) may surprise some, the
  `volatile` qualifier _does not_ provide a means of thread synchronization.
- Is there anywhere in your code you disable/mask interrupts? Take extra care
  during these "critical sections" to avoid missing interrupts and potentially
  causing unintended behavior.
- If using an RTOS, are you using the appropriate interrupt/non-interrupt APIs
  (if applicable)? For instance, FreeRTOS has separate "interrupt safe" and
  "non-interrupt safe" APIs, and you must use them correctly to avoid undefined
  behavior.
