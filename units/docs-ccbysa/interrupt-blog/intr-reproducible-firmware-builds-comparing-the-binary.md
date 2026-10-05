---
id: "intr-reproducible-firmware-builds-comparing-the-binary"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Comparing the Binary"
summary: "At this point, what I like to do is diff the final binaries to see if they match:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#comparing-the-binary"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

At this point, what I like to do is diff the final binaries to see if they match:

```bash
$ cd /private/tmp
$ diff repos/interrupt/example/reproducible-build/build/nrf52.bin dev/interrupt/example/reproducible-build/build/nrf52.bin
Binary files repos/interrupt/example/reproducible-build/build/nrf52.bin and dev/interrupt/example/reproducible-build/build/nrf52.bin differ
```

Darn, they still differ. Sometimes a hexdump of the binary itself can give us clues:

```bash
$ sdiff -s <(xxd repos/interrupt/example/reproducible-build/build/nrf52.bin) <(xxd dev/interrupt/example/reproducible-build/build/nrf52.bin)
00000050: 0300 0000 474e 5500 4a8c 3651 f710 a3f6  ....GNU.J. |	00000050: 0300 0000 474e 5500 a3f4 c1f5 7500 cddb  ....GNU...
00000060: 63e7 2d9c a9c9 0aa4 38f4 9b54 0000 0000  c.-.....8. |	00000060: 5deb df50 e138 ff64 174c 6e12 0000 0000  ]..P.8.d.L
```

The "GNU" in the string in this case stands out. That's likely from the [GNU Build ID](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware) we are using in the firmware to _uniquely_ identify the compilation.

The GNU Build ID is a SHA computed over the binary sections _as well as_ the debug sections in an ELF.

If we run "strings" on either of the ELF files we will find the debug sections also include absolute paths:

```bash
$ arm-none-eabi-strings dev/interrupt/example/reproducible-build/build/nrf52.elf | grep private
[...]
/private/tmp/dev/interrupt/example/reproducible-build
/private/tmp/dev/interrupt/example/reproducible-build
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/include
/private/tmp/dev/interrupt/example/reproducible-build/freertos_kernel/portable/GCC/ARM_CM4F
/private/tmp/dev/interrupt/example/reproducible-build
```

Fortunately, the GNU toolchain has us covered!

{: #fdebug-prefix-map}
