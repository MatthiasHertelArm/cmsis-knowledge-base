---
id: "intr-pocket-article-how-to-implement-an-implementing-a-noinit-section"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM: Implementing a `.noinit` section"
summary: "If we want a section of RAM that is not initialized on startup, we can specify a dedicated region and output section for it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory#implementing-a-noinit-section"
license: "CC-BY-SA-4.0"
mode: "V"
---

If we want a section of RAM that is _not_ initialized on startup, we can specify
a dedicated region and output section for it. The following example is for GNU
`ld`-compatible linker scripts (applies to GNU `ld` and LLVM `lld`, and
toolchains based on those).

```c
MEMORY
{
  FLASH  (rx)  : ORIGIN = 0x08000000, LENGTH = 1M
  RAM    (rwx) : ORIGIN = 0x20000000, LENGTH = 128K - 0x100
  /* Put a noinit region at the top 256 bytes of RAM  */
  NOINIT (rwx) : ORIGIN = 0x20000000 + 128K - 0x100, LENGTH = 0x100
}

SECTIONS
{
  ...
  .noinit (NOLOAD):
  {
    /* place all symbols in input sections that start with .noinit */
    KEEP(*(*.noinit*))
  } > NOINIT
  ...
}
```

> Note that we're using the arithmetic support in ld to compute the origin of
> the `NOINIT` region; purely optional, the start positions could easily be
> hard-coded too (and might be preferable, since it would be more explicit! see
> <https://www.python.org/dev/peps/pep-0020/>)

Now any symbol that's placed into a `.noinit*` section will be located in the
specified region, and _will not_ be initialized by our program's startup code!

To place a symbol into a `.noinit` region, see the following C code examples:

```c
// For GCC or Clang or derived toolchains, use the "section" __attribute__ .
__attribute__((section(".noinit"))) volatile int my_non_initialized_integer;

// for IAR EWARM, it varies, but typically:
__no_init volatile int my_non_initialized_integer @ ".noinit";
```

> Note that it may be necessary to mark the variables as "volatile" (as in the
> example above) to ensure the compiler doesn't optimize away the "store"
> instructions! when in doubt, check the generated assembly where the variable
> is accessed (for example, by running gdb with the .elf, and using the
> `disassemble /s <function>` command) If your system does require volatile, it
> might be worth adding a comment explaining why, since it's usually quite rare
> that volatile is needed.

We can verify that our symbol ended up in the correct location by looking at the
`.map` file (add `-Wl,-Map=app.map` to the linker flags):

```plaintext
.noinit         0x000000002001ff00       0x04
 *(*.noinit*)
 .noinit        0x000000002001ff00       0x04 build/src/main.o
                0x000000002001ff00                my_non_initialized_integer
```

We can also look at our binary with the `size` binutil and see the new section:

```bash
❯ arm-none-eabi-size -Ax build/main.elf
build/bootloader.elf  :
section                size         addr
.text                0x1314    0x8000000
.data                  0x78   0x20000000
.bss                   0xdc   0x20000078
.noinit                0x10   0x2001ff00
```
