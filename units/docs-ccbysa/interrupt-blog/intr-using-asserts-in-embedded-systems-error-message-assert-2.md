---
id: "intr-using-asserts-in-embedded-systems-error-message-assert-2"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / Error Message Assert (#2)"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#error-message-assert-2"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

The next simplest approach is to pass in a unique string to the assert which
provides context for the developer about what the error was and where. We can
then search for this error message within the codebase and figure out at which
location the assert took place at.

```c
#define MY_ASSERT(expr, msg) \
  do {                                          \
    if (!(expr)) {                              \
      my_assert(msg);                           \
    }                                           \
  } while (0)
```

```c
void my_assert(const char *msg) {
  strncpy(g_assert_info.msg, msg, sizeof(g_assert_info.msg));
  __asm("bkpt 2");
}

void assert_path_A(void) {
  MY_ASSERT(0, "Assert in `assert2.c::assert_path_A`");
}
```

The drawback of this method is that every message is stored in the resulting
binary, and this takes up precious code space.

Below, we use `objdump` to view the resulting strings in the binary. We can see
that each assert string takes up ~32 bytes.

```
$ arm-none-eabi-objdump -s -j '.text' build/nrf52.elf
 ...
 2710 63000000 41737365 72742069 6e206061  c...Assert in `a
 2720 73736572 74322e63 3a3a7477 6f5f7472  ssert2.c::two_tr
 2730 75650000 41737365 72742069 6e206061  ue..Assert in `a
 2740 73736572 74322e63 3a3a7477 6f5f6661  ssert2.c::two_fa
 2750 6c736500                             lse.
```

The longer the string, the more codespace that is used, so this would actually
**discourage** the use of asserts, which is not ideal.

#### Extracted Information

We can look up the file and line number of the assert hit assuming all assert
strings are unique.
