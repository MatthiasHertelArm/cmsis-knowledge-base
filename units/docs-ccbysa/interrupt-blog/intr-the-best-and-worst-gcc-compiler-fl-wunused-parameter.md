---
id: "intr-the-best-and-worst-gcc-compiler-fl-wunused-parameter"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Worst / -Wunused-parameter"
summary: "This warning will detect when a parameter passed to a function is never used in the function."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#wunused-parameter"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Worst_

This warning will detect when a parameter passed to a function is never used in the
function. While the goal here is to detect functions with dead parameters, as you start to build
abstractions, sometimes parameters simply won't be used by all the implementations and
the code ends up cluttered by the tricks you will need to mark those parameters as used:

```c
#define MEMFAULT_UNUSED(_x) (void)(_x)
```

Let's take a look at an example:

```c
typedef void (*FlashReadDoneCallback)(void *ctx);

static void prv_spi_flash_read_cb(void *ctx) {
  // nothing to do with ctx so we'll have to add a MEMFAULT_UNUSED here to prevent the warning
  MEMFAULT_UNUSED(ctx);
}

int flash_read(FlashReadDoneCallback cb, void *ctx) {
  // perform flash read
  // [...]
  // invoke callback
  cb(ctx);
}
```

More often then not, the usage of this flag just result in an excessive amount of
`(void)(variable)` calls getting litered in a codebase rather than helping to catch any real issues.

{:.no_toc}
