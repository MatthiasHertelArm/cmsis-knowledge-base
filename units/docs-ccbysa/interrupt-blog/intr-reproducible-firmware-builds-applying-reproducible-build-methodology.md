---
id: "intr-reproducible-firmware-builds-applying-reproducible-build-methodology"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Applying Reproducible Build Methodology During Development"
summary: "Over a projects lifetime, you will likely wind up making changes to the product that should have no impact on the final binary produced. Some examples of this type of change include:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#applying-reproducible-build-methodology-during-development"
license: "CC-BY-SA-4.0"
mode: "V"
---

Over a projects lifetime, you will likely wind up making changes to the product that should have **no** impact on the final binary produced. Some examples of this type of change include:

1. Migrating to a new build system (i.e Make to CMake)
2. Refactoring a Makefile to be more readable
3. Sorting headers in a C file to follow a coding convention
4. Fixing a new [compiler warning](https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#the-best-one-off-warning-options-options-not-covered-by--wall-or--wextra) that shouldn't impact the binary produced.
5. Refactoring a linker script so it's easier to extend

Some of these parts of a codebase can be "scary" ones to touch. By applying what we have learned above to debug how binaries differ, we can make these types of changes with confidence ... if we update a Makefile and don't expect a change in the binary but something _has_ changed, it likely means we have messed up! Let's walk through a quick example.

### Cleaning up a Makefile

In the Makefile for the example app we have been using in this article we have the following block:

```
INCLUDE_PATH_DIRS = \
  $(FREERTOS_PORT_ROOT) \
  $(FREERTOS_ROOT_DIR)/include \
  $(ROOT_DIR) \

INCLUDE_PATH_DIRS += $(ROOT_DIR)/include

INCLUDE_PATH_DIRS += $(ROOT_DIR)/config
```

Let's say we decide to clean this up by moving all the include paths into a single list:

```
INCLUDE_PATH_DIRS = \
  $(FREERTOS_PORT_ROOT) \
  $(FREERTOS_ROOT_DIR)/include \
  $(ROOT_DIR) \
  $(ROOT_DIR)/config \
  $(ROOT_DIR)/include
```

If you want to follow along, you can apply the patch locally:

```bash
$ cd /private/tmp/dev/interrupt/example/reproducible-build/
$ git apply 04-makefile-cleanup.patch
$ cd /private/tmp/repos/interrupt/example/reproducible-build/
$ git apply 04-makefile-cleanup.patch
```

If we have done things right, nothing in the project should change. Let's save a copy of the build and rebuild with the modification:

```bash
$ cd /private/tmp/repos/interrupt/example/reproducible-build/
$ cp build/nrf52.elf nrf52_original.elf
$ cp build/nrf52.bin  nrf52_original.bin
# Apply changes & rebuild
$ make
```

If we compare the Build IDs we see they are now different!

```bash
$ arm-none-eabi-readelf -n build/nrf52.elf

Displaying notes found in: .gnu_build_id
  Owner                 Data size	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 2b01965289ecab1bded71b8dffe0535661e7847a
$ arm-none-eabi-readelf -n nrf52_original.elf

Displaying notes found in: .gnu_build_id
  Owner                 Data size	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 6fe2c11e68fb1c664d6644322b1d4e51bd2114e8
```

We can compare the binaries like we did above. As we would expect the build IDs differ but now we also see a third row which differs:

```bash
sdiff -s <(xxd nrf52_original.bin) <(xxd build/nrf52.bin)
00000050: 0300 0000 474e 5500 6fe2 c11e 68fb 1c66  ....GNU.o. |	00000050: 0300 0000 474e 5500 2b01 9652 89ec ab1b  ....GNU.+.
00000060: 4d66 4432 2b1d 4e51 bd21 14e8 0000 0000  MfD2+.NQ.! |	00000060: ded7 1b8d ffe0 5356 61e7 847a 0000 0000  ......SVa.
000000d0: dc00 0020 03be 7047 13b5 0022 0821 0120  ... ..pG.. |	000000d0: dc00 0020 03be 7047 13b5 0022 0821 6420  ... ..pG..
```

#### Comparing objdump Output

Another thing we can do if the binaries are really close is to compare the assembly. This might give us a better clue as to what changed. Let's try it out:

```
sdiff -s <(arm-none-eabi-objdump -d nrf52_original.elf) <(arm-none-eabi-objdump -d build/nrf52.elf)
nrf52_original.elf:     file format elf32-littlearm       |	build/nrf52.elf:     file format elf32-littlearm
      de:	2001        movs	r0, #1            |       de:	2064        movs	r0, #100	; 0x6
```

We are loading the value of 100 into register r0 instead of 1 in the other build.
We can find what function this instruction is coming from by using addr2line:

```bash
arm-none-eabi-addr2line 0xde -e nrf52_original.elf
 ./main.c:61
```

or by dumping it in GDB:

```bash
(gdb) list *0xde
0xde is in main (main.c:61).
59
60	int main(void) {
==> CHANGE HERE
61   xQueue = xQueueCreate(MAIN_QUEUE_LENGTH, sizeof(uint64_t));
62    configASSERT(xQueue != NULL);
63
64    xTaskCreate(prvQueuePongTask,
65                "Ping", configMINIMAL_STACK_SIZE,
```

Per the [ARM procedure call standard](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#core-registers), `$r0` is used to hold the first argument for a function call. This means that the `$r0` operation we see above maps to `MAIN_QUEUE_LENGTH`. But how did that change between builds? Let's grep[^6] through the codebase to see where it is defined.

```bash
$rg "define.*MAIN_QUEUE_LENGTH"
config/config.h
1:#define MAIN_QUEUE_LENGTH 100

include/config.h
1:#define MAIN_QUEUE_LENGTH 1
```

#### Error Analysis

Oh interesting, the define is provided in two headers. In `main.c` we just include `"config.h"`. When the compiler tries to resolve include paths it will just walk through the list of includes we provided at compilation time _in order_. If we go back and re-examine the change made above, we can see that we accidentally changed the order of the includes. If we change the order back, we can recompile and confirm the build matches again!

> NOTE: A full discussion of C include path best practices is outside the scope of this article but this example raises one reason using a flat include structure can be dangerous. Because the path is not explicit, it's pretty opaque as to what include will path will be used. The bug above could have been avoided by not adding `-Iconfig/` to `CFLAGS` and instead requiring it be included explicitly (i.e `#include config/config.h`).
