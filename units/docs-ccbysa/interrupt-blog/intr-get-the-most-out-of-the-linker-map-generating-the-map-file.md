---
id: "intr-get-the-most-out-of-the-linker-map-generating-the-map-file"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Generating the map file"
summary: "To get started, make sure you generate the map file as part of your build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#generating-the-map-file"
license: "CC-BY-SA-4.0"
mode: "V"
---

To get started, make sure you generate the map file as part of your build.

Using GNU binutils, the generation of the map file must be explicitly requested by setting the right flag. To print the map to `output.map` with LD:

```Makefile
LDFLAGS += -Wl,-Map=output.map
```

As an example for a simple program, you would link the compilation units using those commands:

```bash
# Compile/assemble source files without linking
$ gcc -c sourcefile1.c sourcefile2.c
# Link together following the linker script specs and outputs map file with the link results
$ ld -Map output.map -T linker_script.ld -N -o output.elf sourcefile1.o sourcefile2.o
```

Most compilers have an option to enable the same kind of file, `--map` for the ARM compiler for example.
