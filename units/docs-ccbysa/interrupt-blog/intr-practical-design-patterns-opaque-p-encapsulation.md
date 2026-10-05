---
id: "intr-practical-design-patterns-opaque-p-encapsulation"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C: Encapsulation"
summary: "Because the pointer is opaque, the user's calling code cannot access the data inside the struct. Why is this a good thing?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers#encapsulation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Because the pointer is opaque, the user's calling code cannot access the data inside the struct.
Why is this a good thing?

* It simplifies the API. The user does not need to know or care about internal data.
* The struct definition can change without impacting any of the using code.
* It prevents misuse of internal struct data.

On the topic of misuse, imagine if the user could see inside the opaque pointer. They might think
they're clever enough to manipulate read and write pointers in the ringbuffer themselves, to get some
kind of custom behavior they're looking for, but most likely, they will end up shooting themselves in
the foot (maybe they forgot to account for wraparound).
Furthermore, it creates hidden coupling in the system. If the ringbuffer implementation
changes the way it uses read and write pointers, it will need to visit all the using code that
accesses the pointers as well. In effect, the ringbuffer implementation would be spread out across
multiple files in the system (good luck finding them all!) instead of being isolated to one file.

By defining the struct in `ringbuffer.c`, the data is "private" to that file
(or more precisely, the
[translation unit](https://en.wikipedia.org/wiki/Translation_unit_(programming))).

What if you have a large module, spread over many `.c` files, that all need
access to the struct? In that case, a good option is to define the struct inside of
a private header file - `ringbuffer_private.h` in the example - which you
can `#include` in other module files. This keeps the public interface in
`ringbuffer.h` clean and minimal, and gives internal module files access to the
private struct data.
