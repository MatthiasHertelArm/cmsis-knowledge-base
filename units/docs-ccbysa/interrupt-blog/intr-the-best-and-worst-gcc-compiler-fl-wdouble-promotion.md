---
id: "intr-the-best-and-worst-gcc-compiler-fl-wdouble-promotion"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -Wdouble-promotion"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#wdouble-promotion"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

The C types `float` and `double` are not the same! A `float` represents an IEEE single precision
floating point number whereas a `double` represents double precision floating point number. ARM
Cortex-M MCUs with a Floating Point Unit (FPU) only natively supports single precision floating
point numbers. This means when a `double` is used, the compiler will need to emulate the operation with a
function (instead of a native instruction). If you examine the output of code using a `double`, you will see functions like
`__aeabi_d2f` in the code.

Using a `double` not only affects performance since the instruction is not supported natively but
also bloats the codesize because it pulls in some not-so-small functions.

When using floating point numbers in a project, it's quite easy to unintentionally use a `double`:

```c
bool float_promotion_example(float val) {
  return val > 2.6;
}
```

which results in a code size of:

```bash
$ arm-none-eabi-size build/examples.elf
   text    data     bss     dec     hex	filename
   1420       4       0    1424     590	build/examples.elf

# Look at large emulated instructions pulled into project
$ arm-none-eabi-nm -S -l --size-sort build/examples.elf  | grep aeabi
00008518 00000010 T __aeabi_cdcmpeq
00008518 00000010 T __aeabi_cdcmple
00008528 00000012 T __aeabi_dcmpeq
00008564 00000012 T __aeabi_dcmpge
00008578 00000012 T __aeabi_dcmpgt
00008550 00000012 T __aeabi_dcmple
0000853c 00000012 T __aeabi_dcmplt
00008388 0000001e T __aeabi_ui2d
00008508 00000020 T __aeabi_cdrcmple
000083a8 00000022 T __aeabi_i2d
000083cc 00000042 T __aeabi_f2d
00008420 0000005a T __aeabi_l2d
00008410 0000006a T __aeabi_ul2d
00008110 00000276 T __aeabi_dadd
0000810c 0000027a T __aeabi_dsub
```

The reason a double gets used above is because according to the C standard a floating point
constant, i.e `2.6`, will be of a `double` type. To use a float, the constant must be declared
as `2.6f`.

Fortunately, a warning can be enabled to easily catch when this implicit double promotion takes place:

```bash
$ EXTRA_CFLAGS="-Wdouble-promotion -Werror" make
float_promotion.c: In function 'float_promotion_example':
float_promotion.c:4:14: error: implicit conversion from 'float' to 'double' to match other operand of binary expression [-Werror=double-promotion]
   return val > 2.6;
```

Let's fix the issue by replacing `2.6` with `2.6f` and recompile:

```bash
$ EXTRA_CFLAGS="-Wdouble-promotion -Werror" make && arm-none-eabi-size build/examples.elf
   text    data     bss     dec     hex	filename
   244        4       0     248      f8	build/examples.elf

$ arm-none-eabi-nm -S -l --size-sort build/examples.elf  | grep aeabi
```

We see all the compiler (`__aeabi_*`) functions are gone and we have saved nearly **1200 bytes** of codespace!
