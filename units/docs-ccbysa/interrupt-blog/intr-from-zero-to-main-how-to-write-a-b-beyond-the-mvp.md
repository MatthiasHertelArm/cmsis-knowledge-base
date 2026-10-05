---
id: "intr-from-zero-to-main-how-to-write-a-b-beyond-the-mvp"
type: "concept"
domain: "debug"
title: "From Zero to main(): How to Write a Bootloader from Scratch: Beyond the MVP"
summary: "Our bootloader isn’t too useful so far, it only loads our application. We could do just as well without it. In the following sections, I will go through a few useful things you can do with a bootloader."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-13-how-to-write-a-bootloader-from-scratch.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#beyond-the-mvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Our bootloader isn’t too useful so far, it only loads our application. We could
do just as well without it. In the following sections, I will go through a few
useful things you can do with a bootloader.

### Message passing to catch reboot loops

A common thing to do with a bootloader is monitor stability. This can be done
with a relatively simple setup:
1. On boot, the bootloader increments a persistent counter
2. After the app has been stable for a while (e.g. 1 minute), it resets the
   counter to 0
3. If the counter gets to 3, the bootloader does not start the app but instead
   signals an error.

This requires shared, persistent data between the application and the bootloader
which is retained across reboots. On some architectures, non volatile registers
are available which make this easy. This is the case on all STM32
microcontrollers which have RTC backup registers.

More often than not, we can use a region of RAM to get the same result. As long
as the system remains powered, the RAM will keep its state even if the device
reboots.

First, we carve some RAM for shared data in our memory map:

```
/* memory_map.ld */
MEMORY
{
  bootrom  (rx)  : ORIGIN = 0x00000000, LENGTH = 0x00004000
  approm   (rx)  : ORIGIN = 0x00004000, LENGTH = 0x0003C000
  shared   (rwx) : ORIGIN = 0x20000000, LENGTH = 0x1000
  ram      (rwx) : ORIGIN = 0x20001000, LENGTH = 0x00007000
}

/* shared data starts point at the origin of the shared region */
_shared_data_start = ORIGIN(shared);

```

We can then create a data structure and assign it to this section, with getters
to read it:

```c
/* shared.h */

#include <inttypes.h>

uint8_t shared_data_get_boot_count(void);

void shared_data_increment_boot_count(void);

void shared_data_reset_boot_count(void);

/* shared.c */

#include "shared.h"

extern uint32_t _shared_data_start;

#pragma pack (push)
struct shared_data {
  uint8_t boot_count;
};
#pragma pack (pop)

struct shared_data *sd = (struct shared_data *)&_shared_data_start;

uint8_t shared_data_get_boot_count(void) {
  return sd->boot_count;
}

void shared_data_increment_boot_count(void) {
  sd->boot_count++;
}

void shared_data_reset_boot_count(void) {
  sd->boot_count = 0;
}
```

We compile the `shared` module into both our app and our bootloader, and can
read the boot count in both programs.

### Relocating our app from flash to RAM

More commonly, bootloaders are used to relocate applications before they are
executed. Relocations involves copying the application code from one place to
another in order to execute it. This is useful when your application is stored
in non-executable memory like a SPI flash.

Consider the following memory map:

```
/* memory_map.ld */
MEMORY
{
  bootrom  (rx)  : ORIGIN = 0x00000000, LENGTH = 0x00010000
  approm   (rx)  : ORIGIN = 0x00010000, LENGTH = 0x00004000
  ram      (rwx) : ORIGIN = 0x20000000, LENGTH = 0x00004000
  eram     (rwx) : ORIGIN = 0x20004000, LENGTH = 0x00004000
}

__bootrom_start__ = ORIGIN(bootrom);
__bootrom_size__ = LENGTH(bootrom);
__approm_start__ = ORIGIN(approm);
__approm_size__ = LENGTH(approm);
__eram_start__ = ORIGIN(eram);
__eram_size__ = LENGTH(eram);
```

In this case, `approm` is our app storage and `eram` is our executable RAM,
where we want to copy our program. Our bootloader needs to copy the code from
`approm` to `eram` before executing it.

We know from our previous blog post that executable code typically ends up in
the `.text` section so we must tell the linker that this section is **stored** in
`approm` but executed from `eram` so our program can execute correctly.

This is similar to our `.data` section, which is stored in `rom` but lives in
`ram` while the program is running. We use the `AT` linker command to specify
the storage region and the `>` operator to specify the load region.  This is the
resulting linker script section:

```
/* app.ld */
SECTIONS {
    .text :
    {
        KEEP(*(.vectors .vectors.*))
        *(.text*)
        *(.rodata*)
    } > eram AT > approm
    ...
}
```

We then update our bootloader to copy our code from one to the other before
starting the app:

```c
  /* booloader.c */

  /* copy app code to eram */
  uint32_t *src = (uint32_t*) &__approm_start__;
  uint32_t *dst = (uint32_t*) &__eram_start__;
  int size = (int) &__approm_size__;
  printf("Copying firmware from %p to %p\n", src, dst);
  memcpy(dst, src, size);

  /* find app start & SP */
  uint32_t app_sp = dst[0];
  uint32_t app_start = dst[1];

  /* cleanup peripherals here we may have initialized */

  /* start the app */
  start_app(app_start, app_sp);
```


### Locking the bootloader with the MPU

Last but not least, we can protect the bootloader using the memory protection
unit to make it inaccessible from the app. This prevents accidentally erasing
the bootloader during execution.

If you do not know about the MPU, check out [Chris’s excellent blog post from a few
weeks ago](https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu).

Remember that our MPU regions must be power-of-2 sized. Thankfully, our
bootloader already is! `0x4000` is 2^14 bytes.

We add the following MPU code to our bootloader:

```c
/* bootloader.c */
int main(void) {
  /* ... */
  base_addr = 0x0;
  *mpu_rbar = (base_addr | 1 << 4 | 1);
  //  AP=0b110 to make the region read-only regardless of privilege
  //  TEXSCB=0b000010 because the Code is in "Flash memory"
  //  SIZE=13 because we want to cover 16kiB
  //  ENABLE=1
  *mpu_rasr = (0b110 << 24) | (0b000010 << 16) | (13 << 1) | 0x1;

  start_app(app_start, app_sp);

  /* Not reached */
  while (1) {}
}
```
