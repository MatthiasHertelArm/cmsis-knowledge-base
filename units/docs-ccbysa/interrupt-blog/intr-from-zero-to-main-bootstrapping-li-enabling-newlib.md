---
id: "intr-from-zero-to-main-bootstrapping-li-enabling-newlib"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Implementing Newlib / Enabling Newlib"
summary: "Newlib is enabled by default when you build a project with arm-none-eabi-gcc. Indeed, you must explicitly opt-out with -nostdlib if you prefer to build your firmware without it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#enabling-newlib"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementing Newlib_

Newlib is enabled **by default** when you build a project with
`arm-none-eabi-gcc`. Indeed, you must explicitly opt-out with `-nostdlib` if you
prefer to build your firmware without it.

This is what we do for our “minimal” example, to guarantee we do not include any
libc functionality by mistake.

```makefile
PROJECT := minimal
BUILD_DIR ?= build

CFLAGS += -nostdlib

SRCS = \
	startup_samd21.c \
	$(PROJECT).c

include ../common-standalone.mk
```

It is very easy to add a dependency on the C standard library without meaning
to, as GCC will sometimes use standard C functions implicitly. For example,
consider this code used to zero-initialize a struct:

```c
int main() {
  int b[50] = {0}; // zero initialize a struct
  /* ... */
}
```

We added no new `#include`, nor any call to C library functions. Yet if we
compile this code with `-nostdlib`,  we’ll get the following error:

```shell
...
Linking build/minimal.elf
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: build/objs/a/b/c/minimal.o: in function `main':
/minimal/minimal.c:16: undefined reference to `memset'
collect2: error: ld returned 1 exit status
make: *** [build/minimal.elf] Error 1
```

If we remove `-nostdlib`, the program compiles and link without problems.

```shell
Linking build/minimal.elf
arm-none-eabi-objdump -D build/minimal.elf > build/minimal.lst
arm-none-eabi-objcopy build/minimal.elf build/minimal.bin -O binary
arm-none-eabi-size build/minimal.elf
   text    data     bss     dec     hex filename
   1292       0    8192    9484    250c build/minimal.elf
```

So here we are, using Newlib, and we did not have to do anything. Could it
really be this simple?

> Note: the variant of Newlib bundled with `arm-none-eabi-gcc` is not compiled
> with `-g`, which can make debugging difficult. For that reason, you may chose
> to replace it with your own build of Newlib. You can read more about that
> process in the [Implementing our own C standard library
> section](#implementing-our-own-c-standard-library) of this
> article.
