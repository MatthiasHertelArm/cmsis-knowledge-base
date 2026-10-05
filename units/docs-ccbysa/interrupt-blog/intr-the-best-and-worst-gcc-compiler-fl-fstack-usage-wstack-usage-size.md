---
id: "intr-the-best-and-worst-gcc-compiler-fl-fstack-usage-wstack-usage-size"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best One-Off Warning Options (options not covered by -Wall or -Wextra) / -fstack-usage & -Wstack-usage=`"
summary: "Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#fstack-usage-wstack-usage-size"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: The Best One-Off Warning Options (options not covered by -Wall or -Wextra)_

For embedded development, there is often not a lot of RAM available to allocate for stack space
(typically on the order of a few hundred to a few thousand bytes). Therefore, stack overflows can
be very common especially if the programmer is not careful about what local variables they put on
the stack.

There's a useful pair of flags which can be used to monitor stack space in a function and emit warnings when the usage is too high.

To generate stack depth information, you need to use the `-fstack-usage` flag which will emit `.su`
files for each c file you compile. Tools like Puncover[^4] will even analyze the stack space
information emitted and generate maximal stack depth estimations based on call path.

Let's compile the following and inspect the `.su` file which is output:

```c
#include <stdint.h>

int stack_usage_example(int num) {
  uint8_t tmp[256];
  [... operations on tmp ...]
}

int vla_stack_usage(int num) {
  if (num <= 0) {
    return -1;
  }

  uint8_t tmp[num];
  [... operations on tmp ...]
}
```

The `.su` file will look like:

```bash
$ EXTRA_CFLAGS=-fstack-usage make
$ cat stack_usage.su
stack_usage.c:3:5:stack_usage_example	256	static
stack_usage.c:14:5:vla_stack_usage	16	dynamic
```

We will see the stack usage of the function in bytes followed by `static` if the usage is fixed or `dynamic` if the
entire stack usage cannot be computed at compilation time because a variable length array (VLA) was
used.

`-Wstack-usage=<stack_limit>` can also be leveraged to emit a warning when stack usage exceeds a
certain value. Let's try it out!

```bash
$ EXTRA_CFLAGS=" -Wstack-usage=255" make
stack_usage.c: In function 'stack_usage_example':
stack_usage.c:3:5: warning: stack usage is 256 bytes [-Wstack-usage=]
 int stack_usage_example(int num) {
     ^~~~~~~~~~~~~~~~~~~
stack_usage.c: In function 'vla_stack_usage':
stack_usage.c:14:5: warning: stack usage might be unbounded [-Wstack-usage=]
 int vla_stack_usage(int num) {
```
