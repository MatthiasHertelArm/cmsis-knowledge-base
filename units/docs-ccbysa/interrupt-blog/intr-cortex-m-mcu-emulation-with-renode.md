---
id: "intr-cortex-m-mcu-emulation-with-renode"
type: "concept"
domain: "debug"
title: "Cortex-M MCU Emulation with Renode"
summary: "In this new era of work-from-home, firmware engineers may not have all the equipment and development boards they are used to having at the office. One way around this? Emulation!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-23-intro-to-renode.md"
doc_source: "https://interrupt.memfault.com/blog/intro-to-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this new era of work-from-home, firmware engineers may not have all the
equipment and development boards they are used to having at the office. One way
around this? Emulation!

While they're not quite the real thing, emulators can run our firmware, print
data over UART, read registers from I2C sensors, and even run a filesystem on a
SPI flash device. That's more than enough to write some real firmware!



In this post, I walk through setting up the Renode emulator and running a
firmware in it for STM32. Using that setup, we'll debug our firmware, run it
through integrated tests, and shorten the iteration cycle of development.
