---
id: "intr-from-zero-to-main-how-to-write-a-b-a-minimal-bootloader"
type: "concept"
domain: "debug"
title: "From Zero to main(): How to Write a Bootloader from Scratch: A minimal bootloader"
summary: "Let’s build a simple bootloader together. To start, our bootloader must do two things:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-13-how-to-write-a-bootloader-from-scratch.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#a-minimal-bootloader"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let’s build a simple bootloader together. To start, our bootloader must do two
things:

1. Execute on MCU boot
2. Jump to our application code

We’ll need to decide on a memory map, write some bootloader code, and update our
application to make it bootload-able.

### Setting the stage

For this example, we’ll be using the same setup as we did in our previous Zero
to Main posts:
* Adafruit's [Metro M0 Express](https://www.adafruit.com/product/3505) as our
  development board,
* a simple [CMSIS-DAP Adapter](https://www.adafruit.com/product/2764)
* OpenOCD (the [Arduino fork](https://github.com/arduino/OpenOCD)) for
  programming

### Deciding on a memory map

We must first decide on how much space we want to dedicate to our bootloader.
Code space is precious - your application may come to need more of it - and you
will not be able to change this without updating your bootloader, so make
this as small as you possibly can.

Another important factor is your flash sector size: you want to make sure you
can erase app sectors without erasing bootloader data, or vice versa.
Consequently, your bootloader region must end on a flash sector boundary
(typically 4kB).

I decided to go with a 16kB region, leading to the following memory map:

```
        0x0 +---------------------+
            |                     |
            |     Bootloader      |
            |                     |
     0x4000 +---------------------+
            |                     |
            |                     |
            |     Application     |
            |                     |
            |                     |
    0x30000 +---------------------+
```

We can transcribe that memory into a linker script:

```
/* memory_map.ld */
MEMORY
{
  bootrom  (rx)  : ORIGIN = 0x00000000, LENGTH = 0x00004000
  approm   (rx)  : ORIGIN = 0x00004000, LENGTH = 0x0003C000
  ram      (rwx) : ORIGIN = 0x20000000, LENGTH = 0x00008000
}

__bootrom_start__ = ORIGIN(bootrom);
__bootrom_size__ = LENGTH(bootrom);
__approm_start__ = ORIGIN(approm);
__approm_size__ = LENGTH(approm);
```

Since linker scripts are composable, we will be able to `include` that memory
map into the linker scripts we write for our bootloader and our application.

You’ll notice that the linker script above declares some variables. We’ll need
those for our bootloader to know where to find the application. To make them
accessible in C code, we declare them in a header file:

```c
/* memory_map.h */
#pragma once

extern int __bootrom_start__;
extern int __bootrom_size__;
extern int __approm_start__;
extern int __approm_size__;
```

### Implementing the bootloader itself
Next up, let’s write some bootloader code. Our bootloader needs to start
executing on boot and then jump to our app.

We know how to do the first part from our previous post: we need a valid stack
pointer at address `0x0` , and a valid `Reset_Handler`  function setting up our
environment at address `0x4`. We can reuse our previous startup file and linker
script, with one change: we use  `memory_map.ld` rather than define our own
`MEMORY` section.

We also need to put our code in the `bootrom` region from our memory rather than
the `rom` region in our previous post.

Our linker script therefore looks like this:

```
/* bootloader.ld */
INCLUDE memory_map.ld

/* Section Definitions */
SECTIONS
{
    .text :
    {
        KEEP(*(.vectors .vectors.*))
        *(.text*)
        *(.rodata*)
        _etext = .;
    } > bootrom
  ...
}
```

To jump into our application, we need to know where the `Reset_Handler` of the
app is, and what stack pointer to load.  Again, we know from our previous post
that those should be the first two 32-bit words in our binary, so we just need
to dereference those addresses using the `__approm_start__` variable from our
memory map.

```c
/* bootloader.c */
#include <inttypes.h>
#include "memory_map.h"

int main(void) {
  uint32_t *app_code = (uint32_t *)__approm_start__;
  uint32_t app_sp = app_code[0];
  uint32_t app_start = app_code[1];
  /* TODO: Start app */
  /* Not Reached */
  while (1) {}
}
```

Next we must load that stack pointer and jump to the code. This will require a
bit of assembly code.

ARM MCUs use the [`msr` instruction
](http://www.keil.com/support/man/docs/armasm/armasm_dom1361289882044.htm) to
load immediate or register data into system registers, in this case the MSP
register or “Main Stack Pointer”.

Jumping to an address is done with a branch, in our case with a [`bx`
instruction](http://www.keil.com/support/man/docs/armasm/armasm_dom1361289866466.htm).

We wrap those two into a `start_app` function which accepts our `pc` and `sp` as
arguments, and get our minimal bootloader:

```c
/* bootloader.c */
#include <inttypes.h>
#include "memory_map.h"

static void start_app(uint32_t pc, uint32_t sp) __attribute__((naked)) {
    __asm("           \n\
          msr msp, r1 /* load r1 into MSP */\n\
          bx r0       /* branch to the address at r0 */\n\
    ");
}

int main(void) {
  uint32_t *app_code = (uint32_t *)__approm_start__;
  uint32_t app_sp = app_code[0];
  uint32_t app_start = app_code[1];
  start_app(app_start, app_sp);
  /* Not Reached */
  while (1) {}
}
```

> Note: hardware resources initialized in the bootloader must be de-initialized
> before control is transferred to the app. Otherwise, you risk breaking
> assumptions the app code is making about the state of the system

### Making our app bootloadable

We must update our app to take advantage of our new memory map. This is again
done by updating our linker script to include `memory_map.ld` and changing our
sections to go to the `approm` region rather than `rom`.

```
/* app.ld */
INCLUDE memory_map.ld

/* Section Definitions */
SECTIONS
{
    .text :
    {
        KEEP(*(.vectors .vectors.*))
        *(.text*)
        *(.rodata*)
        _etext = .;
    } > approm
  ...
}
```

We also need to update the [*vector
table*](https://developer.arm.com/docs/dui0552/latest/the-cortex-m3-processor/exception-model/vector-table)
used by the microcontroller. The vector table contains the address of every
exception and interrupt handler in our system. When an interrupt signal comes
in, the ARM core will call the address at the corresponding offset in the vector
table.

For example, the offset for the Hard fault handler is `0xc`, so when a hard
fault is hit, the ARM core will jump to the address contained in the table at
that offset.

By default, the vector table is at address `0x0`, which means that when our chip
powers up, only the bootloader can handle exceptions or interrupts! Fortunately, ARM
provides the [Vector Table Offset
Register](https://developer.arm.com/docs/dui0552/latest/cortex-m3-peripherals/system-control-block/vector-table-offset-register)
to dynamically change the address of the vector table. The register is at
address `0xE000ED08` and has a simple layout:

```
31                                  7              0
+-----------------------------------+--------------+
|                                   |              |
|              TBLOFF               |   Reserved   |
|                                   |              |
+-----------------------------------+--------------+
```

Where `TBLOFF` is the address of the vector table. In our case, that’s the start
of our text section, or `_stext`. To set it in our app, we add the following to
our `Reset_Handler`:

```c
/* startup_samd21.c */
/* Set the vector table base address */
uint32_t *vector_table = (uint32_t *) &_stext;
uint32_t *vtor = (uint32_t *)0xE000ED08;
*vtor = ((uint32_t) vector_table & 0xFFFFFFF8);
```

One quirk of the ARMv7-m architecture is the alignment requirement for the
vector table, as specified in section B1.5.3 of the [reference
manual](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf):

> The Vector table must be naturally aligned to a power of two whose alignment value is greater than or equal
to (Number of Exceptions supported x 4), with a minimum alignment of 128 bytes.The entry at offset 0 is
used to initialize the value for SP_main, see The SP registers on page B1-8. All other entries must have bit
[0] set, as the bit is used to define the EPSR T-bit on exception entry (see Reset behavior on page B1-20 and
Exception entry behavior on page B1-21 for details).

Our SAMD21 MCU has 28 interrupts on top of the 16 system reserved exceptions,
for a total of 44 entries in the table. Multiply that by 4 and you get 176. The
next power of 2 is 256, so our vector table must be 256-byte aligned.

### Putting it all together

Because it is hard to witness the bootloader execute, we add a print line to
each of our programs:

```c
/* boootloader.c */
#include <inttypes.h>
#include "memory_map.h"

static void start_app(uint32_t pc, uint32_t sp) {
    __asm("           \n\
          msr msp, r1 /* load r1 into MSP */\n\
          bx r0       /* branch to the address at r0 */\n\
    ");
}

int main() {
  serial_init();
  printf("Bootloader!\n");
  serial_deinit();

  uint32_t *app_code = (uint32_t *)__approm_start__;
  uint32_t app_sp = app_code[0];
  uint32_t app_start = app_code[1];

  start_app(app_start, app_sp);

  // should never be reached
  while (1);
}
```

and:

```c
/* app.c */
int main() {
  serial_init();
  set_output(LED_0_PIN);

  printf("App!\n");
  while (true) {
    port_pin_toggle_output_level(LED_0_PIN);
    for (int i = 0; i < 100000; ++i) {}
  }
}
```

> Note that the bootloader *must* deinitialize the serial peripheral before
> starting the app, or you’ll have a hard time trying to initialize it again.

 You can compile both these programs and load the resulting elf files with `gdb`
which will put them at the correct address. However, the more convenient thing
to do is to build a single binary which contains both programs.

To do that, you must go through the following steps:
1. Pad the bootloader binary to the full 0x4000 bytes
2. Create the app binary
3. Concatenate the two

Creating a binary from an elf file is done with `objcopy` . To
accommodate our use case, `objcopy` has some handy options:

```
$ arm-none-eabi-objcopy --help | grep -C 2 pad
  -b --byte <num>                  Select byte <num> in every interleaved block
     --gap-fill <val>              Fill gaps between sections with <val>
     --pad-to <addr>               Pad the last section up to address <addr>
     --set-start <addr>            Set the start address to <addr>
    {--change-start|--adjust-start} <incr>
```

The `—pad-to` option will pad the binary up to an address, and `—gap-fill` will
allow you to specify the byte value to fill the gap with. Since we are writing
our firmware to flash memory, we should fill with `0xFF` which is the erase
value of flash, and pad to the max address of our bootloader.

We implement those rule in our Makefile, to avoid having to type them out each
time:

```
# Makefile
$(BUILD_DIR)/$(PROJECT)-app.bin: $(BUILD_DIR)/$(PROJECT)-app.elf
  $(OCPY) $< $@ -O binary
  $(SZ) $<

$(BUILD_DIR)/$(PROJECT)-boot.bin: $(BUILD_DIR)/$(PROJECT)-boot.elf
  $(OCPY) --pad-to=0x4000 --gap-fill=0xFF -O binary $< $@
  $(SZ) $<

```

Last but not least, we need to concatenate our two binaries. As funny as that
may sound, this is best achieved with `cat`:

```
# Makefile
$(BUILD_DIR)/$(PROJECT).bin: $(BUILD_DIR)/$(PROJECT)-boot.bin $(BUILD_DIR)/$(PROJECT)-app.bin
  cat $^ > $@
```
