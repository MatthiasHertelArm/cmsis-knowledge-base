---
id: "intr-reproducible-firmware-builds-making-the-elf-debug-info-the-same"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Making the ELF debug info the same"
summary: "We can use -fdebug-prefix-map=old=new[^6] to control what path is used to prefix debug information. We can add the following line to the CFLAGS in the makefile to make the path relative to the root directory!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#making-the-elf-debug-info-the-same"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

We can use `-fdebug-prefix-map=old=new`[^6] to control what path is used to prefix debug information. We can
add the following line to the `CFLAGS` in the makefile to make the path relative to the root directory!

```bash
CFLAGS += \
[...]
  -fdebug-prefix-map=$(ROOT_DIR)=.
```

Let's apply the fix:

```bash
$ cd /private/tmp/dev/interrupt/example/reproducible-build/
$ git apply 03-fdebug-prefix-map.patch
$ cd /private/tmp/repos/interrupt/example/reproducible-build/
$ git apply 03-fdebug-prefix-map.patch
```

#### Ensuring GDB can find source when using -fdebug-prefix-map

By default, GDB scans the current working directory and the compilation directory to lookup source code. If you do not invoke GDB from the root directory of the repo, you will need to use the `directory` command (or `--directory` CLI argument) to tell GDB where the root of the source code is:

```bash
$ /private/tmp/repos/interrupt/example/reproducible-build/build/
# arm-none-eabi-gdb-py --eval-command="target remote localhost:2331" --ex="mon reset" --ex="load" --ex="mon reset" --se=nrf52.elf
[...]
Reset_Handler () at startup.c:36
36	startup.c: No such file or directory.

===> Fixing source directory
(gdb) directory /private/tmp/repos/interrupt/example/reproducible-build/
Source directories searched: /private/tmp/repos/interrupt/example/reproducible-build:$cdir:$cwd
(gdb) list *Reset_Handler
0x1b0 is in Reset_Handler (startup.c:36).
34
35  void Reset_Handler(void) {
36    prv_cinit();
37
38    main();
```

After making the changes, let's recompile the project. Both binaries should now have the same build id!

```bash
$ make -C repos/interrupt/example/reproducible-build/
[...]
$ make -C dev/interrupt/example/reproducible-build/
[..]

$ arm-none-eabi-readelf -n build/nrf52.elf

Displaying notes found in: .gnu_build_id
  Owner                 Data size	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 6fe2c11e68fb1c664d6644322b1d4e51bd2114e8
$ arm-none-eabi-readelf -n build/nrf52.elf

Displaying notes found in: .gnu_build_id
  Owner                 Data size	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 6fe2c11e68fb1c664d6644322b1d4e51bd2114e8
```

Great, the Build IDs are an exact match. We could also diff the ELF files and confirm they are identical as well:

```
$ diff dev/interrupt/example/reproducible-build/build/nrf52.elf repos/interrupt/example/reproducible-build/build/nrf52.elf && echo "Artifacts Match"
Artifacts Match
```
