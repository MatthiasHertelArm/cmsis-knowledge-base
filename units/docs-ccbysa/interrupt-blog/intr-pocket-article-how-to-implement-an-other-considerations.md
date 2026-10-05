---
id: "intr-pocket-article-how-to-implement-an-other-considerations"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM: Other considerations"
summary: "Some chips will have a \"backup RAM\" or dedicated USB or Ethernet memory banks. These memories can be a convenient spot to place noinit data (if the memory is not being used for another purpose)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory#other-considerations"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Backup RAM

Some chips will have a "backup RAM" or dedicated USB or Ethernet memory banks.
These memories can be a convenient spot to place noinit data (if the memory is
not being used for another purpose).

For example, on the STM32F407VG, there's a 4kB "Backup RAM" intended for very
low power sleep data retention; however, the memory can be used for any purpose.

```c
MEMORY
{
  /* on this chip, there's 4kB of "Backup RAM" mapped to this address */
  NOINIT (rwx) : ORIGIN = 0x40024000, LENGTH = 4k
}
```

On this chip, the backup RAM does need to be powered up to be used:

```c
//! Using the stm32f407xx.h CMSIS register structures to enable the backup SRAM
static void enable_backup_sram(void) {
  // enable power interface clock
  RCC->APB1ENR |= RCC_APB1ENR_PWREN;

  // enable backup SRAM clock
  RCC->AHB1ENR |= RCC_AHB1ENR_BKPSRAMEN;

  // enable backup SRAM
  PWR->CR |= PWR_CR_DBP;
}
```

Then we can read/write variables that are placed in that region! Since this RAM
may not be typically used for the main application, this could be considered
"free" memory for various purposes (such as non-initialized data!)!

### Retrofitting a noinit region when you can’t update the bootloader

This scenario could happen if the application needs a `.noinit` region, but the
bootloader is not updateable (either due to external requirements, permanently
enabling write protect on the bootloader flash pages, or avoiding the risk of
potentially bricking a device if the bootloader update fails).

If the bootloader is set up to use all of RAM, you'll need to examine which
locations are actually used. For example, stack may start at the top of RAM and
grow down; if there's a known limit to the stack, a `.noinit` region could be
added below the stack region, and the bootloader won't overrwrite it.

To illustrate this, here's a typical RAM layout for an embedded system,
including stack and heap, from lowest to highest memory address:

```plaintext
.data
.bss
.heap (end of .bss, grows up)
<possible spot for retrofitted .noinit>
.stack (end of RAM, grows down)
```

Of course, if you're lucky, there may be a small reserve of RAM ([backup
RAM](#backup-ram)) that can be used instead!

### Gotchas: Watch out for ROM bootloaders (they use RAM too)

Some chips have ROM bootloaders (also referred to "ISP", In-System Programming),
that can:

- run before the user application is started
- run on-demand, depending on boot pins, or programmatically launched from
  software

These ROM programs will often use RAM for their own purposes! which can impact
`.noinit` regions. Consult the chip documentation, but be wary. Some chips don't
have good documentation on the ROM bootloader.

Some chips use routines stored in ROM for other purposes (flash programming,
built-in USB operations, etc); for example, the LPC15xx series documents this:

[(figure: lpc iap example)](https://interrupt.memfault.com/img/noinit/lpc15xx-isp-iap-ram-usage.png)

### Test implementation

Some chips can lose SRAM contents when resetting (some chips wire up `NVIC`
reset to pulse the physical reset line!), which can make these schemes unstable
and a pain to debug.

When bringing up a new chip, it's worth consulting the docs on this topic, as
well as doing a quick check that SRAM contents persist through chip reset. This
can be done by:

1. writing a pattern to entire reserved area (eg `0x01234567`)
2. reset the chip and confirm the pattern is still valid across the region

{:.no_toc}
