---
id: "intr-using-asserts-in-embedded-systems-standard-library-assert-1"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / Standard Library Assert (#1)"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#standard-library-assert-1"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

The initial approach is to use what already exists within the standard library,
`assert(expr)`. This requires us to implement the function `__assert_func`.

```c

void __assert_func(const char *file,
                   int line,
                   const char *func,
                   const char *failedexpr) {
  snprintf(g_assert_info.msg, sizeof(g_assert_info.msg),
           "ASSERT: %s at %s\n", failedexpr, func);
  strncpy(g_assert_info.file, file, sizeof(g_assert_info.file));
  g_assert_info.line = line;

  __asm("bkpt 1");
}

void assert_path_A(void) {
  assert(0);
}
```

With the `stdlib.h` implementation of `assert.h`, the filepath, line number,
function name, and the actual expression being tested are **all** passed into
the assert handler.

If code space is of any concern to you, I would advise never to use this
approach.
