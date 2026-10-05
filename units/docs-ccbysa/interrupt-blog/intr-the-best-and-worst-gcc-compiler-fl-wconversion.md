---
id: "intr-the-best-and-worst-gcc-compiler-fl-wconversion"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -Wconversion"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#wconversion"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

When arithmetic operations are performed on integer types (i.e `uint8_t`, `int8_t`, `uint16_t`,
etc) a set of implicit conversions on the types can take place. First **integer promotion**
occurs. The C standard defines this as[^17]:

> If an **int** can represent all values of the original type (as restricted by the width, for a
> bit-field), the value is converted to an **int**; otherwise, it is converted to an **unsigned
> int**.

Then the following set of rules are applied to the promoted values:

> 

It can be hard to keep track of the set of conversions taking place but fortunately the
`-Wconversion` option can be used to generate warnings when **implicit** conversions that are
likely to change the underlying value take place. This warning can be tedious to eliminate from a codebase
but I've seen it help catch real bugs on numerous occasions in the past.

Consider the following simple example as an illustration:

```c
uint8_t conversion_error_example(uint32_t val1, uint8_t val2) {
  uint8_t step1 = val1 * val2;
  int final_step = step1 / val2;
  return final_step;
}
```

```bash
$ EXTRA_CFLAGS="-Wconversion -Werror" make
main.c: In function 'conversion_error_example':
main.c:91:19: error: conversion from 'long unsigned int' to 'uint8_t' {aka 'unsigned char'} may change value [-Werror=conversion]
   uint8_t step1 = val1 * val2;
                   ^~~~
main.c:94:10: error: conversion from 'int' to 'uint8_t' {aka 'unsigned char'} may change value [-Werror=conversion]
   return final_step;
```
