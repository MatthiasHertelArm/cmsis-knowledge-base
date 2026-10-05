---
id: "intr-gnu-build-ids-for-firmware-adding-the-gnu-build-id-to-your-builds"
type: "concept"
domain: "debug"
title: "GNU Build IDs for Firmware: Adding the GNU build ID to your builds"
summary: "In GCC, you can enable build IDs with the -Wl,--build-id which passes the --build-id flag to the linker. You can then read it back by dumping the notes section of the resulting elf file with readelf -n."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-29-gnu-build-id-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-build-id-for-firmware#adding-the-gnu-build-id-to-your-builds"
license: "CC-BY-SA-4.0"
mode: "V"
---

**Note**: all of our example are based on the
[minimal](https://github.com/memfault/zero-to-main/tree/master/minimal) program from our Zero to main()
series.

In GCC, you can enable build IDs with the `-Wl,--build-id` which passes the
`--build-id` flag to the linker. You can then read it back by dumping the notes
section of the resulting elf file with `readelf -n`.

By default, this is not enabled:

```terminal
francois-mba:minimal francois$ make clean all
...
arm-none-eabi-size build/minimal.elf
   text    data     bss     dec     hex filename
   1252       0    8192    9444    24e4 build/minimal.elf
...
francois-mba:minimal francois$ arm-none-eabi-readelf -n build/minimal.elf
[No output]
```

But a small change to the CFLAGS is all it takes:
```terminal
francois-mba:minimal francois$ CFLAGS="-Wl,--build-id" make clean all
build/minimal.elf
...
arm-none-eabi-size build/minimal.elf
   text    data     bss     dec     hex filename
   1288       0    8192    9480    2508 build/minimal.elf
francois-mba:minimal francois$ arm-none-eabi-readelf -n build/minimal.elf

Displaying notes found in: .note.gnu.build-id
  Owner                 Data size       Description
  GNU                  0x00000014       NT_GNU_BUILD_ID (unique build ID
bitstring)
    Build ID: bab6b09f86b3c3017499d8e386447a610c559bd5
```

As you can see, our binary now contains the build id
`bab6b09f86b3c3017499d8e386447a610c559bd5`.
