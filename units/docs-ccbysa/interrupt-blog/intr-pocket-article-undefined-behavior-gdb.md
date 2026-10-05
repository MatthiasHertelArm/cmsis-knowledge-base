---
id: "intr-pocket-article-undefined-behavior-gdb"
type: "concept"
domain: "debug"
title: "Pocket article: Undefined Behavior Sanitizer Trap on Error: `gdb`"
summary: "One particularly nice result of using the undefined trap- loading the executable from above into gdb (after recompiling with -Og and -ggdb3) and running it with the bad input will halt at the location of the undefined trap:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-06-22-ubsan-trap.md"
doc_source: "https://interrupt.memfault.com/blog/ubsan-trap#gdb"
license: "CC-BY-SA-4.0"
mode: "V"
---

One particularly nice result of using the undefined trap- loading the executable
from above into gdb (after recompiling with `-Og` and `-ggdb3`) and running it
with the bad input will halt at the location of the undefined trap:

```bash
❯ gcc -Og -ggdb3 -fsanitize=undefined -fsanitize-undefined-trap-on-error \
  ubsan-basic.c -o ubsan-basic-trap-on-error
❯ gdb -ex 'r' --args ubsan-basic-trap-on-error 2
```

[(figure: undefined behavior trap in GDB)](https://interrupt.memfault.com/img/ubsan-trap/ubsan-undefined-instruction-gdb.png)
