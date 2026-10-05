---
id: "intr-tools-we-use-installing-gdb-for-ar-binaries-from-arm"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / Binaries from ARM"
summary: "ARM ships full prebuilt GCC + Binutils toolchains for Linux, Windows, and Mac. These were originally hosted on launchpad.net, but were moved here around 2016:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#binaries-from-arm"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

ARM ships full prebuilt GCC + Binutils toolchains for Linux, Windows, and Mac.
These were originally hosted on launchpad.net, but were moved here around 2016:

<https://developer.arm.com/downloads/-/gnu-rm>

In 2022, the downloads relocated again to this page:

<https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/downloads>

These packages are very handy- they include the following components:

- GCC compiler
- all binutils
  - GDB
  - LD
  - objdump, etc
- prebuilt Newlib C library
- prebuilt "Newlib-Nano" reduced size C library
- various example linker scripts and startup files

Another benefit- you can have developers on Windows/Linux/Mac all using the same
version of the compiler (doesn't necessarily guarantee bit-for-bit reproducible
builds, but chances are pretty good).

The same tools can also easily be used in whatever CI system you are using.

Note that these packages are the officially supported toolchain from ARM itself.

There is one gotcha with these packages, though- the Python support is whatever
was configured at build time by ARM. This means if you're using [GDB's Python
API](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api), you'll
need to make sure your Python scripts/dependencies/interpreter matches the
interpreter embedded into GDB.

And in the latest release, Python support was dropped in the Mac release:

```bash
# check which dynamic libraries the mac arm-none-eabi-gdb binary depends on

# v11.2-2022.02 (no Python support 😔. note the *gdb-py binary is absent from
# the archive)
❯ llvm-otool-14 -L ~/Downloads/gcc-arm-11.2-2022.02-darwin-x86_64-arm-none-eabi/bin/arm-none-eabi-gdb
/home/noah/Downloads/gcc-arm-11.2-2022.02-darwin-x86_64-arm-none-eabi/bin/arm-none-eabi-gdb:
        /usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1281.100.1)
        /usr/lib/libiconv.2.dylib (compatibility version 7.0.0, current version 7.0.0)
        /usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 902.1.0)

# v10.3-2021.10 (python2.7! in 2021!)
❯ llvm-otool-14 -L ~/Downloads/gcc-arm-none-eabi-10.3-2021.10-mac/bin/arm-none-eabi-gdb-py
/home/noah/Downloads/gcc-arm-none-eabi-10.3-2021.10-mac/bin/arm-none-eabi-gdb-py:
        /usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.250.1)
        /System/Library/Frameworks/Python.framework/Versions/2.7/Python (compatibility version 2.7.0, current version 2.7.10)
        /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1575.17.0)
        /usr/lib/libiconv.2.dylib (compatibility version 7.0.0, current version 7.0.0)
        /usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.4)

# still present in the linux version of v11.2-2022.02 though. But it's a
# somewhat venerable python3.6, which I don't have installed right now 😅
❯ ldd ~/Downloads/gcc-arm-11.2-2022.02-x86_64-arm-none-eabi/bin/arm-none-eabi-gdb
        linux-vdso.so.1 (0x00007ffd3fd4d000)
        libncursesw.so.5 => /lib/x86_64-linux-gnu/libncursesw.so.5 (0x00007f9f6c717000)
        libtinfo.so.5 => /lib/x86_64-linux-gnu/libtinfo.so.5 (0x00007f9f6c6e8000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f9f6c6e3000)
        libpython3.6m.so.1.0 => not found
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f9f6c6de000)
        libutil.so.1 => /lib/x86_64-linux-gnu/libutil.so.1 (0x00007f9f6c6d7000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f9f6c5f0000)
        libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f9f6c5bf000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f9f6c393000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f9f6c373000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9f6c14b000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f9f6c764000)
```

This could potentially be a pretty serious problem if there is some tooling or
scripting that uses the Python API and the release for your host system doesn't
have Python enabled.
