---
id: "intr-the-best-and-worst-gcc-compiler-fl-wformat-2-wformat-truncation"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -Wformat=2 & -Wformat-truncatio"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#wformat-2-wformat-truncation"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

By default, `-Wall` enables `-Wformat` which turns on a variety of checks to make sure any formatter
strings used in standard library routines (i.e `printf`, `sprintf`, etc) are valid. However,
there's a bunch of extra formatter checks that can only be enabled individually[^11].

One interesting option is upgrading the `-Wformat` check level to 2 which includes a couple additional
checks such as `-Wformat-security`. Let's take a look at an example where a string to print is
passed but no sanitization on the string is performed.

```c
void print_user_provided_buffer(char *buf) {
  printf(buf);
}
```

```bash
$ EXTRA_CFLAGS="-Wformat" make
# No issues identified

$ EXTRA_CFLAGS="-Wformat=2" make
main.c: In function 'print_user_provided_buffer':
main.c:78:3: warning: format not a string literal and no format arguments [-Wformat-security]
   printf(buf);
```

> NOTE: A pretty slick feature with GCC is being able to enable format
> checks for custom functions[^12]. This is accomplished using the format attribute:
>
> ```c
> int my_printf (void *a, const char *fmt, ...)
>     __attribute__ ((format (printf, 2, 3)));
> ```

Another interesting set of formatter warning flags not enabled by default is `-Wformat-overflow` and
`-Wformat-truncation`. The options are able to detect various types of buffer overflows and
truncation that could arise when using routines such as `sprintf` and `snprintf` respectively:

```c
void snprintf_truncation_example(int val) {
  char buf[4];
  snprintf(buf, sizeof(buf), "%d", val);
}
```

```bash
$ EXTRA_CFLAGS="-Wformat-truncation=2" make
main.c: In function 'snprintf_truncation_example':
main.c:87:31: warning: '%d' directive output may be truncated writing between 1 and 11 bytes into a region of size 4 [-Wformat-truncation=]
   snprintf(buf, sizeof(buf), "%d", val);
                               ^~
main.c:87:3: note: 'snprintf' output between 2 and 12 bytes into a destination of size 4
  snprintf(buf, sizeof(buf), "%d", val);
```
