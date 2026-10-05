---
id: "intr-from-zero-to-main-how-to-write-a-b"
type: "concept"
domain: "debug"
title: "From Zero to main(): How to Write a Bootloader from Scratch"
summary: "This is the third post in our Zero to main() series, where we bootstrap a working firmware from zero code on a cortex-M series microcontroller."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-13-how-to-write-a-bootloader-from-scratch.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is the third post in our [Zero to main() series](),
where we bootstrap a working firmware from zero code on a
cortex-M series microcontroller.

Previously, [we wrote a startup file to bootstrap our C environment](https://interrupt.memfault.com/blog/zero-to-main-1), and [a linker
script to get the right data at the right addresses](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware). These two will allow us to
write a monolithic firmware which we can load and run on our microcontrollers.

In practice, this is not how most firmware is structured. Digging through vendor
SDKs, you’ll notice that they all recommend using a *bootloader* to load your
applications. A bootloader is a small program which is responsible for loading
and starting your application.


In this post, we will explain why you may want a
bootloader, how to implement one, and cover a few advanced techniques you may
use to make your bootloader more useful.


> If you'd rather listen to me present this information and see some demos in action, watch
> [this webinar recording](https://hubs.la/Q02hgRrk0)
