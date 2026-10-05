---
id: "intr-peeking-inside-cmsis-packs-cmsis-pack-contents"
type: "concept"
domain: "debug"
title: "Peeking inside CMSIS-Packs: CMSIS-Pack Contents"
summary: "The format and associated tooling are described here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-07-cmsis-packs.md"
doc_source: "https://interrupt.memfault.com/blog/cmsis-packs#cmsis-pack-contents"
license: "CC-BY-SA-4.0"
mode: "V"
---

The format and associated tooling are described here:

> <https://arm-software.github.io/CMSIS_5/Pack/html/index.html>

A CMSIS-Pack is a ZIP file (with the `.pack` extension).

The actual contents of an individual pack can vary a lot, but in general,
there's the minimum items below (which are usually the most useful too):

1. a C header providing peripheral definition file for the chip(s) supported by
   the pack
2. startup files / linker scripts for various toolchains
3. SVD files that describe the peripheral registers
4. flash algorithms (FLM files) for reading + writing on-board non-volatile
   memory
5. peripheral driver files

There's often a lot more included in a Pack, for example:

- documentation (datasheets or user manuals)
- various tools (flash utilities, debug scripts)
- project templates
- board support packages
- middleware libraries
- sample projects
