---
id: "intr-the-best-and-worst-gcc-compiler-fl-fshort-enum"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Worst / -fshort-enum"
summary: "A really unfortunate flag that is hard to avoid is -fshort-enum. This flag allows the compiler to change the type of an enum based on the declared range of values. For example,"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#fshort-enum"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Worst_

A really unfortunate flag that is hard to avoid is `-fshort-enum`. This flag allows the compiler to change the type of an enum based on the declared range of values. For example,

```c
enum StatusCode {
  kStatusCode_Success = 0,
  kStatusCode_Failure = 0xff,
}
```

would be stored in a single byte type such as a `uint8_t` since the range is from 0 to 255 and

```c
enum StatusCode {
  kStatusCode_Success = 0,
  kStatusCode_Failure = 0xffffffff,
}
```

would be stored in a four byte type such as a `uint32_t` since the range is from 0 to `UINT32_MAX`.

Some of the blame here is on the C specification & ARM ABI itself which supports two modes for
representing enums. Section "7.1.3 Enumerated Types" of the ARM Procedure Call Standard
documentation[^13] states that the two permitted ABI variants for enumeration types are:

> - An enumerated type normally occupies a word (int or unsigned int). If a word cannot represent all
>   of its enumerated values the type occupies a double word (long long or unsigned long long).
> - The type of the storage container for an enumerated type is the smallest integer type that can contain all of its enumerated values

There a few key disadvantages of truncating enums to the shortest width type:

- Binary compatibility can be broken if the values in an enum change between releases. For example, if the max value in
  one version is 255 and then in a future version it's 4096, the size of the enum will change from a
  1-byte to a 2-byte representation. This means linking against a pre-compiled library using the older version
  of the enum will no longer work.
- When operations are performed on sizes that don't match the size of the architecture, extra
  instructions are often needed to mask out bits in the register, which uses more code space. This
  can easily be seen with the for loop example below.
- Enum types can wind up in packed structures. Changing the legal values of an enum can then cause
  unexpected breakages because the size of the enum member and consequently the structure will
  change. If an enum is used in a struct saved on flash, for example, after a firmware update the
  code may no longer be able to read the data from flash correctly.

#### Comparison of for loop using uint8_t and int

The following is an example of how operating on a shorter width type (`uint8_t`) requires an extra
masking instruction than operating on a type aligned with the architecture register size
(`int`). When an enum is truncated to a smaller width, the same type of masking instructions may be
needed when operations are performed with it.

```c
//! 0000807c <simple_for_loop_with_byte>:
//!    807c:       2300            movs    r3, #0
//!    807e:       461a            mov     r2, r3
//!    8080:       b2d9            uxtb    r1, r3
//!    8082:       4288            cmp     r0, r1
//!    8084:       d801            bhi.n   808a <simple_for_loop_with_byte+0xe>
//! -- Extra instruction for masking so register holds a uint8_t
//!    8086:       b2d0            uxtb    r0, r2
//!    8088:       4770            bx      lr
//!    808a:       441a            add     r2, r3
//!    808c:       3301            adds    r3, #1
//!    808e:       e7f7            b.n     8080 <simple_for_loop_with_byte+0x4>
//! Total function size: 20 bytes (10 instructions)
uint8_t simple_for_loop_with_byte(uint8_t max_value) {
  int sum = 0;
  for (uint8_t i = 0; i < max_value; i++) {
    sum += i;
  }
  return sum;
}

//! 00008090 <simple_for_loop_with_word>:
//!    8090:       2300            movs    r3, #0
//!    8092:       461a            mov     r2, r3
//!    8094:       4298            cmp     r0, r3
//!    8096:       dc01            bgt.n   809c <simple_for_loop_with_word+0xc>
//!    8098:       4610            mov     r0, r2
//!    809a:       4770            bx      lr
//!    809c:       441a            add     r2, r3
//!    809e:       3301            adds    r3, #1
//!    80a0:       e7f8            b.n     8094 <simple_for_loop_with_word+0x4>
//! Total function size: 18 bytes (9 instructions)
int simple_for_loop_with_word(uint8_t max_value) {
  int sum = 0;
  for (int i = 0; i < max_value; i++) {
    sum += i;
  }
  return sum;
}
```

#### What to do?

The arm toolchain by default is compiled with `-fshort-enum` so if you are using standard
libraries (such as newlib libc). You can disable short enums by setting the `-fno-short-enum` flag
but if you try to link against a unit that enables short enums (such as newlib) you will see the
following linker warning:

```c
arm-none-eabi/bin/ld: warning: <path_to_file> uses 32-bit enums yet the output is to use variable-size enums; use of enum values across objects may fail
```

When compiling with `-nostdlib` and linking your own libc implementation, it's worth
considering compiling with `-fno-short-enum` so all your enums are a fixed width and cannot change
over time.

Due to the nuances of enums in C, never use enums directly in packed structures. Instead use a type
with a constant size and assert if the enum does not fit within the allocated size.

```c
typedef struct __attribute__((packed)) {
  uint32_t status; // for enum StatusCode
} my_packed_struct;

_Static_assert(
  sizeof(enum StatusCode) <= sizeof(((0*)my_packed_struct)->status),
  "enum does not fit within structure member")
```
