---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-gnu-binutils"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutils"
summary: "GNU Binutils is a collection of tools that can be used alongside GNU GCC to inspect and edit binaries."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#gnu-binutils"
license: "CC-BY-SA-4.0"
mode: "V"
---

GNU Binutils is a collection of tools that can be used alongside GNU GCC to inspect and edit binaries.
Most of these tools operate on ELFs, and for Linux as well as most embedded software, both the
individual object files (.o) and the final linked output (the ELF) are in this format.

### Installing Binutils with a Package Manager

Binutils can easily be installed with a package manager on OSX or Linux:

- OSX: `brew install binutils`
- Linux: `apt-get install binutils`

### Installing Binutils From Source

Sometimes it can be fun (or useful) to compile the latest GNU Binutil to get a preview of
unreleased features or customize the supported architecture targets in the build.
If you want to try compiling from source, you can run the following:

```
$ git clone git://sourceware.org/git/binutils-gdb.git
$ git log --oneline -1
3349112e38 elf: Remove zero-sized relocation section from section group
$ ./configure --prefix=/usr/local/binutils_latest/arm-none-eabi --target=arm-none-eabi
--with-python --disable-ld
$ make
$ # Wait 10-20 minutes ...
$ ./binutils/size --version
GNU size (GNU Binutils) 2.34.50.20200404
Copyright (C) 2020 Free Software Foundation, Inc.
This program is free software; you may redistribute it under the terms of
the GNU General Public License version 3 or (at your option) any later version.
This program has absolutely no warranty.
```

### Compiling Binutils For Multiple Targets

A typical GNU Binutil release will only include select targets. For example, the official GNU ARM
toolchain[^4] includes:

```
$ arm-none-eabi-addr2line --help | grep "supported targets"

arm-none-eabi-addr2line: supported targets: elf32-littlearm
elf32-littlearm-fdpic elf32-bigarm elf32-bigarm-fdpic elf32-little
elf32-big srec symbolsrec verilog tekhex binary ihex plugin
```

However, Binutils can be compiled to support multiple architectures / targets from the same binary!
If you are switching between architectures frequently, you can compile a
single Binutil's image by utilizing the `--enable-targets` configure option. You can either provide a comma separated list
of targets to enable a select subset or use `--enable-targets=all` to enable all supported targets
(which is over 250 targets!).
