---
id: "intr-c-structure-padding-initialization-best-practice"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization: Best Practice?"
summary: "It's tricky to recommend a one-size-fits-all option here, because different software will have different constraints. However, some general purpose advice follows."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization#best-practice"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's tricky to recommend a one-size-fits-all option here, because different
software will have different constraints. However, some general purpose advice
follows.

### Avoid relying on structure layout

The simplest option to avoid padding issues is to avoid the padding fields
altogether:

> Access data directly via each member, do not alias structures or use `memcmp`
> etc.

This only works if the padding data can be safely ignored in all use cases for
the data structures in question.

_Note however that packed structs can be safely `memcmp`'d, see below_

Another approach is to avoid structure holes entirely!

For example, you can use the `-Wpadded` compiler warning in
[GCC](https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#index-Wpadded) and
[Clang](https://releases.llvm.org/15.0.0/tools/clang/docs/DiagnosticsReference.html#wpadded) to detect
padding, and with `-Werror` or `-Werror=padded`, you can trigger compilation
errors if padding is detected. To address the warnings, you can add placeholders
to fill unused space:

```c
struct foo {
  uint32_t i;
  uint8_t b;
  uint8_t padding_[3];
};
```

(Note that GCC will emit a warning on _declaration_, where Clang will only warn
when the violating struct is actually used in a definition. Similar, but subtly
different as usual 🌈).

Alternatively, the `pahole` tool could be used to detect any structures with
padding bits (for example, as a linter pass on the generated binary), and they
can be corrected by either reordering structure members to eliminate padding, or
adding `uint8_t padding_[n]` fields to explicitly address the holes. See also
[The Lost Art of Structure Packing](http://www.catb.org/esr/structure-packing/)
linked previously.

It's generally preferable to strive for padding to only be present at end of
struct.

### Use `memset` to zero-initialize padding bits

`memset` reliably sets the entire memory space of an object, including the
padding bits.

Must be manually done, though, so can be error-prone.

Be sure to set the size argument directly from the object in question:

```c
// error prone! if the type of 'a' changes, we might get unexpected results
memset(&a, 0, sizeof(struct foo));

// much better
memset(&a, 0, sizeof(a));
```

### Last resort, `__attribute__((packed))`

This will eliminate structure padding, but there can be considerable compute
overhead (and with code doing unusual type aliasing, you may find yourself in an
Unaligned Access fault 😓).

On the plus side, the structure fields should have easily predictable offsets in
memory, for example if it needs to be serialized out.

Additionally, packed structs can be safely `memcmp`'d, since there are no
"ghost" bits hiding in between explicitly allocated members 👻
