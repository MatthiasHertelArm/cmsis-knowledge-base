---
id: "intr-using-asserts-in-embedded-systems-register-values-only-assert-5"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / Register Values Only Assert (#5)"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#register-values-only-assert-5"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

The problem with all of the above assert implementations is that our code size
is bloated due to storing string filenames, and also that our code size can
change depending on how we name the files in our project. This encourages poor
naming practices, as well as produces unexpected build sizes.

My favorite way to implement asserts is to record both the program counter and
the link register within the macro. This provides the following benefits:

- Each assert consumes a fixed number of bytes, no matter the filepath,
  filename, or number of asserts per file.
- By capturing both the PC and LR, we can get an extra frame in our 'backtrace'.
- If we really wanted to micro-optimize, we can choose not to record the LR and
  save a couple more bytes.

Below we define two macros, `GET_LR()` and `GET_PC()`, to retrieve the registers
`pc` and `lr` respectively.

```c
#define GET_LR() __builtin_return_address(0)
// This is ARM and GCC specific syntax
#define GET_PC(_a) __asm volatile ("mov %0, pc" : "=r" (_a))

#define MY_ASSERT_RECORD()     \
  do {                         \
    void *pc;                  \
    GET_PC(pc);                \
    const void *lr = GET_LR(); \
    my_assert(pc, lr);         \
  } while (0)

#define MY_ASSERT(exp)         \
  do {                         \
    if (!(exp)) {              \
      MY_ASSERT_RECORD();      \
    }                          \
  } while (0)
```

In our `my_assert` implementation, we then record the two register values in our
struct. Since we aren't storing the file or line number information directly in
our firmware, we can also save RAM and flash space. This could allow us to store
many more asserts in our logs!

```c
void my_assert(uint32_t *pc, uint32_t *lr) {
  // File and line deliberately left empty
  g_assert_info.pc = (uint32_t)pc;
  g_assert_info.lr = (uint32_t)lr;
  __asm("bkpt 5");
}
```

The drawback to this approach is that we'll have to use `addr2line` or a similar
tool to go from our register values to the file and line information, but this
can be added to a simple script and used by the entire team with ease.

```
$ arm-elf-linux-addr2line --exe build/nrf52.elf 0x2250
/Users/tyler/dev/memfault/interrupt/example/debugging-asserts/impls/assert5.c:13
```

> NOTE: Compiler optimizations such as function inlining may result in different
> asserts being merged together, which will produce confusing results. One way
> to mitigate this is to also pass in the `__LINE__` information to the assert
> to make every `my_assert` call unique.

#### Extracted Information

We can use `addr2line` on both the PC and LR to find the file and line number of
the assert hit, as well as **caller's** file and line number.
