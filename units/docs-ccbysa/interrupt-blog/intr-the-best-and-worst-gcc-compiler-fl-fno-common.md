---
id: "intr-the-best-and-worst-gcc-compiler-fl-fno-common"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -fno-common"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#fno-common"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

Ideally a codebase doesn't use many global variable declarations but I've seen so many libraries that do.

Consider the following situation where we have two c files which reference the same variable name
but intend to use the variable individually:

```c
//
// File main.c - g_variable defined for later use in the file

int g_variable = 4;

//
// File tentative_global.c
//
int g_variable;

void tentative_global_init(int initial_value) {
  g_variable = initial_value;
}

int tentative_global_increment(void) {
  g_variable++;
}
```

The confusing part here is that the snippet above will compile without any duplicate symbol
warning. This is because `int g_variable` without an initializer is a **tentative definition**. A
**tentative definition** does not initially allocate any space for the variable and at link time will
either be resolved to a pre-existing symbol if a symbol of the same name already exists or
otherwise space will be allocated.

This can lead to some confusing side effects if the programmer thinks unique instances of the
variable are being operated on within each c file.

A neat way to catch this kind of issue is to compile with `-fno-common` which disables the ability
for tentative definitions to be merged into a pre-existing definition. This will lead to a
duplicate symbol warning being emitted at link time:

```bash
$ EXTRA_CFLAGS=-fno-common make
arm-none-eabi/bin/ld: <path_to_file1.o>:(.bss+0x0): multiple definition of `g_variable'; <path_to_file2.o>:(.data+0x0): first defined here
```
