---
id: "intr-cortex-m-mcu-emulation-with-renode-what-is-renode"
type: "concept"
domain: "debug"
title: "Cortex-M MCU Emulation with Renode: What is Renode?"
summary: "Renode is an open-source Emulator for embedded platforms. Today, it supports x86 (Intel Quark), Cortex-A (NVIDIA Tegra), Cortex-M, SPARC (Leon), and RISC-V based platforms."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-23-intro-to-renode.md"
doc_source: "https://interrupt.memfault.com/blog/intro-to-renode#what-is-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Renode](https://renode.io/) is an open-source Emulator for embedded platforms.
Today, it supports x86 (Intel Quark), Cortex-A (NVIDIA Tegra), Cortex-M, SPARC
(Leon), and RISC-V based platforms.

Renode can take the same firmware you are running in production, and run it
against emulated cores, peripherals, and even sensors and actuators. Better
yet, its extensive networking support and multi-system emulation make it a shoe
in for testing systems made up of multiple devices talking together.

With Renode, you can start development before your hardware is ready, test your
firmware without deploying racks of hardware, and shorten your iteration cycles
by cutting out flash loading delays.

Renode is built using the Mono framework, which allows it to run cross-platform.

> **Why not QEMU?** - Readers who have experience with emulation will point out
> that QEMU has existed for a long time, and is capable of emulating Cortex-M
> targets. In our experience, QEMU is focused on emulating systems meant for
> higher-level OSes (e.g. Linux computers) rather than embedded devices. To
> date, it only supports two cortex-M series targets, both made by TI.
