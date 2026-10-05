---
id: "intr-the-best-and-worst-gcc-compiler-fl-the-best-options-for-debugability-code-s"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best Options for Debugability & Code Size"
summary: "When a binary is loaded on an embedded device, it is important that debug information is included in the ELF. Otherwise, gdb (or your IDE) will not be able to display variables or backtraces."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#the-best-options-for-debugability-code-size"
license: "CC-BY-SA-4.0"
mode: "V"
---

### -g3

When a binary is loaded on an embedded device, it is important that debug information is included in the
ELF. Otherwise, gdb (or your IDE) will not be able to display variables or backtraces. There are many
"Debug Option" flags[^6] one can use to control the diagnostic information emitted.

Typically you will see a project use `-g` but consider compiling with `-g3`. It will include
a couple extra goodies such as macro definitions used in your application which can be useful to be
able to print in gdb especially when the definition comes from a chain of definitions.

You can try it out by compiling:

```bash
$ EXTRA_CFLAGS="-g" make
$ arm-none-eabi-readelf   --debug-dump=macro  build/examples.elf  | grep MEMFAULT_EXAMPLE_MACRO

(gdb) p/x MEMFAULT_EXAMPLE_MACRO
No symbol "MEMFAULT_EXAMPLE_MACRO" in current context.


$ EXTRA_CFLAGS="-g3" make
$ arm-none-eabi-readelf   --debug-dump=macro  build/examples.elf  | grep MEMFAULT_EXAMPLE_MACRO
DW_MACRO_define_strp - lineno : 13 macro : MEMFAULT_EXAMPLE_MACRO 0x4d

(gdb) p/x MEMFAULT_EXAMPLE_MACRO
$1 = 0x4d
```

### -Os

You can find all the details about optimization flags in the "Optimization Options" section of the
GNU GCC docs[^5]. `-Os`, optimize for size, is generally the optimization flag you will see used
for embedded systems. It enables a good balance of flags which optimize for size _as well as
speed_. Forgetting to flip on this flag can have serious code size impacts. For more details check
out the [interrupt series]() of posts about it!

### \-ffunction-sections, \-fdata-sections, & \-\-gc-sections

Clearly a favorite of ours as we've touched upon these flags in several articles[^14] [^15] but
worth mentioning again. I've seen a surprising number of embedded projects over the years that
forgot to enable these flags for portions of the project.

By default the linker will place all functions in an object within the same linker "section". This
becomes very clear when examining the mapfile and seeing a bunch of symbols in the `.text` section.

```
 .text          0x0000000000008238       0x60 /var/folders/dm/b0yt_1d11z9d53rtsm3y74sm0000gn/T//ccqZLzPH.o
                0x0000000000008238                simple_math_get_sum
                0x0000000000008268                simple_math_get_delta
```

With `-ffunction-sections`, each function gets its own section:

```
 .text.simple_math_get_sum
                0x0000000000008238       0x30 /var/folders/dm/b0yt_1d11z9d53rtsm3y74sm0000gn/T//ccC7FiQW.o
                0x0000000000008238                simple_math_get_sum
 .text.simple_math_get_delta
                0x0000000000008268       0x30 /var/folders/dm/b0yt_1d11z9d53rtsm3y74sm0000gn/T//ccC7FiQW.o
                0x0000000000008268                simple_math_get_delta
```

As the linker resolves references between objects it will mark a section as used. A final
optimization pass it can make is to cull any unused sections. For larger projects, this will often
result in substantial code savings.

This optimization is enabled by passing `--gc-sections` to the linker. Diagnostic logs about the
sections dropped can also be displayed using `--print-gc-sections` linker option. Let's try it out:

```bash
$ EXTRA_CFLAGS="-ffunction-sections -fdata-sections" EXTRA_LDFLAGS="--gc-sections --print-gc-sections" make
arm-none-eabi/bin/ld: removing unused section '.text.variable_shadow_error_example2' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.text.flash_read' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.text.print_user_provided_buffer' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.text.printf' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.text.simple_math_get_delta' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.text.stack_usage_example' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.text.vla_stack_usage' in file '<path_to_file>'
arm-none-eabi/bin/ld: removing unused section '.comment' in file '<path_to_file>'
```

### -Wpadded

Warn if padding is added to a structure due to alignment requirements:

```c
#include <stddef.h>
#include <stdint.h>

// Note: clang will only warn in the below examples if there's an instance of a
// structure definition with a padding violation

// The below 'struct padded' causes this warning:
// <source>:8:1: warning: padding struct size to alignment boundary [-Wpadded]
//     8 | };
//       | ^
struct padded {
  uint16_t a;
  uint8_t b;
} padded;

// The below 'struct aligned' causes this warning:
// <source>:14:14: warning: padding struct to align 'a' [-Wpadded]
//    14 |     uint16_t a;
//       |              ^
struct aligned {
  uint8_t b;
  uint16_t a;
} aligned;

// The same struct, but force packed- no warning is emitted because no padding
// is added. Note that this can have negative effects on code generated to
// access struct members; this should really only be used for structures that
// need to be consistently laid out for external interfaces (eg a SPI flash
// command data packet)
struct __attribute__((packed)) packed_aligned {
  uint8_t b;
  uint16_t a;
} packed_aligned;

// This structure is aligned to field widths, and there's some manual padding at
// the end to fill unused space; since all memory in the structure has a type
// associated with it, an added benefit is C initializer rules will allow us to
// safely use eg 'memcmp' when comparing (initialized) instances of the
// structure. See https://godbolt.org/z/5Wdhdx for an example of how this can
// fail otherwise!
struct naturally_aligned {
  uint32_t a;
  uint16_t b;
  uint8_t c;
  uint8_t _pad[1];
};

// memcmp(&one, &two, sizeof(one)) == 0
struct naturally_aligned one = {0}, two = {0};

// Confirm all the fields in 'struct naturally_aligned' are where we think they
// should be, and the total structure size matches expectation
_Static_assert(offsetof(struct naturally_aligned, a) == 0, "ok");
_Static_assert(offsetof(struct naturally_aligned, b) == 4, "ok");
_Static_assert(offsetof(struct naturally_aligned, c) == 6, "ok");
_Static_assert(sizeof(struct naturally_aligned) == 8, "ok");
```

This warning is helpful if you want to optimize the structure definitions in
your program (could be considered in a last-stakes optimization effort, or if
you're interested in really polishing those structure definitions). It can be
quite an exuberant warning in existing codebases.

The [pahole](https://linux.die.net/man/1/pahole) utility can be used on an
existing elf to scan for padded struct definitions, or if you really wanted to,
as part of a CI step banning unoptimized structure definitions 😅 though the
compiler flag should be enough.

I'd be remiss if I left out a reference to this legendary article, ["The Lost
Art of Structure Packing"](http://www.catb.org/esr/structure-packing/)
