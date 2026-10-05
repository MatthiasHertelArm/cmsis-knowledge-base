---
id: "intr-from-zero-to-main-how-to-write-a-b-why-you-may-need-a-bootloader"
type: "concept"
domain: "debug"
title: "From Zero to main(): How to Write a Bootloader from Scratch: Why you may need a bootloader"
summary: "Bootloaders serve many purposes, ranging from security to software architecture."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-13-how-to-write-a-bootloader-from-scratch.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#why-you-may-need-a-bootloader"
license: "CC-BY-SA-4.0"
mode: "V"
---

Bootloaders serve many purposes, ranging from security to software architecture.

Most commonly, you may need a bootloader to load your software. Some
microcontrollers like Dialog’s
[DA14580](https://www.dialog-semiconductor.com/products/connectivity/bluetooth-low-energy/smartbond-da14580-and-da14583)
have little to no onboard flash and instead rely on an external device to store
firmware code. In that case, it is the bootloader’s job to copy code from
non-executable storage, such as a SPI flash, to an area of memory that can be
executed from, such as RAM.

Bootloaders also allow you to decouple parts of the program that are mission
critical, or that have security implications, from application code which
changes regularly.  For example, your bootloader may contain firmware update
logic so your device can recover no matter how bad a bug ships in your
application firmware.

Last but certainly not least, bootloaders are an essential component of a
trusted boot architecture.  Your bootloader can, for example, verify a
cryptographic signature to make sure the application has not been replaced or
tampered with.
