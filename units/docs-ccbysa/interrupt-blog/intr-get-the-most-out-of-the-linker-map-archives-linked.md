---
id: "intr-get-the-most-out-of-the-linker-map-archives-linked"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Digging into the map files / Archives linked"
summary: "What? An archive in my binary? I'm only blinking an LED!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#archives-linked"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Digging into the map files_

What? An archive in my binary? I'm only blinking an LED!

Don't be afraid, the good news is that the map file does mention the specific symbols which caused the archive members to be brought in, in the first lines of the file.

Here are my first lines:

```
    Archive member included to satisfy reference by file (symbol)

    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-exit.o)
                                  /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/crt0.o (exit)
```

The format is:

```
    The archive file location (compilation unit)
    			The compilation unit referencing the archive (symbol called)
```

It means that a `crt0` file is calling the `exit` function from `exit.o` included in `libc_nano.a`.

The reason is not in the scope of this article, but there are indeed standard libraries that are provided by your toolchain (here the GNU toolchain). Those are available to provide standard functions such as `atoi`. In that example, I specified to the linker to use the `nano.specs` file. That's why standard functions all come from `libc_nano.a`. You can read more about this on [lb9mg.no](https://lb9mg.no/2018/08/14/reducing-firmware-size-by-removing-libc/).

Now, comparing the two generated map files, the first difference spotted is that some other archive members are included in the program: `atoi`, which itself needs `_strtol_r` which itself needs `_ctype_`:

```
    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-atoi.o)
                                  _build/nrf52840_xxaa/main.c.o (atoi)
    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-strtol.o)
                                  /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-atoi.o) (_strtol_r)
    /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-ctype_.o)
                                  /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-strtol.o) (_ctype_)
```

We now have a better sense of the files actually included into our program, and the reason why they are there. Let's explore what else is inside the file!
