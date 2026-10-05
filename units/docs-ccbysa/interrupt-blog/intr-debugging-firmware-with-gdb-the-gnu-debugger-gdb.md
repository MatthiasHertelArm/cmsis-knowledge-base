---
id: "intr-debugging-firmware-with-gdb-the-gnu-debugger-gdb"
type: "concept"
domain: "debug"
title: "Debugging Firmware with GDB: The GNU Debugger (GDB)"
summary: "GDB was developed by Richard Stallman in 1986 as part of the GNU system. It is one of the most popular debuggers out there, and for many good reasons!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-21-gdb-for-firmware-1.md"
doc_source: "https://interrupt.memfault.com/blog/gdb-for-firmware-1#the-gnu-debugger-gdb"
license: "CC-BY-SA-4.0"
mode: "V"
---

GDB was developed by Richard Stallman in 1986 as part of the GNU system. It is one of the most popular debuggers out there, and for many good reasons!

Some of the most important are:

- GDB supports a vast number of architectures including: ARM, x86, MIPS, and many more. Because of this, a firmware developer's knowledge and expertise with GDB is potentially transferrable across many projects.
- GDB is command-line based which gives it high flexibility and usability in debugging tasks that require some level of automation. This became especially true with the release of the Python API for GDB in GDB's release version 7.0 (in 2011).
- GDB supports remote debugging. This is crucial for embedded systems where the development environment resides on an architecture different from the target system (e.g. developing on a Windows machine for an ARM-based target).

Because of these reasons, we believe it is extremely helpful for a firmware developer to at least get **some** exposure to using GDB.

In this post, we'll walk through setting up GDB for the following environment:

- A Nordic nRF52840 development kit
- A macOS machine as the development environment
- Running an example from the nRF5 SDK (version 15.3.0), specifically the UART example application.
- We'll be running a non-BLE peripheral example (UART) that does **not** use Nordic's SoftDevice. *Debugging nRF applications with SoftDevice can get complicated, so we'll leave that to a later post.*

We'll then go through demos of utilizing the most useful features of GDB to debug our example application.
