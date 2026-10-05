---
id: "intr-peeking-inside-cmsis-packs-svd-file"
type: "concept"
domain: "debug"
title: "Peeking inside CMSIS-Packs: SVD File"
summary: "This is another XML file that contains information about the peripheral registers in the chip. Under certain conditions, it's invaluable; some examples I've used before:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-07-cmsis-packs.md"
doc_source: "https://interrupt.memfault.com/blog/cmsis-packs#svd-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is another XML file that contains information about the peripheral
registers in the chip. Under certain conditions, it's **_invaluable_**; some examples
I've used before:

- using [PyCortexMDebug in gdb](https://interrupt.memfault.com/blog/advanced-gdb#svd-files-and-peripheral-registers) to pretty-print register values while
  debugging 😍
- generating language bindings over the memory-mapped peripherals:
  <https://github.com/rust-embedded/svd2rust>

> Tip: always be careful when using these SVD files; they occasionally can
> have mistakes in them, which can be really confusing. When in doubt, check the
> datasheet or reference implementations (eg CMSIS headers) as a separate
> source.
