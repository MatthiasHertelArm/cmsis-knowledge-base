---
id: "intr-mcuboot-walkthrough-and-porting-gu-triggering-firmware-upgrades-from-main-a"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Triggering Firmware Upgrades from Main Application"
summary: "MCUboot has a few functions that we will typically want to call from the main application to put the firmware update process in motion:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#triggering-firmware-upgrades-from-main-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

MCUboot has a few functions that we will typically want to call from the main application to put the
firmware update process in motion:

1. `boot_set_pending(int permanent)` - This triggers a write to the "image trailer" in flash that
   marks an upgrade of the primary slot to the data in the secondary slot has been requested. The
   swap can either be permanent or temporary. If it is temporary, `boot_set_confirmed()` must be
   called after the upgrade to prevent a revert to the previous image. Next time the bootloader
   starts, it will start to perform the operation requested.
2. `boot_set_confirmed()` - If `boot_set_pending` was called with `permanent=0`, the bootloader
   will swap back to the older image if a restart takes place and `boot_set_confirmed()` has not
   been called.

Both of these utilities can be picked up by compiling `bootutil_misc.c` and the `mcuboot_port.c` file into the main application which is what we have done for the example application.

I've added a `swap_images` CLI command which calls `boot_set_pending()` and triggers a
reboot. `boot_set_confirmed()` is called by the main application once initialization routines have
run successfully.

```c
static int prv_swap_images(int argc, char *argv[]) {
  EXAMPLE_LOG("Triggering Image Swap");

  const int permanent = 0;
  boot_set_pending(permanent);
  prv_reboot();
  return 0;
}
```

We can simulate a DFU by copying the application binary into our secondary slot for image 0 with GDB. Recall this slot starts at address `0x28000`:

```
(gdb) restore application/build/nrf52-app.bin binary 0x28000
```

After running the GDB command, we can call `swap_images` from the shell and we should see an upgrade kickoff in the bootloader:

```
shell> swap_images
Triggering Image Swap
[INF] Primary image: magic=good, swap_type=0x2, copy_done=0x1, image_ok=0x1
[INF] Secondary image: magic=good, swap_type=0x2, copy_done=0x3, image_ok=0x3
[INF] Boot source: none
[INF] Swap type: test
[DBG] erasing trailer; fa_id=1
[DBG] flash_area_erase: Addr: 0x00027000 Length: 4096
[DBG] initializing status; fa_id=1
# ...
[DBG] writing copy_done; fa_id=1 off=0x1ffe0 (0x27fe0)
[DBG] flash_area_write: Addr: 0x00027fe0 Length: 4
Starting Main Application
  Image Start Offset: 0x8000
  Vector Table Start Address: 0x8200. PC=0x8771, SP=0x20002000
```

Sweet, it works!
