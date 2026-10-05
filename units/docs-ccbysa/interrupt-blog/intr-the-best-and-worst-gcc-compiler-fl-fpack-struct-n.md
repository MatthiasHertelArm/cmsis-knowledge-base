---
id: "intr-the-best-and-worst-gcc-compiler-fl-fpack-struct-n"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Worst / -fpack-struct=n"
summary: "When defining structures in C, members are aligned by their size. So for example, a uint16_t which is 2 bytes in size will always be aligned on a 2 byte boundary."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#fpack-struct-n"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Worst_

When defining structures in C, members are aligned by their size. So for example, a
`uint16_t` which is 2 bytes in size will always be aligned on a 2 byte boundary. This means there
is often some padding bytes inserted into the struct to achieve this alignment.

```c
typedef struct {
  uint8_t a; // at offset 0
  // 1 padding byte
  uint16_t b; // at offset 2
} my_struct;
```

Sometimes, a programmer may try to pack _all_ structs using `-fpack-struct` to save a little RAM space. This is a bad idea!
While it may reduce the RAM footprint of a codebase, it will wind up generating more code
because unaligned accesses to data generally require more instructions than aligned ones. This in
turn will impact performance. It also creates a problematic situation if you link static libraries compiled with and
without the flag because then the offset of the members within the struct will be different based
on the compilation unit!

When no value, n, is specified,`-fpack-struct` will pack all the structures in your
code such that there are no holes. When a value n is passed to pack struct, it will only force alignment of types greater than that
size along that boundary. So in the example below if we compile with `-fpack-struct`, members b & c
will be aligned but if we compile with `-pack-struct=4`, only c will be shifted.

```c
typedef struct {
  uint8_t a;
  uint16_t b;
  uint64_t c;
  uint32_t d;
} my_struct;

_Static_assert(offsetof(my_struct, a) == 0,
  "a not at offset 0 within struct");
_Static_assert(offsetof(my_struct, b) == 2,
    "b not at offset 2 within struct");
_Static_assert(offsetof(my_struct, c) == 8,
  "c not at offset 8 within struct");
_Static_assert(offsetof(my_struct, d) == 16,
  "d not at offset 16 within struct");
```

```bash
$ EXTRA_CFLAGS=-fpack-struct=4 make
main.c:30:1: error: static assertion failed: "c not at offset 8 within struct"
 _Static_assert(offsetof(my_struct, c) == 8, "c not at offset 8 within struct");
 ^~~~~~~~~~~~~~
main.c:31:1: error: static assertion failed: "d not at offset 16 within struct"
 _Static_assert(offsetof(my_struct, d) == 16, "d not at offset 16 within struct");
 ^~~~~~~~~~~~~~
```

> NOTE: Structure packing is extremely common in embedded devices. The use case
> is typically when some kind of data is being serialized and sent out over a
> transport or saved to some kind of persistent storage. This is done to save
> space and be portable -- compilers may pad the same struct differently. For
> example, on a 64 bit architecture, a struct is typically padded such that it
> winds up 8 byte aligned whereas on a 32bit architecture structs are usually
> padded to be 4 byte aligned. If you are passing data between these two
> architectures with the same struct definition and things are unpacked, the two
> structures would not be equivalent! To pack individual structures, you can use
> the "packed" attribute. It's still a good idea to naturally align the members
> within a struct when possible for minimal code size usage and performance; see
> [above](#-wpadded) for information on struct padding!
