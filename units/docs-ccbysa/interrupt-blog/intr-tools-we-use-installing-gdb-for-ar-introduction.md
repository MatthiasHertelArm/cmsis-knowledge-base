---
id: "intr-tools-we-use-installing-gdb-for-ar-introduction"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Introduction"
summary: "GDB, the GNU Project Debugger, is by default typically compiled to target the same architecture as the host system. When we talk about \"host\" and \"target architectures, what we mean is:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

GDB, the GNU Project Debugger, is by default typically compiled to target the
same architecture as the host system. When we talk about "host" and "target
architectures, what we mean is:

1. the **host** architecture: where the GDB program itself is run
2. the **target** architecture: where the program being debugged is run

Debugging a program that's running on the same machine as the host might look
like this:

[(figure: img/installing-gdb/gdb_host_target.drawio.svg)](https://interrupt.memfault.com/img/installing-gdb/gdb_host_target.drawio.svg)

In embedded engineering, we often want to target a foreign architecture (eg, the
embedded device, connected to some debug probe). That setup might look like
this:

[(figure: img/installing-gdb/gdb_cross_target.drawio.svg)](https://interrupt.memfault.com/img/installing-gdb/gdb_cross_target.drawio.svg)

We need a version of GDB that supports the target architecture of the program
being debugged.

In this article, we're interested in running GDB on an x86-64 or arm64 host and
debugging an arm-v7m (32-bit) target. Getting the right toolchain setup can be
tricky, especially if we want advanced features to be available. I'll go over
different approaches people use to download and setup GDB and explain the pros
and cons of each of them.
