---
id: "intr-from-zero-to-main-demystifying-fir-variables"
type: "concept"
domain: "debug"
title: "From Zero to main(): Demystifying Firmware Linker Scripts: Variables"
summary: "In the first post, our ResetHandler relied on seemingly magic variables to know the address of each of our sections of memory. It turns out, those variable came"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-25-how-to-write-linker-scripts-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#variables"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the first post, our `ResetHandler` relied on seemingly magic variables to know
the address of each of our sections of memory. It turns out, those variable came

In order to make section addresses available to code, the linker is able
to generate symbols and add them to the program.

You can find the syntax in the [linker
documentation](https://sourceware.org/binutils/docs/ld/Simple-Assignments.html#Simple-Assignments),
it looks exactly like a C assignment: `symbol = expression;`

Here, we need:

1. `_etext` the end of the code in `.text` section in flash.
2. `_sdata` the start of the `.data` section in RAM
3. `_edata` the end of the `.data` section in RAM
4. `_sbss` the start of the `.bss` section in RAM
5. `_ebss` the end of the `.bss` section in RAM

They are all relatively straightforward: we can assign our symbols to the value
of the location counter (`.`) at the start and at the end of each section
definition.

The code is below:

```
    .text :
    {
        KEEP(*(.vectors .vectors.*))
        *(.text.*)
        *(.rodata.*)
        _etext = .;
    } > rom

    .bss (NOLOAD) :
    {
        _sbss = . ;
        *(.bss .bss.*)
        *(COMMON)
        _ebss = . ;
    } > ram

    .data :
    {
        _sdata = .;
        *(.data*);
        _edata = .;
    } > ram AT >rom
```

One quirk of these linker-provided symbols: you must use a reference to
them, never the variable themselves. For example, the following gets us a
pointer to the start of the `.data` section:

```c
uint8_t *data_byte = &_sdata;
```

You can read more details about this in the [binutils
docs](https://sourceware.org/binutils/docs/ld/Source-Code-Reference.html).
