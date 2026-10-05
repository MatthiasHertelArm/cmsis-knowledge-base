---
id: "llvmet-migrating-from-arm-gnu-toolchain-linker"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Linker"
summary: "lld is designed as a drop in replacement for GNU ld, however there are some known differences to take into account, see:  Linker Script implementation notes and policy in the LLD documentation.  The LLD and GNU linker incompatibilities blog post."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#linker"
license: "Apache-2.0"
mode: "V"
---

`lld` is designed as a drop in replacement for GNU `ld`,
however there are some known differences to take into account, see:
* [Linker Script implementation notes and policy](https://lld.llvm.org/ELF/linker_script.html)
in the LLD documentation.
* The [LLD and GNU linker incompatibilities](https://maskray.me/blog/2020-12-19-lld-and-gnu-linker-incompatibilities)
blog post.
* When selecting the printf/scanf picolibc implementation variant with `--defsym from=to`, see
[Printf and Scanf levels in Picolibc](https://github.com/picolibc/picolibc/blob/main/doc/printf.md#printf-and-scanf-levels-in-picolibc),
LLD includes not only the printf/scanf implementation variant from picolibc specified through `--defsym`, but
also the default PICOLIBC_DOUBLE_PRINTF_SCANF variant. To avoid linking the default variant into the application, you
must include the `--gc-sections` linker flag.
