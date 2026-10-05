---
id: "intr-c-structure-padding-initialization-c-structure-padding"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: C Structure Padding"
summary: "Recently I was reading this excellent post on some of the upcoming features in C23, and it inspired me to do a little exploration and documentation around the current state of initialization of padding in structures in the C-language."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#c-structure-padding"
license: "CC-BY-SA-4.0"
mode: "V"
---

Recently I was reading this
[_excellent_ post](https://thephd.dev/ever-closer-c23-improvements#consistent-warningless-and-intuitive-initialization-with--)
on some of the upcoming features in C23, and it inspired me to do a little
exploration and documentation around the current state of initialization of
padding in structures in the C-language.

For background, let's take this example C structure:

```c
#include <stdint.h>

struct foo {
  uint32_t i;
  uint8_t b;
};
```

By default, padding will be inserted at the end of this structure, to align it
to the largest member size. We can use the
[`pahole`](https://linux.die.net/man/1/pahole) tool to examine structure holes
after compiling (with debug symbols enabled, `-g`):

```c
struct foo {
        uint32_t                   i;                    /*     0     4 */
        uint8_t                    b;                    /*     4     1 */

        /* size: 8, cachelines: 1, members: 2 */
        /* padding: 3 */
        /* last cacheline: 8 bytes */
};
```

My understanding is this is done so if the structure is addressed as part of an
array, the first member of each element in the array will have the same
alignment:

```c
struct foo foo_array[2];
// if &foo_array[0] has 4 byte alignment, we want &foo_array[1]
// to also have 4 byte alignment. This is because on most architectures it is more efficient to access data along boundaries aligned with their size.
```

The other (more commonly encountered) case is where padding is inserted between
structure members:

```c
struct foo_internal_padding {
  uint8_t b;
  uint32_t i;
};
```

Running `pahole` as above shows the padding inserted after the first element:

```c
struct foo {
        uint8_t                    b;                    /*     0     1 */

        /* XXX 3 bytes hole, try to pack */

        uint32_t                   i;                    /*     4     4 */

        /* size: 8, cachelines: 1, members: 2 */
        /* sum members: 5, holes: 1, sum holes: 3 */
        /* last cacheline: 8 bytes */
};
```

> Note! the _excellent_ guide here (which we've linked before), is a great
> reference on structure padding and artisanal hand-packing:
> <http://www.catb.org/esr/structure-packing/>

Of course, to prevent padding, we can force the compiler to pack the structure:

```c
struct __attribute__((packed)) foo {
  uint8_t b;
  uint32_t i;
};
```

Now we have no padding inside the structure:

```c
struct foo {
        uint8_t                    b;                    /*     0     1 */
        uint32_t                   i;                    /*     1     4 */

        /* size: 5, cachelines: 1, members: 2 */
        /* last cacheline: 5 bytes */
} __attribute__((__packed__));
```

Similarly, a structure that would normally have padding at the end will no
longer have it:

```c
struct foo {
        uint32_t                   i;                    /*     0     4 */
        uint8_t                    b;                    /*     4     1 */

        /* size: 5, cachelines: 1, members: 2 */
        /* last cacheline: 5 bytes */
} __attribute__((__packed__));
```

_Note that accessing members of compiler-packed structs often can add compute
overhead; the CPU may need to do bytewise loads and stores depending on
alignment requirements of the architecture._

For completeness, note that arrays of packed structures by default will also be
packed (no trailing padding inserted between array elements; example
[here](https://godbolt.org/z/hhzf9zW4E)). Usually the compiler will do the
correct thing, but you might run into unexpected cases when type aliasing (this
is undefined behavior anyway, and there be dragons here 🐉!).

**Bitfields** follow similar rules when it comes to packing, with the added
complexity where the type holding the bitfield is undefined, with this somewhat
horrifying language in the C11 specification §6.7.2.1/11:

> An implementation may allocate any addressable storage unit large enough to
> hold a bit-field. If enough space remains, a bit-field that immediately
> follows another bit-field in a structure shall be packed into adjacent bits of
> the same unit. If insufficient space remains, whether a bit-field that does
> not fit is put into the next unit or overlaps adjacent units is
> implementation-defined. The order of allocation of bit-fields within a unit
> (high-order to low-order or low-order to high-order) is
> implementation-defined. The alignment of the addressable storage unit is
> unspecified.

As Mitch Johnson over at theinterrupt.slack.com pointed out, there are other
subtleties to consider with bitfields that can have architecture-specific
implications:

> ... some architectures (ARM in particular) require compilers to represent
> volatile bitfield layout and accesses in a well-defined fashion in order to
> comply with their procedure call standard. This allows use of volatile
> bitfields to properly represent access to memory-mapped peripherals.
> https://developer.arm.com/documentation/ihi0042/j/?lang=en This can still be
> fraught with danger. GCC's had a number of bugs around volatile bitfield
> usage, and ARM's own clang derivative has had varyingly non-compliant behavior
> over time: https://developer.arm.com/documentation/ka004594/latest
