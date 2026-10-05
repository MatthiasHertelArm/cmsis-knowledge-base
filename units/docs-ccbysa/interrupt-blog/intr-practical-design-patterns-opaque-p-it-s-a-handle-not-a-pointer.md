---
id: "intr-practical-design-patterns-opaque-p-it-s-a-handle-not-a-pointer"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C: It's a Handle, Not a Pointer"
summary: "The opaque pointer typedef is such that it hides the fact that it's a pointer:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers#it-s-a-handle-not-a-pointer"
license: "CC-BY-SA-4.0"
mode: "V"
---

The opaque pointer typedef is such that it hides the fact that it's a pointer:

```c
typedef struct ringbuffer_instance_t* ringbuffer_t;
```

It's an abstract representation of the instance, often referred to as a
[handle](https://en.wikipedia.org/wiki/Handle_(computing)).

We could just as easily define the handle as a `uint32_t` (maybe it's an index
into an array), and none of the using code would change:

```c
typedef uint32_t ringbuffer_t;
```

Once created, the handle is passed in *by value* to each function.
At the call site, a variable of type `ringbuffer_t` almost looks like a
normal value, like a number:

```c
ringbuffer_t rbuf = ringbuffer_create(10);
ringbuffer_enqueue(rbuf, 0xA5);
```

Using a non-pointer handle type is a stylistic choice, but I think it makes the API easier
to use. When it looks like a normal value, users don't have to use the `*` or `&`
operators. Conversely, if the user sees an API that deals with pointers, there is a small
bit of cognitive overhead and anxiety (questions of ownership, calling mechanics).
