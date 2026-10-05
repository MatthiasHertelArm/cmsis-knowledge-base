---
id: "intr-practical-design-patterns-opaque-p-object-life-cycle"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C: Object Life Cycle"
summary: "When you use this pattern, it's customary to declare create and destroy functions. These are analogous to constructors and destructors in OOP."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers#object-life-cycle"
license: "CC-BY-SA-4.0"
mode: "V"
---

When you use this pattern, it's customary to declare `*_create`
and `*_destroy` functions. These are analogous to constructors and destructors
in OOP.

The `*_create` function will perform allocation and initialization of an instance and return an
[opaque pointer](https://en.wikipedia.org/wiki/Opaque_pointer)
to the user, which represents the instance. It's really just a pointer to a struct,
but the user can't see what's in the struct. The user's calling code will fail to compile
if it tries to dereference the struct pointer because the struct is not defined in the header
(it is only declared).

Likewise, `*_destroy` will clean up
the instance, making it null-and-void for future use (it would be user error if they try
to use the instance after it's been destroyed).

After the user has created an instance, they call functions which take the instance as the first
parameter. This is analogous to class member functions in C++, which implicitly take a `this`
pointer as the first parameter.
