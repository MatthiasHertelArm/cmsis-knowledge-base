---
id: "intr-tools-we-use-installing-gdb-for-ar-build-from-source"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / Build from source"
summary: "Building a custom copy of GDB is one way to enable support for the necessary architecture."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#build-from-source"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

[Building a custom copy of GDB](https://interrupt.memfault.com/blog/gnu-binutils) is one
way to enable support for the necessary architecture.

You might for example build GDB enabling all targets:

```bash
❯ ./configure
  --target="arm-elf-linux"
  --enable-targets=all
  --with-python
❯ make -j $(nproc)
```

This results in a nicely tuned copy of GDB- you can select only the features
needed, enable different optimizations, select the correct Python version to
integrate, etc., and are in full control of your software supply chain!

The downsides of from-source builds (in general):

- can be challenging to build for Windows or other non-Unix platforms
- need to maintain build tooling + binary repositories
- using custom builds, you might encounter edge cases or warts that have been
  solved in more widely used copies of the same software

> Quick note- if you want to see which architectures a given `gdb` binary
> supports, here's a shell "one-liner" that can be useful (taken from
> [here](https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=gdb/gdb_buildall.sh;hb=4a94e36819485cdbd50438f800d1e478156a4889#l206)):
>
> ```bash
> gdb --batch -nx --ex 'set architecture' 2>&1 | \
>   tail -n 1 | \
>   sed 's/auto./\n/g' | \
>   sed 's/,/\n/g' | \
>   sed 's/Requires an argument. Valid arguments are/\n/g' | \
>   sed '/^[ ]*$/d' | sort | uniq
> ```
>
> Warning, this won't work with the built-in `sed` on macos, it's too old and
> doesn't have the necessary GNU extensions.
