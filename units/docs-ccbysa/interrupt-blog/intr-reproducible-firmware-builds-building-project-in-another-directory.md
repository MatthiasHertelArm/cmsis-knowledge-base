---
id: "intr-reproducible-firmware-builds-building-project-in-another-directory"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Building Project In Another Directory"
summary: "Instead of cloning the repo in the /private/tmp/repos/ directory, let's walk through the same steps but use the /private/tmp/dev/ directory instead."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#building-project-in-another-directory"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

Instead of cloning the repo in the `/private/tmp/repos/` directory, let's walk through the same steps but use the `/private/tmp/dev/` directory instead.

```bash
$ mkdir -p /private/tmp/dev
$ cd /private/tmp/dev && git clone git@github.com:memfault/interrupt.git
$ cd interrupt/example/reproducible-build/
$ make
[...]
Linking library
Generated build/nrf52.elf
$ arm-none-eabi-gdb-py --eval-command="target remote localhost:2331" --ex="mon reset" --ex="load" --ex="mon reset" --se=build/nrf52.elf
[...]
(gdb) continue
Program received signal SIGTRAP, Trace/breakpoint trap.
0x0000014c in my_fault_handler_c (frame=0x200007a8 <ucHeap+1140>) at /private/tmp/dev/interrupt/example/reproducible-build/startup.c:87
87    HALT_IF_DEBUGGING();
```

Now when we start the application, we crash on boot. How strange!
