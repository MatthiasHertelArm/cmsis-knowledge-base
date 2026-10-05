---
id: "intr-using-asserts-in-embedded-systems-file-path-and-line-number-assert-3"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / File**path** and Line Number Assert (#3)"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#file-path-and-line-number-assert-3"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

The most common approach I've seen for asserts is to include the filepath and
line number into the assert macro, using the `__FILE__` and `__LINE__` defines
provided by the compiler.

```c
#define MY_ASSERT(expr) \
  do {                                          \
    if (!(expr)) {                              \
      my_assert(__FILE__, __LINE__);            \
    }                                           \
  } while (0)
```

```c
void my_assert(const char *file, uint32_t line) {
  strncpy(g_assert_info.file, file, sizeof(g_assert_info.file));
  g_assert_info.line = line;
  __asm("bkpt 3");
}

void assert_path_A(void) {
  MY_ASSERT(0);
}
```

This approach works very well and gives the developer exactly the amount of
context required to find the issue. However, the `__FILE__` macro includes the
**entire** filepath of the file, and those can get quite lengthy. In my local
build, `__FILE__` is 77 bytes!

```
(gdb) p __FILE__
$1 = "/Users/tyler/dev/memfault/interrupt/example/debugging-asserts/impls/assert3.c"
```

Thankfully, the `__FILE__` string table entry is reused between asserts in the
same file, so the code size bloat primarily depends on the number of files with
asserts within them. However, most projects have a non-trivial number of files.

As a rough estimate, if we have asserts in 50 different files, this results in
**~50 bytes per filepath \* 50 files => 2500 bytes**, which is an enormous
amount of bloat just for storing filepaths!

For this reason, many RTOS implementations that include an `ASSERT` macro can
optionally leave these strings out of the build, such as Zephyr[^8] and
MyNewt[^9].

> NOTE: One simple code size (and sanity) optimization is to normalize these
> `__FILE__` paths to the root of the project directory. This will result in a
> build path that removes the `/Users/tyler/dev/memfault/...` portion. An added
> benefit of this is that all all machines should produce builds with the same
> filepaths, resulting in more similarly sized builds.

#### Extracted Information

We know the file and line number of the assert hit.
