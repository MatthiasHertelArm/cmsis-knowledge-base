---
id: "intr-device-firmware-update-cookbook-design-patterns-recipes"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Design Patterns & Recipes"
summary: "I have put together a full implementation of the Bootloader, the Loader, and the Application in the Interrupt Github repository."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#design-patterns-recipes"
license: "CC-BY-SA-4.0"
mode: "V"
---

I have put together a full implementation of the Bootloader, the Loader, and the
Application in the [Interrupt
Github
repository](https://github.com/memfault/interrupt/tree/master/example/fwup-architecture).
While discussing every line in detail is outside of the scope of this
conversation, I want to highlight a few patterns I have learned over the years.
These include ways to package firmware images, write them to flash, share data
between programs, and more!

This post builds upon many ideas previously written about on Interrupt. If you
haven't read them already, I recommend the following:
* [How to Write a Bootloader from Scratch](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch)
* [How to Write Linker Scripts for Firmware](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware)
* [GNU Build IDs for Firmware](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware)
* [Building a Tiny CLI Shell for Tiny Firmware](https://interrupt.memfault.com/blog/firmware-shell)
