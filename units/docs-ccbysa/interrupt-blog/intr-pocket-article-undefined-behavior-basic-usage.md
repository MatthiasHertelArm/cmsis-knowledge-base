---
id: "intr-pocket-article-undefined-behavior-basic-usage"
type: "concept"
domain: "debug"
title: "Pocket article: Undefined Behavior Sanitizer Trap on Error: Basic Usage"
summary: "To enable UBSan, add this flag during compilation and linking:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-06-22-ubsan-trap.md"
doc_source: "https://interrupt.memfault.com/blog/ubsan-trap#basic-usage"
license: "CC-BY-SA-4.0"
mode: "V"
---

To enable UBSan, add this flag during compilation and linking:

`-fsanitize=undefined`

You may notice that enabling this flag increases the size of the compiled
program. This is due to the runtime checks inserted by the compiler, which also
will increase execution time. For this small example program, running the `size`
program shows a ~50% increase with `-fsanitize-undefined`!

```bash
❯ size ubsan-basic-noubsan ubsan-basic
   text    data     bss     dec     hex filename
   1894     616       8    2518     9d6 ubsan-basic-noubsan
   2874     944       8    3826     ef2 ubsan-basic
```

### Examples

Consider the small C program below:

```c
// ubsan-basic.c

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  (void)argc;

  const char *arr[] = {
      "0",
      "1",
  };

  // sketchy code below- argv may not have a second entry! could easily have an
  // out-of-bounds access in arr!
  int foo = atoi(argv[1]);
  printf("foo is %s\n", arr[foo]);

  return 0;
}
```

#### Without UBsan

Building that program normally:

```bash
❯ gcc ubsan-basic.c -o ubsan-basic
```

And running with problematic input:

```bash
❯ ./ubsan-basic 2
foo is
```

We get a weird result! we've indexed into the `arr` array at an out-of-bounds
position (2), but the program happily fetched that memory location and tried to
print it as a string 😬.

This type of bug is very popular over at
[https://cve.mitre.org/](https://cve.mitre.org/) 😔

#### With UBsan

Building the same program _with_ UBSan:

```bash
❯ gcc -fsanitize=undefined ubsan-basic.c -o ubsan-basic
```

We can see that the runtime was linked in:

```bash
❯ ldd ubsan-basic
        linux-vdso.so.1 (0x00007ffcccdfd000)

        # libubsan below
        libubsan.so.1 => /lib/x86_64-linux-gnu/libubsan.so.1 (0x00007f22c0cb5000)

        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f22c0ac9000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f22c0ac2000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f22c0aa0000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f22c0887000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f22c086a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f22c163f000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f22c071c000)
```

If we run that program with problematic input, UBSan prints a warning, and the
printf was modified to print a `(null)` value instead of the possibly problematic
fetch.

[(figure: img/ubsan-trap/ubsan-basic.png)](https://interrupt.memfault.com/img/ubsan-trap/ubsan-basic.png)

If it's preferable to have the program crash instead, use the
`-fno-sanitize-recover=all` to disable the error recovery functionality and
immediately crash (exit with non-zero exit code) on errors:

```bash
❯ gcc -fsanitize=undefined -fno-sanitize-recover=all ubsan-basic.c -o ubsan-basic
```

[(figure: img/ubsan-trap/ubsan-basic-no-recover.png)](https://interrupt.memfault.com/img/ubsan-trap/ubsan-basic-no-recover.png)

See details on sanitize-recover here:

[https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Instrumentation-Options.html#index-fno-sanitize-recover](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Instrumentation-Options.html#index-fno-sanitize-recover)
