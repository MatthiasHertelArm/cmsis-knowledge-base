---
id: "intr-considerations-when-building-embed-aside-portability-of-records"
type: "concept"
domain: "debug"
title: "Considerations when Building Embedded Databases: Aside: Portability of Records"
summary: "Thinking ahead, you may eventually wish to run your fishtank code on different hardware either because of an upgrade to the product, a new version of the product, or because you want to be able to load up …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-24-choosing-or-building-an-embedded-db.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#aside-portability-of-records"
license: "CC-BY-SA-4.0"
mode: "V"
---

Thinking ahead, you may eventually wish to run your fishtank code on different
hardware either because of an upgrade to the product, a new version of the
product, or because you want to be able to load up records from the embedded
system inside a mobile app or a server.

That new processor may be 64-bit processor, or may even use a different
endianness than the microcontroller. Taking a closer look at the
`fishtank_config_t` struct, we see that the basic `int` type is used, which uses
4 bytes on 32-bit chips, but might use 16- or 8- bits on other architectures,
and the endianness (byte order) depends on the processor.

### Integer Size and Alignment

With the definition of `fishtank_config_t` above, `sizeof(fishtank_config_t)`
will be different for different platforms. Compiling on a 64-bit MacBook where
Apple kept `int` as 32-bit with 32-bit alignment, you'll get the same 8-byte
structure as on a 32-bit microcontroller. However, if you compile on an AWS EC2
instance (as you may want to do if there is a cloud component to your fishtank),
then you get a 16-byte structure because `int` there is 8 bytes.

For portability, use the fixed-width definitions in `stdint.h` and instruct the
compiler to pack your structure to remove any padding which would otherwise be
added to encourage alignment to word boundaries:

```c
#pragma pack(push, 1)
typedef struct {
    int32_t salinity;
    int32_t oxygen;
} fishtank_config_t;
#pragma pack(pop)
```

### Much Ado About Endianness

There's one remaining portability issue. There have historically been
"big-endian" processors which represent multi-byte integers with the
most-significant byte first rather than least-significant byte first (so-called
"little endian") which has become the dominant endianness today. This means that
even with the fixed-sized, packed structure above, there may be processors where
a record with `salinity == 2` is interpreted as `33554432` because of the endian
mismatch.

If this sounds confusing, that's because it is. Even when working in a systems
language such as C, we get used to the convenient abstraction of "an integer"
without worrying about how it is laid out in memory. So let's take a look at how
the a 32-bit unsigned integer with the hexadecimal value `0xDEADBEEF` is stored
in memory using either endianness convention:

| endianness    | byte 0 | byte 1 | byte 2 | byte 3 |
| ------------- | ------ | ------ | ------ | ------ |
| little-endian | 0xEF   | 0xBE   | 0xAD   | 0xDE   |
| big-endian    | 0xDE   | 0xAD   | 0xBE   | 0xEF   |

You can see that on little-endian systems, the least significant byte (`0xEF`)
comes in the first memory location, as opposed to big-endian which starts with
the most significant byte (`0xDE`). Now it should be clear that if the same byte
buffer is loaded into a big-endian and a little-endian system, they will be
interpreted as very different integers.

At Bond, we initially took pains to build `hton` (host-to-network) functions for
every structure which would enforce big-endian integer representations, in
keeping with the tradition of TCP/IP networking and numerous file formats.
However, maintaining those `hton` functions is highly error-prone and it is easy
to end up with records that have some of their multi-byte fields in "network
byte order" while others remain in the native byte order. What a mess!

What we learned is that, unless you need to support some very exotic big-endian
architecture, you're better off ignoring endianness and just letting all your
structs be little-endian. This greatly simplifies maintainability, reduces
confusion for developers unfamiliar with byte-order, saves CPU time, and allows
working with constant record data without RAM copies to reverse the byte order
before write to flash.
