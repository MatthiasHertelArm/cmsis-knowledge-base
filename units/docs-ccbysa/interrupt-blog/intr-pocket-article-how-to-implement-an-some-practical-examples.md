---
id: "intr-pocket-article-how-to-implement-an-some-practical-examples"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM: Some practical examples"
summary: "Let's take a look at some simple examples showcasing how a .noinit section can be implemented and used"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory#some-practical-examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's take a look at some simple examples showcasing how a `.noinit` section can
be implemented and used

### No bootloader, just application

(See [How to write a bootloader from scratch (The Interrupt): Message passing to
catch reboot
loops](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#message-passing-to-catch-reboot-loops)
for another example of this!)



This system just has a single application that immediately starts when the chip
is powered up. There's two variables located in the `.noinit` section:

```c
// Two non-initialized variables, used to demonstrate keeping information
// through chip reset. Marked 'volatile' to ensure the compiler doesn't optimize
// away the STR's to these addresses
#define RESET_MAGIC 0xDEADBEEF
// magic value used to check if the variables are initialized
__attribute__((section(".noinit"))) volatile uint32_t reset_count_magic;
// reset counter, incremented on every warm reset
__attribute__((section(".noinit"))) volatile uint32_t reset_count;
```

When the chip is initially powered on, the contents of SRAM is unknown. To
handle this, the `reset_count_magic` variable contains a special value when
initialized. To use it, we might do something like this:

```c
if (reset_count_magic != RESET_MAGIC) {
  reset_count_magic = RESET_MAGIC;
  reset_count = 0;

  printf("First reset!\n");
}

printf("Reset count: %lu\n", ++reset_count);
```

After a cold power on, the `reset_count_magic` should persist through warm
resets (eg if a Hard Fault happens, or the system intentionally reboots), and
the `reset_count` should increment.

You can see more details in the implementation here:

<https://github.com/noahp/cortex-m-bootloader-sample/tree/app-only>

### Bootloader and application, separate linker scripts

This system has a bootloader and application, placed into separate pages of
flash memory:

```c
MEMORY
{
  BOOTLOADER_FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 16K
  APP_FLASH (rx) : ORIGIN = 0x08004000, LENGTH = 1M - 16K
  RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K - 0x100
  NOINIT (rwx) : ORIGIN = 0x20000000 + 128K - 0x100, LENGTH = 0x100
}
```

Each linker script specifies the correct region to place read-only code and
data, for example, for the bootloader:

```c
SECTIONS
{
    .text :
    {
        KEEP(*(.isr_vector))
        *(.text*)
        KEEP(*(.init))
        KEEP(*(.fini))
        *(.rodata*)
    } > BOOTLOADER_FLASH
}
```

On chip power up, the bootloader runs first (since it's placed at the lowest
flash address). In this example, the bootloader and app share a source file
containing the non-initialized variable:

```c
// noinit.c

#include <stdint.h>

// marked 'volatile' to ensure the compiler doesn't optimize away the STR's to
// these addresses
__attribute__((section(".noinit"))) volatile uint32_t mailbox[4];
```

The bootloader can set values into that variable, and the application can read
them:

```c
// bootloader main.c:
  extern volatile uint32_t mailbox[4];
  mailbox[0] = get_random_number();
  printf("Set random value to mailbox: 0x%08" PRIx32 "\n", mailbox[0]);

// app main.c:
  extern volatile uint32_t mailbox[4];
  printf("mailbox was: 0x%08" PRIx32 "\n", mailbox[0]);
```

The application could also set values into the mailbox, then jump to the
bootloader (eg via reset). This might be used to command the bootloader to
reflash the application, for example in a "dual-bank" (aka A/B) partition
scheme.

You can see more details in the implementation here:

<https://github.com/noahp/cortex-m-bootloader-sample/tree/two-linker-scripts>

### Bootloader and application, shared linker script

This system is very similar to the one above, except the bootloader and
application use the same linker script:

```c
MEMORY
{
  BOOTLOADER_FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 16K
  APP_FLASH (rx) : ORIGIN = 0x08004000, LENGTH = 1M - 16K
  RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K - 0x100
  NOINIT (rwx) : ORIGIN = 0x20000000 + 128K - 0x100, LENGTH = 0x100
}

SECTIONS
{
  .text :
  {
        KEEP(*(.isr_vector))
        *(.text*)
        KEEP(*(.init))
        KEEP(*(.fini))
        *(.rodata*)
  } > FLASH__  /* placeholder region identifier */
}
```

To link the bootloader or application, the shared linker script is run through
the C preprocessor to generate the linker script used for linking. The `FLASH__`
placeholder is replaced with the appropriate `BOOTLOADER_FLASH`/`APP_FLASH`
region for the application being linked:

```bash
❯ gcc -DFLASH__=APP_FLASH -E -P -C -x c-header src/common/stm32f407.ld > build/app.ld
```

(A similar technique is used by the Zephyr RTOS build system to derive the
correct linker script for different targets/memory configurations).

You can see more details in the implementation here:

<https://github.com/noahp/cortex-m-bootloader-sample/tree/shared-linker-script>
