---
id: "intr-the-best-and-worst-gcc-compiler-fl-additional-resources"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: Additional Resources"
summary: "If you'd like to check the flags used in various compilation units in your application, as long as you are compiling with -g, the elf will contain this information, i.e:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#additional-resources"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you'd like to check the flags used in various compilation units in your application, as long as
you are compiling with `-g`, the elf will contain this information, i.e:

```
$ arm-none-eabi-readelf --debug-dump=info  build/examples.elf | grep "DW_AT_producer"
    <c>   DW_AT_producer    : (indirect string, offset: 0x0): GNU C17 8.3.1 20190703 (release) [gcc-8-branch revision 273027] -mthumb -mfloat-abi=hard -mfpu=fpv4-sp-d16 -mcpu=cortex-m4 -march=armv7e-m+fp -g -Os
[...]
```

If you enjoy staying up to date with the latest compiler options available, the GCC
[release notes](https://gcc.gnu.org/gcc-9/changes.html) are an excellent resource.

If you want to use the absolute latest version of GCC for ARM,
[Arch Linux](https://www.archlinux.org/packages/community/x86_64/arm-none-eabi-gcc/) generally has
bleeding edge version of the toolchain available for install on the OS.
