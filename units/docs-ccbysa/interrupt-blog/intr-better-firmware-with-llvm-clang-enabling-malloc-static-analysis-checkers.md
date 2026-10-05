---
id: "intr-better-firmware-with-llvm-clang-enabling-malloc-static-analysis-checkers"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Static Analysis With Clang and scan-build / Enabling \"Malloc\" Static Analysis Checkers"
summary: "Part of: Static Analysis With Clang and scan-build"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#enabling-malloc-static-analysis-checkers"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Static Analysis With Clang and scan-build_

`scan-build` also includes a sophisticated suite of dynamic memory checkers to catch bugs such as
memory leaks, use-after-free and double free errors (These are mostly run as part of the `unix.Malloc` checker). If you use the C standard library calls (i.e
`calloc`, `malloc`, `free`, etc) in your embedded project, these checks will work out of the box.

However, for many embedded projects this is not the case. It's typical to have a heap (or "byte
pool") per subsystem (i.e network stack, graphics, sensor data, etc). This can help prevent
one subsystem from taking down the other. In other embedded systems, RAM speed may not be heterogeneous, and it may
be desirable to partition RAM into pools by access speed. This way subsystems requiring the
fastest RAM (i.e graphics) can use one heap and subsystems which do not care can use slower RAM.

Conveniently, you can use compiler attributes to flag functions that behave like "malloc" and enable the
`unix.Malloc` checkers on them. Let's set this up for the `memory_pool.h` file in our example project:

```c
#pragma once
//! @file memory_pool.h

#include <stddef.h>

void *memory_pool_allocate(size_t size);
void memory_pool_free(void *ptr);
```

#### Attributes For Malloc Checking on Custom Functions

In our `compiler.h` header we will add the following:

```c
#if defined(__clang__)

#define EXAMPLE_PROJ_MALLOC_LIKE_FUNC \
  __attribute__((ownership_returns(malloc)))

//! Note: Second Argument is the argument index for
//! the pointer being free'd. For simplicity, let's assume
//! the pointer is always in the 1st argument
#define EXAMPLE_PROJ_FREE_LIKE_FUNC \
__attribute__((ownership_takes(malloc, 1)))

#else

#define EXAMPLE_PROJ_MALLOC_LIKE_FUNC
#define EXAMPLE_PROJ_FREE_LIKE_FUNC

#endif
```

##### Aside: Prefix Project Macros!

Due to the C language's lack of namespacing, it's a good idea to prefix your macros to avoid collisions with
other libraries. (i.e `MY_PROJECT_MIN()` instead of `MIN()`).

This helps avoid define collisions with poorly structured libraries and prevents the use of the
`#ifndef`-`#define`-`#endif` anti-pattern:

```c
#ifndef MIN
#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#endif
```

#### Instrument Custom Malloc Implementation

We'll update `memory_pool.h` to use the attributes defined above and apply one small workaround so the checker
works with our custom functions:

```c
#pragma once
//! @file memory_pool.h

#include <stddef.h>

EXAMPLE_PROJ_MALLOC_LIKE_FUNC
void *memory_pool_allocate(size_t size);

//! As of LLVM 10, the "unix.MismatchedDeallocator" expects
//! memory to always be released with free() and will emit
//! the following error if not:
//!
//! "warning: Memory allocated by my_malloc_func(), should be
//! deallocated by free(), not my_free_func()"
//!
//! To circumvent the error for now we remap our custom free
//! function to free() when scan-build is running. Hopefully, future
//! releases of Clang make it possible to change this rule via annotations.
#ifdef __clang_analyzer__
#define memory_pool_free free
#endif

EXAMPLE_PROJ_FREE_LIKE_FUNC
void memory_pool_free(void *ptr);
```

Let's try it out on a few examples:

```c
uint32_t example_access_garbage(void) {
  const size_t size = 10;
  uint8_t *ptr = memory_pool_allocate(size);
  if (ptr == NULL) {
    return 0;
  }

  // access the data before setting it
  uint32_t sum = 0;
  for (size_t i = 0; i < size; i++) {
    sum += ptr[i];
  }

  return sum;
}
```

```
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ scan-build make
[...]
src/memory_leak_examples.c:31:9:
  warning: Assigned value is garbage or undefined
    sum += ptr[i];
```

```c
uint32_t example_memory_leak(void) {
  const size_t size = 10;
  uint8_t *ptr = memory_pool_allocate(size);
  if (ptr == NULL) {
    return 0;
  }

  // ... do something with the pointer ...
  const uint8_t return_code = ((uint32_t)(uintptr_t)ptr) ? 0xa5 : 0xef;
  if (return_code == 0xa5) {
    return 1;
  }

  memory_pool_free(ptr);
  return 0;
}
```

```
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ scan-build make
[...]
src/memory_leak_examples.c:47:12:
  warning: Potential leak of memory pointed to by 'ptr'
    return 1;
```
