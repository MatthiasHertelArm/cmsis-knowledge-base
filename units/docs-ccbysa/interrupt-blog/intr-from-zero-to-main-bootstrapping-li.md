---
id: "intr-from-zero-to-main-bootstrapping-li"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib"
summary: "This is the fourth post in our Zero to main() series, where we worked methodically to demystify what happens to firmware before the main() function is called."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is the fourth post in our [Zero to main() series](), where we worked methodically to demystify what happens to
firmware before the main() function is called. So far, we bootstrapped a C
environment, wrote a linker script from scratch, and implemented our own
bootloader.

And yet, we cannot even write a hello world program! Consider the following
`main.c` file:

```c
#include <stdio.h>

int main() {
  printf("Hello, World\n");
  while (1) {}
}
```
Compiling this using our Makefile and linker script from [previous](https://interrupt.memfault.com/blog/zero-to-main-1) [posts](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware), we hit
the following error:

```shell
$ make
...
Linking build/minimal.elf
arm-none-eabi/bin/ld: build/objs/a/b/c/minimal.o: in function `main':
/minimal/minimal.c:4: undefined reference to `printf'
collect2: error: ld returned 1 exit status
make: *** [build/minimal.elf] Error 1
```

Undefined reference to `printf`! How could this be? Our firmware’s C environment
is still missing a key component: a working C standard library.  This means that
commonly used functions such as `printf`, `memcpy`, or `strncpy` are all out of
reach of our program so far.

In firmware-land, nothing comes free with the system: just like we had to
explicitly zero out the `bss` region to initialize some of our static variables,
we’ll have to port a `printf` implementation alongside a C standard library if
we want to use it.


In this post, we will add RedHat’s Newlib to our firmware and highlight some of
its features. We will implement syscalls, learn about constructors, and finally
print out “Hello, World”! We will also learn how to replace parts or all of the
standard C library.
