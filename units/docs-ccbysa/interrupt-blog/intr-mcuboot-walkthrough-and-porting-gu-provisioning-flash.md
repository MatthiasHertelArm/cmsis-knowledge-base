---
id: "intr-mcuboot-walkthrough-and-porting-gu-provisioning-flash"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Porting MCUboot / Provisioning Flash"
summary: "Now that we have a working build, we will need to allocate the flash available on our system to different \"flash areas\"."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#provisioning-flash"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Porting MCUboot_

Now that we have a working build, we will need to allocate the flash available on our system to
different "flash areas".

> For a production application, it's important to think through these allocations because once we have shipped a bootloader using them, we will not be able to change them!

Notably, for the flash storage available, we will need to look up the following for each flash available on the system:

* the total size of the flash
* the erase size of sectors within each flash

This information is generally available in one of the vendor datasheets or SDKs. For example, in
the NRF52840, we have 1MB of internal flash with erase sector sizes of 4kB.

> Fun fact: For other MCUs, the layout can be a bit more complex. For example, sometimes the first few sectors
>will be smaller (so a bootloader can be put in a small slot). In particular, the layouts for STM32 parts can get quite interesting:
>
> 


We saw above that the binary size of the bootloader is ~20kB  (`.text` + `.data`) so let's budget
for up to 32kB for bootloader space. We'll then use two (arbitrarily sized) 128kB slots for app images and leave the rest of internal flash for data storage.

This gives us the following target layout for our application:

|Slot | Flash Area Id |Start | End | Size
|Bootloader| 0 |0x0|0x8000| 32kB|
|App Primary Slot| 1|0x8000|0x28000| 128kB|
|App Upgrade Slot| 2|0x28000|0x48000| 128kB|
|Data Storage| |0x48000|0x100000| 736kB|


> For a real application, it's likely the configuration will be more complex than this. For example, the upgrade slot may live on external flash to support larger binaries on the device.
