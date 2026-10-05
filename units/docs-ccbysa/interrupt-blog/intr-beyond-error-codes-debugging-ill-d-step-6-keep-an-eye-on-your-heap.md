---
id: "intr-beyond-error-codes-debugging-ill-d-step-6-keep-an-eye-on-your-heap"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 6 - Keep an Eye on Your Heap"
summary: "Do you use dynamic memory allocation (think malloc(), calloc(), realloc()) in your application? If you answered no, are you sure?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-6-keep-an-eye-on-your-heap"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

Do you use dynamic memory allocation (think `malloc()`, `calloc()`, `realloc()`)
in your application? If you answered no, are you sure? Generally speaking, to
even use any memory allocation functions (which are provided in the standard
library) a "system call" function `_sbrk_r` must be defined. For convenience,
many "code generation" style vendor tools will generate a default implementation
of `_sbrk_r` for you, as well as linker scripts and symbols that locate your
stack and heap. There are also a host of functions in the C and C++ standard
libraries that (implementation dependent) end up allocating memory under the
hood (`printf()`, `sprintf()`, `std::string`, `std::Vector` to name only a few).
The combination of these two leads many people (myself included at one point!)
to have dynamic memory allocation in their program under the hood without them
even realizing it. When starting a new project, I like to start by defining
`_sbrk_r` with a placeholder like so to ensure any memory allocation I wasn't
expecting makes itself known:

```c
char *_sbrk_r(int incr)
{
  log("Not so fast!");
  asm volatile ("bkpt #0");
  while(1) {};
  // Unreachable
  return NULL;
}
```

Dynamic memory allocation isn't inherently a bad thing, however, it opens up the
door for an entirely different class of errors. The
[following article](https://docs.oracle.com/cd/E60778_01/html/E60757/glmrb.html)
from Oracle does a fairly good job at succinctly summing up some of the errors
you could expect when using dynamic memory allocation.

There's another error worth mentioning when the heap gets involved that is
pretty specific to bare metal systems like the ones we work with. Oftentimes,
the heap and stack on a bare metal system are configured like so:

(figure: RAM layout)

The stack grows _downward_ in address space, while the heap grows _upwards._
Like two trains rushing towards each other on the same track, one getting large
enough will _eventually_ start to clobber the other. This produces behavior very
similar to a stack overflow. Fortunately, because any heap expansion is called
explicitly in code, checks can and should be implemented to trigger an error
condition if the heap is about to grow beyond its bounds. Some RTOSes even
include their own heap management schemes, such as
[FreeRTOS](https://www.freertos.org/Documentation/02-Kernel/02-Kernel-features/09-Memory-management/01-Memory-management)
and
[Zephyr](https://docs.zephyrproject.org/latest/kernel/memory_management/heap.html).
Similar to stack inspection, stopping the program with a debugger and taking a
look at the state of your heap (and the variables that have been allocated
within it) before the offending portion of code can sometimes yield insights
into potential memory corruption issues.

Having vetted the stack and the heap, it's time to step down a level and get a
little closer to the MCU itself.
