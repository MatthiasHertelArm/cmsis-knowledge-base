---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-objcopy"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / objcopy"
summary: "objcopy is most commonly used as the last stage of a build to generate the .bin or .hex file which can be flashed onto a device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#objcopy"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`objcopy` is most commonly used as the last stage of a build to generate the `.bin` or `.hex` file which
can be flashed onto a device. Unlike an operating system where there is a "dynamic loader" that
resolves addresses and loads libraries at runtime, on embedded devices all of the memory locations
are typically resolved at link time.

```bash
$ arm-none-eabi-objcopy firmware.elf firmware.bin -O binary
```

> NOTE: For an example of using objcopy to build a bootloader for an embedded device,
> check out [this post](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#putting-it-all-together).

#### Converting Binaries into an Object (.o) File

For embedded development you may want to include binary artifacts into a firmware as a
byte array. For example, sometimes a firmware will include binaries that need to be loaded onto peripherals,
such as a GPS or accelerometer firmware image. One neat thing you can do with objcopy is convert
any binary blob into an object file that can then be linked in your image.

For example, if you want to include `my_binary.bin` in an image, you could create a `.o` as
follows:

```bash
$ arm-none-eabi-objcopy -I binary -O elf32-littlearm
   --add-section my_binary_section=my_binary.bin my_binary.bin
  my_binary.o
```

`objcopy` will emit symbols in the object that then make it easy to reference the blob from your
C Code:

```bash
arm-none-eabi-nm -S -l my_binary.o
00000031 D _binary_my_binary_bin_end
00000031 A _binary_my_binary_bin_size
00000000 D _binary_my_binary_bin_start
```
