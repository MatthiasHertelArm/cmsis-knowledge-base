---
id: "intr-using-asserts-in-embedded-systems-file-name-and-line-number-assert-4"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / File**name** and Line Number Assert (#4)"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#file-name-and-line-number-assert-4"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

Since the filepaths can be lengthy and waste code space, one solution is to use
only the filename itself, e.g. `assert3.c`, instead of the filepath, e.g.
`/Users/tyler/.../assert3.c`.

This can be accomplished by adding a define called `__FILENAME__` and using this
in the assert implementation instead. In the Makefile or similar build system,
this macro is defined in line with the compilation rule.

```
$(BUILD_DIR)/%.o: $(ROOT_DIR)/%.c | $(BUILD_DIR) $(DEP_DIR) $(FREERTOS_PORT_ROOT)
  ...
  $(Q) arm-none-eabi-gcc $(DEP_CFLAGS) $(CFLAGS) $(INCLUDE_PATHS) \
      -D__FILENAME__=\"$(notdir $<)\" \
      -c -o $@ $<
```

In the assert header, we can now use `__FILENAME__` instead of `__FILE__`.

```c
#define MY_ASSERT(expr)                   \
  do {                                    \
    if (!(expr)) {                        \
      my_assert(__FILENAME__, __LINE__);  \
    }                                     \
  } while (0)
```

With this change, we reduce our file string from
`/Users/tyler/dev/memfault/interrupt/example/debugging-asserts/impls/assert3.c`
to `assert3.c`, resulting in 68 bytes of code space savings per file which
contains an assert.

```
$ arm-none-eabi-objdump -s -j '.text' build/nrf52.elf
 ...
26b0 61737365 7274342e 6300               assert4.c
```

#### Extracted Information

We know the file and line number of the assert hit.
