---
id: "pyocd-semihosting-building-into-firmware"
type: "concept"
domain: "debug"
title: "Semihosting: Building into firmware"
summary: "These are the steps, in short, for how to include semihosting support when linking firmware with gcc and newlib."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/semihosting.md#building-into-firmware"
license: "Apache-2.0"
mode: "V"
---

These are the steps, in short, for how to include semihosting support when linking firmware with gcc
and newlib.

- On the linker command line, add `--specs=rdimon.specs` and ensure `-nostartfiles` is not present.
- Call `initialise_monitor_handles()` from your firmware before using semihosting.

The C runtime stdio will now be connected with semihosting.

This small example shows how to init and use semihosting from gcc.

```c
#include <stdio.h>

extern void initialise_monitor_handles(void);

void main(void) {
    // init semihosting console
    initialise_monitor_handles();

    // say hello via semihosting
    printf("hello, world!\n");
}
```

These blog articles are also very helpful guides for using semihosting with gcc:

- [Introduction to ARM Semihosting](https://interrupt.memfault.com/blog/arm-semihosting) is an excellent
    overall introduction, including how to link in semihosting support for gcc and newlib-based projects.
- [Semihosting with GNU ARM Embedded (LaunchPad) and GNU ARM Eclipse Debug Plugins](https://mcuoneclipse.com/2014/09/11/semihosting-with-gnu-arm-embedded-launchpad-and-gnu-arm-eclipse-debug-plugins/)

For other toolchains, please see the vendor's documentation.
