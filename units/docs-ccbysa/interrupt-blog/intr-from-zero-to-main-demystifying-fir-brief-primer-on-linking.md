---
id: "intr-from-zero-to-main-demystifying-fir-brief-primer-on-linking"
type: "concept"
domain: "debug"
title: "From Zero to main(): Demystifying Firmware Linker Scripts: Brief Primer on Linking"
summary: "Linking is the last stage in compiling a program. It takes a number of compiled object files and merges them into a single program, filling in addresses so that everything is in the right place."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-25-how-to-write-linker-scripts-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#brief-primer-on-linking"
license: "CC-BY-SA-4.0"
mode: "V"
---

Linking is the last stage in compiling a program. It takes a number of compiled
object files and merges them into a single program, filling in addresses so
that everything is in the right place.

Prior to linking, the compiler will have taken your source files one by one and compiled
them into machine code. In the process, it leaves placeholders for
addresses as (1) it does not know where the code will end up within the broader
structure of the program and (2) it knows nothing about symbols outside of the
current file or compilation unit.

The linker takes all of those object files and merges them together along with
external dependencies like the C Standard Library into your program. To figure
out which bits go where, the linker relies on a linker script - a blueprint for
your program. Lastly, all placeholders are replaced by addresses.

We can see this at play in our minimal program. Let's follow what happens to
our `main` function in `minimal.c` for example. The compiler builds it into
an object file with:

```
$ arm-none-eabi-gcc -c -o build/objs/a/b/c/minimal.o minimal.c <CFLAGS>
```

We can dump symbols in `minimal.o` to look at `main` within it:

```
$ arm-none-eabi-nm build/objs/a/b/c/minimal.o
...
00000000 T main
...
```

As expected, it does not have addresses yet. We then link everything with:

```
$ arm-none-eabi-gcc <LDFLAGS> build/objs/a/b/c/minimal.o <other object files> -o build/minimal.elf
```

And dump the symbols in the resulting `elf` file:

```
$ arm-none-eabi-nm build/minimal.elf
...
00000294 T main
...
```

The linker has done its job, and our `main` symbol has been assigned an address.

The linker often does a bit more than that. For example, it can generate debug
information, garbage collect unused sections of code, or run whole-program
optimization (also known as Link-Time Optimization, or LTO). For the sake of
this conversation, we will not cover these topics.

For more information on the linker, there's a great thread on [Stack
Overflow](https://stackoverflow.com/questions/3322911/what-do-linkers-do).
