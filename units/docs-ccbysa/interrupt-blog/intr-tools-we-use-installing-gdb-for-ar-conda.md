---
id: "intr-tools-we-use-installing-gdb-for-ar-conda"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / Conda"
summary: "Conda is a cross-platform package manager, which we've written about before on Interrupt:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#conda"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

[Conda](https://conda.io/) is a cross-platform package manager, which we've
written about before on Interrupt:

- [Managing Developer Environments with
  Conda](https://interrupt.memfault.com/blog/conda-developer-environments)

It behaves quite similarly to system package managers, but can be used on
different hosts (Linux/Mac/Windows), so a development team can standardize
tooling without requiring a single host platform!

This is great! But there are a few downsides:

- same as with system package managers, we are relying on externally maintained
  tooling packages
- complex conda environments can get into dependency issues when updating
  packages
- not all packages will provide versions for all of Linux + Mac + Windows
- creating + maintaining conda packages can be pretty difficult, especially
  since cross-building conda packages is not yet fully supported

Plug (note: the author is an employee at Memfault), Memfault maintains conda
packages for multi-arch GDB:

- <https://anaconda.org/Memfault/multi-arch-gdb>
- <https://docs.memfault.com/docs/mcu/coredump-elf-with-gdb/#installing-multi-architecture-gdb-with-conda>
