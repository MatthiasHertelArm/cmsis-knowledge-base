---
id: "intr-device-firmware-update-cookbook-shared-memory"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Design Patterns & Recipes / Shared Memory"
summary: "It is often useful to exchange information between our different programs."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#shared-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Design Patterns & Recipes_

It is often useful to exchange information between our different programs. The
application may want to signal to the loader that it should go into DFU mode on
the next reboot, and the loader may want to pass arguments to the application.

On some platforms, scratch registers can be used as mailboxes between the
different programs. This is the case for the STM32. For all others, we must make
do with RAM. "But François, isn't RAM volatile"? Not quite: as long as your MCU
remains powered, the SRAM will hold its state. For short durations, you can
treat it as non-volatile storage.

The simplest way to carve out an area of RAM to be shared across our programs is
to declare it in a shared linker script. We've [covered linker scripts on
Interrupt](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware),
so I won't detail the syntax again. This is what it looks like:

```
// memory_map.ld
MEMORY
{
  sharedram (rwx): ORIGIN = 0x20000000, LENGTH = 256
  ram (rwx)      : ORIGIN = 0x20000100, LENGTH = 128K - LENGTH(sharedram)
}

SECTIONS
{
    .shared_memory (NOLOAD) : {
        KEEP(*(.shared_memory))
    } >sharedram
}
```

This shared linker script can then be included by the individual program's
linker script with the `INCLUDE` directive.

Now that we have a region of RAM defined, we can define a structure for it. You
will want that structure to be packed to guard against alignment mismatches
across your programs as you update compiler flags and versions. Here again, we
use the `section` attribute to assign our symbol to the `.shared_memory` section.

```c
// shared_memory.c
typedef struct __attribute__((packed)) {
    uint32_t magic;
    uint32_t flags;
} shared_memory_t;

volatile shared_memory_t shared_memory __attribute__((section(".shared_memory")));
```

In the event of power loss, RAM will be left in an indeterminate state. We'll
need to detect this and reset the shared memory when it happens. On the STM32,
the RCC peripheral can tell us whether or not we lost power. When power is
lost, we'll erase the magic value at the beginning of our struct so that the
rest of our code knows not to trust the shared memory region. Stick the
following code somewhere in your early init sequence.

(thank you to interrupt reader dreiss for sending us this code snippet)
```
if (RCC->CSR & RCC_CSR_PORRSTF) {
    // Power loss has occurred.
    // Clear magic to ensure we initialize shared_memory.
    shared_memory.magic = 0;
    __DMB();  // Possibly not necessary.
    // Clear reset flags.
    RCC->CSR |= RCC_CSR_RMVF;
}
```

When we inspect our shared memory further down the line, we check the magic
number and initialize the struct if it isn't what we expect.

```c
void shared_memory_init(void) {
    if (shared_memory.magic != MAGIC) {
        printf("Shared memory uinitialized, setting magic\n");
        memset(&shared_memory, 0, sizeof(shared_memory_t));
        shared_memory.magic = MAGIC;
    }
}
```

A common use case for shared memory is to signal to the Loader that we should
not load the Application on the next boot and instead go into DFU mode. We use a
simple flag to signal this:

```c
bool shared_memory_is_dfu_requested(void) {
    return (shared_memory.flags & DFU_REQUESTED) != 0;
}

void shared_memory_set_dfu_requested(bool yes) {
    shared_memory.flags |= DFU_REQUESTED;
}
```

Using the shell from [Tyler's last post on CLI's](https://interrupt.memfault.com/blog/firmware-shell), I
created a shell command in the Application to set that flag and reboot:

```c
int cli_command_dfu_mode(int argc, char *argv[]) {
    shell_put_line("Rebooting into DFU mode");
    shared_memory_set_dfu_requested(true);
    scb_reset_system();
    while (1) {}
    return 0;
}
```

In the Loader, we systematically check the DFU flag before we start the
Application.

```c
// loader.c
if (!shared_memory_is_dfu_requested()) {
    // start app
}

printf("Entering DFU Mode\n");
shared_memory_set_dfu_requested(false);
```
