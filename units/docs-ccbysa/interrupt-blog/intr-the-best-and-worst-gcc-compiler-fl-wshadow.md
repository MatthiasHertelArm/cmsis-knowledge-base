---
id: "intr-the-best-and-worst-gcc-compiler-fl-wshadow"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -Wshadow"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#wshadow"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

Shadowing variables at the very least makes code difficult to read and often can be indicative of a
bug because the code is not operating on the value the programmer expects. These can easily be
detected by using `-Wshadow`.

```c
int variable_shadow_error_example2(void) {
  int result = 4;

  for (int i = 0; i < 10; i++) {
    int result = i;
    // do something with result
  }

  return result;
}
```

```bash
$ EXTRA_CFLAGS=-Wshadow make
main.c: In function 'variable_shadow_error_example2':
main.c:55:9: warning: declaration of 'result' shadows a previous local [-Wshadow]
     int result = i;
         ^~~~~~
main.c:52:7: note: shadowed declaration is here
   int result = 4;
```
