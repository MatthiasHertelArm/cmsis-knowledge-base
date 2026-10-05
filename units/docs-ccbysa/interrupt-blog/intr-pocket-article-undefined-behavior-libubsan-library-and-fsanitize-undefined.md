---
id: "intr-pocket-article-undefined-behavior-libubsan-library-and-fsanitize-undefined"
type: "concept"
domain: "debug"
title: "Pocket article: Undefined Behavior Sanitizer Trap on Error: `libubsan` library and `-fsanitize-undefined-trap-on-error`"
summary: "For hosted platforms (eg Linux, BSD's, macOS, Windows), there's usually a libubsan library installed with your toolchain. On my system it's here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-06-22-ubsan-trap.md"
doc_source: "https://interrupt.memfault.com/blog/ubsan-trap#libubsan-library-and-fsanitize-undefined-trap-on-error"
license: "CC-BY-SA-4.0"
mode: "V"
---

For hosted platforms (eg Linux, BSD's, macOS, Windows), there's usually a
`libubsan` library installed with your toolchain. On my system it's here:

```bash
❯ ldconfig -p | grep libubsan
        libubsan.so.1 (libc6,x86-64) => /lib/x86_64-linux-gnu/libubsan.so.1
```

We saw above that it's linked into our executable, so we end up depending on it
at runtime; on unhosted platforms (eg, embedded bare metal, or RTOS's) it may
not exist! Luckily, both GCC and Clang support this flag:

`-fsanitize-undefined-trap-on-error`

Which will instead insert an undefined instruction (on armv7-m, `udf`) on
errors. Let's see how that works:

```bash
❯ gcc -fsanitize=undefined -fsanitize-undefined-trap-on-error ubsan-basic.c -o ubsan-basic
❯ ldd ubsan-basic
        linux-vdso.so.1 (0x00007ffc6c110000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f62c4b00000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f62c4d04000)

# running with problematic input results in a crash!
❯ ./ubsan-basic 2
[1]    529554 illegal hardware instruction (core dumped)  ./ubsan-basic 2
```

As seen above, the undefined instruction trap should cause your program to crash
in a noticeable way (eg, on Cortex-M processors, you end up in a UsageFault, and
the `UNDEFINSTR` bit will be set in the `UFSR` register). You can use this to
instrument/detect the cases of undefined behavior, and FIX them 🤩!

Compiling with this flag also reduces the output binary somewhat, here's a
comparison for our test program:

```bash
# compile without ubsan
❯ gcc ubsan-basic.c -o ubsan-basic-noubsan
# compile with normal ubsan
❯ gcc -fsanitize=undefined ubsan-basic.c -o ubsan-basic
# compile with ubsan and trap-on-error
❯ gcc -fsanitize=undefined -fsanitize-undefined-trap-on-error ubsan-basic.c -o ubsan-basic-trap-on-error

❯ size ubsan-basic-noubsan ubsan-basic ubsan-basic-trap-on-error
   text    data     bss     dec     hex filename
   1894     616       8    2518     9d6 ubsan-basic-noubsan
   2874     944       8    3826     ef2 ubsan-basic
   2054     616       8    2678     a76 ubsan-basic-trap-on-error
```
