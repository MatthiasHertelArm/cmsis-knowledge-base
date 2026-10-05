---
id: "intr-the-best-and-worst-gcc-compiler-fl-wundef"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -Wundef"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#wundef"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

A classic bug encountered in C code is an undefined macro silently evaluating as 0 and causing
unexpected behavior. For example, consider a define used in a codebase, `ACCEL_ENABLED`, which controls whether or not the accelerometer code responsible for step tracking is initialized.

There are several bugs that can pretty easily go unnoticed:

- A file references `ACCEL_ENABLED` but doesn't pick up the appropriate configuration header where the macro is defined so the accelerometer related code in the file gets compiled out.
- The correct configuration header is sourced but a programmer mistypes the name of the macro (i.e `ACCEL_ENABLE` instead of `ACCEL_ENABLED`) and so the code also gets compiled out.

These classes of errors can _easily_ be identified by using the `-Wundef` flag:

```c
#if ACCEL_ENABLED
//
// accelerometer configuration code
//
#endif /* ACCEL_ENABLED */
```

```bash
$ EXTRA_CFLAGS=-Wundef make
main.c:13:5: warning: "ACCEL_ENABLED" is not defined, evaluates to 0 [-Wundef]
#if ACCEL_ENABLED
```

Note that this type of check is _not_ possible when the check is preceded by the ifdef
(anti-)pattern check:

```c
#if defined(ACCEL_ENABLED) && ACCEL_ENABLE
// typo "ACCEL_ENABLE" (instead of ACCEL_ENABLED) will go unnoticed
#endif
```

In general, it's advisable to use `#ifdef` sparingly in a project for these reasons.
