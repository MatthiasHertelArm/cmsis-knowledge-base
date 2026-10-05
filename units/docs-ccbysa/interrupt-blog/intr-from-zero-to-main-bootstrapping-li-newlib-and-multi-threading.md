---
id: "intr-from-zero-to-main-bootstrapping-li-newlib-and-multi-threading"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Implementing Newlib / Newlib and Multi-threading"
summary: "We have not yet talked much about multi-threading (e.g. with an RTOS) in this series, and going into details is outside of the scope of this article."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#newlib-and-multi-threading"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementing Newlib_

We have not yet talked much about multi-threading (e.g. with an RTOS) in this
series, and going into details is outside of the scope of this article. However,
there are a few things worth knowing when using Newlib in a multi-threaded
environment.

#### `_impure_ptr` and the `_reent` struct

Most Newlib functions are *reentrant*. This means that they can be called by
multiple processes safely.

For the functions that cannot be easily made re-entrant, newlib depends on the
operating system correctly setting the `_impure_ptr` variable whenever a context
switch occur. That variable is expected to hold a `struct _reent` for the
current thread. That struct is used to store state for standard library
functions being used by that thread.

#### Locking shared memory

Some standard library functions depend on global memory which would not make
sense to hold in the `_reent` struct. This is especially important when using
`malloc` to allocate memory out of the heap. If multiple threads try modifying
the heap at the same time, they risk corrupting it.

To allow multiple threads to call `malloc`, Newlib provides the `__malloc_lock`
and `__malloc_unlock` APIs[^1]. A good implementation of these APIs would lock
and unlock a recursive mutex.
