---
id: "intr-mcuboot-walkthrough-and-porting-gu-example-project-setup"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Example Project Setup"
summary: "In the sections that follow, we will explore in detail how to port MCUboot to a custom application."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#example-project-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the sections that follow, we will explore in detail how to port MCUboot to a custom application. If you would like to skip ahead and just try out the bootloader itself, you can build and flash the example bootloader and application included in the interrupt repository.

The example bootloader and application are bare-metal targets that expose a CLI which can be used for trying out MCUboot functionality.
The setup makes use of the following:

- a nRF52840-DK[^nrf5_sdk] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^jlink] as our gdbserver (V6.84a)
- GCC 9.3.1 / GNU Arm Embedded Toolchain as our compiler[^3]
- GNU Make as our build system
- the simple CLI shell [we built up in a previous post](https://interrupt.memfault.com/blog/firmware-shell).
- PySerial's `miniterm.py`[^miniterm] to connect to the serial console on the nRF52.

### Installing

Before you get started, I recommend doing a full chip erase on the development board to put the flash in a clean state

```bash
$ nrfjprog --eraseall
```

To flash the board, you will need to start a JLinkGDBServer:

```bash
$ JLinkGDBServer  -if swd -device nRF52840_xxAA  -nogui
```

In another terminal build and flash the bootloader:

```bash
$ git clone git@github.com:memfault/interrupt.git

$ cd example/mcuboot/bootloader/
$ make flash
$ Linking library
Generated bootloader/build/nrf52-bootloader.elf
Loading section .interrupts, size 0x240 lma 0x0
Loading section .text, size 0x4d57 lma 0x240
Loading section .data, size 0x9c lma 0x4f98
Start address 0x240, load size 20531
Transfer rate: 6683 KB/sec, 5132 bytes/write.
Resetting target
(gdb) c

```

In another terminal you can start a CLI and should see:

```
$ miniterm.py - 115200 --raw

[INF] Primary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
[INF] Secondary image: magic=unset, swap_type=0x1, copy_done=0x3, image_ok=0x3
[INF] Boot source: none
[INF] Swap type: none
[DBG] erasing trailer; fa_id=2
[DBG] flash_area_erase: Addr: 0x00047000 Length: 4096
```

You can then flash a working application by compiling and flashing the application.

```bash
$ cd example/mcuboot/application
$ make flash

$ make flash
Compiling external/MCUboot/boot/bootutil/src/bootutil_misc.c
Linking library
Restoring binary file application/build/nrf52-app.bin into memory (0x8000 to 0x9e58)
Resetting target
(gdb) c
```

From miniterm you should now see:

```
== Main Application Booted!==

shell>
```

### Testing Upgrade Functionality

#### 1. Compile a new Application

Compile a new application with some kind of change so you can easily confirm it was installed.

```diff
--- a/example/mcuboot/application/src/main.c
+++ b/example/mcuboot/application/src/main.c
@@ -39,7 +39,8 @@ int main(void) {
   // successfully completed init, mark image as stable
   boot_set_confirmed();

   EXAMPLE_LOG("==Main Application Booted==");
+  EXAMPLE_LOG("A modified application image");
```

```
$ cd example/mcuboot/application
$ make
```

#### 2. Install the application in the upgrade slot using GDB

```
(gdb) restore ../application/build/nrf52-app.bin binary 0x28000
```

#### 3. Kickoff image upgrade operation

Installing the image that has been written to the secondary slot can be kicked off using the `swap_images` CLI command

```
swap_images: Swap images
reboot: Reboot System
help: Lists all commands
shell> swap_images
...
Starting Main Application
  Image Start Offset: 0x8000
  Vector Table Start Address: 0x8200. PC=0x8771, SP=0x20002000
[DBG] writing image_ok; fa_id=1 off=0x1ffe8 (0x27fe8)
[DBG] flash_area_write: Addr: 0x00027fe8 Length: 4
==Main Application Booted==
A modified application image

shell>
```
