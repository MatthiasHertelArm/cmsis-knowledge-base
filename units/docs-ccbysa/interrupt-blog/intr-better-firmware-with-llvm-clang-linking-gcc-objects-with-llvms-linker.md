---
id: "intr-better-firmware-with-llvm-clang-linking-gcc-objects-with-llvms-linker"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Linking GCC Objects with LLVMs Linker"
summary: "The LLVM linker (ld.lld) [^9] strives to be a drop-in replacement for the GNU linkers and has come a long way in recent years in terms of compatibility."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#linking-gcc-objects-with-llvms-linker"
license: "CC-BY-SA-4.0"
mode: "V"
---

The LLVM linker (ld.lld) [^9] strives to be a drop-in replacement for the GNU linkers and has come a long way in
recent years in terms of compatibility.

There's some pretty bold claims made on the official docs that may make you want to try it out:

> LLD is very fast. When you link a large program on a multicore machine, you can expect that LLD runs more than twice as fast as the GNU gold linker. Your mileage may vary, though.

As of GCC9[^6], it is even possible to tell GCC to use it instead of the GNU linker with the
`-fuse-ld=lld` option:

```bash
$ export LLVM_BIN_PATH=$(dirname $(which ld.lld))
$ make clean
# NOTE: The -B<PATH> argument tells GCC to search PATH
# for binaries
$ CLI_LDFLAG_OVERRIDES="-B${LLVM_ROOT} -Wl,-fuse-ld=lld" \
  COMPILER=arm-none-eabi-gcc make
```
