---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-additional-tools-for-examining-elfs"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: Additional Tools for Examining ELFs"
summary: "There's a number of additional tools aside from GNU Binutils which I've found tremendously useful over the years."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#additional-tools-for-examining-elfs"
license: "CC-BY-SA-4.0"
mode: "V"
---

There's a number of additional tools aside from GNU Binutils which I've found tremendously useful
over the years. While a full discussion of them is outside the scope of this article (and merits a
blog post of their own), I've included some of my favorite highlights in the following sections.

### Godbolt (aka Compiler Explorer)

No discussion of binary inspection is complete without a shout out to Compiler Explorer. This is an online tool
that allows you to compile snippets of code against a ridiculous amount of different compilers. Even better you can
create short urls and share links with friends.

For example, [here is](https://godbolt.org/z/iqeNUv) an interesting one I was looking at recently.



For ARMv7-M, 4 byte loads and store instructions (`ldr` and `str`, respectively) support unaligned
access. When compiling code for space optimizations (using `-Os` CFLAG), I would have expected unaligned
accesses to get optimized using this instruction. What I noticed is for some reason if the
unaligned store is through a packed structure, the optimization does not take place.

### pyelftools

Pyelftools is a pure Python package capable of parsing ELF and DWARF information. If you are
looking to perform your own analysis on ELF files, I highly recommend checking out the
repo. There is an [examples](https://github.com/eliben/pyelftools/tree/master/examples) folder in
the project that you can use as inspiration to get started.

#### Pure Python GNU Binutils size Command Equivalent

As a quick example, we can implement an equivalent of the `size` binutil command in about 30 lines
of Python!

```python
# pyelftools_size.py
def _get_allocated_section_sizes(elffile):
    from elftools.elf.constants import SH_FLAGS

    text = data = bss = 0
    for section in elffile.iter_sections():
        sh_flags = section["sh_flags"]
        if sh_flags & SH_FLAGS.SHF_ALLOC == 0:
            continue  # Section is not in final binary

        section_size = section["sh_size"]

        if (sh_flags & SH_FLAGS.SHF_EXECINSTR != 0 or
            sh_flags & SH_FLAGS.SHF_WRITE == 0):
            text += section_size
        elif section["sh_type"] != "SHT_NOBITS":
            data += section_size
        else:
            bss += section_size

    return (text, data, bss)


def size_elf(fname):
    from elftools.elf.elffile import ELFFile

    with open(fname, "rb") as ef:
        text, data, bss = _get_allocated_section_sizes(ELFFile(ef))
    print(f"   text\t   data\t    bss\t    dec\t    hex\tfilename")
    tot = text + data + bss
    print(f"{text:7d}\t{data:7d}\t{bss:7d}\t{tot:7d}\t{tot:7x}\t{fname")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please specify a path to an ELF")
        exit(-1)
    size_elf(sys.argv[1])

```

We can compare the binutil size to the Python size to confirm it works!

```bash
$ python pyelftools_size.py nrf52_example/build/nrf52.elf
   text    data     bss     dec     hex	filename
   6340     244   11684   18268    475c	nrf52_example/build/nrf52.elf
$ arm-none-eabi-size nrf52_example/build/nrf52.elf
   text    data     bss     dec     hex	filename
   6340     244   11684   18268    475c	nrf52_example/build/nrf52.elf
```

### abidiff

[abidiff](https://sourceware.org/libabigail/manual/abidiff.html#) analyzes two ELFs and compares
them for compatibility. This can be an interesting tool to run on ELFs if you are linking libraries
compiled with multiple compilers or maintaining a third party binary SDK and want to catch
regressions. I assume you can ompile it yourself on OSX, but I typically just run it in an
ubuntu docker image and install via `apt-get`:

```
$ apt-get install libabigail
$ apt-get install abigail-tools
```

#### A Contrived Example

```c
// test.c
void my_public_function_1(void) {
}

#if ADD_NEW_API
void my_public_function_2(void) {
}
#endif
```

```bash
$ gcc -c test.c -o test_v1.o
$ gcc -c test.c -DADD_NEW_API=1 -o test_v2.o
```

```bash
$ abidiff test_v1.o test_v2.o
Functions changes summary: 0 Removed, 0 Changed, 0 Added function
Variables changes summary: 0 Removed, 0 Changed, 0 Added variable
Function symbols changes summary: 0 Removed, 1 Added function symbol not referenced by debug info
Variable symbols changes summary: 0 Removed, 0 Added variable symbol not referenced by debug info

1 Added function symbol not referenced by debug info:

  my_public_function_2
```

### LLVM

The LLVM project has [clones](https://llvm.org/docs/CommandGuide/index.html#gnu-binutils-replacements) of most of the
binutil commands we discussed above as well as a bunch of tools of its own. There's a healthy
competition between the LLVM and GNU projects which means if a new feature makes it to one of them,
there's typically work already underway to bring the other to parity. If you haven't looked at LLVM
before, it's definitely worth checking out!
