---
id: "intr-profiling-newlib-nano-s-memcpy-newlib-s-non-nano-implementation"
type: "concept"
domain: "debug"
title: "Profiling newlib-nano's memcpy: Newlib's non-nano implementation"
summary: "The above version of memcpy is the one used when linking with --specs=nano.specs; the \"nano\" version of libc, which is intended to optimize for code space (the nano specs override some libraries with the \"nano\" variant, see here)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-09-07-memcpy-newlib-nano.md"
doc_source: "https://interrupt.memfault.com/blog/memcpy-newlib-nano#newlib-s-non-nano-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

The above version of `memcpy` is the one used when linking with
`--specs=nano.specs`; the "nano" version of libc, which is intended to optimize
for code space (the nano specs override some libraries with the "nano" variant,
see
[here](https://cygwin.com/git/?p=newlib-cygwin.git;a=blob;f=libgloss/arm/elf-nano.specs;h=82594bd03cea8584188f625826deb20a50fee603;hb=HEAD)).

Linking without selecting the nano specs yields a much larger binary (in the
test repo, my application went from ~17kB to ~33kB). However, not only do the
non-nano versions more closely match glibc implementations (eg more
`printf/scanf` formatters are supported by default), the implementations tend to
be much more optimized for speed. This implementation of `memcpy` is 308 bytes-
it's implemented in assembly with several unrolled loop optimizations:

> [https://cygwin.com/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/arm/memcpy-armv7m.S;h=c8bff36f60cf6ed520172c85406f6a9529f41de3;hb=HEAD](https://cygwin.com/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/machine/arm/memcpy-armv7m.S;h=c8bff36f60cf6ed520172c85406f6a9529f41de3;hb=HEAD)

The same test as we did above results in:

```plaintext
len = 1, cyccnt = 39, cycles/byte = 39.000
len = 2, cyccnt = 40, cycles/byte = 20.000
len = 4, cyccnt = 37, cycles/byte = 9.250
len = 8, cyccnt = 45, cycles/byte = 5.625
len = 16, cyccnt = 43, cycles/byte = 2.688
len = 32, cyccnt = 60, cycles/byte = 1.875
len = 64, cyccnt = 81, cycles/byte = 1.266
len = 128, cyccnt = 134, cycles/byte = 1.047
len = 256, cyccnt = 240, cycles/byte = 0.938
len = 512, cyccnt = 452, cycles/byte = 0.883
len = 1024, cyccnt = 876, cycles/byte = 0.855
len = 2048, cyccnt = 1724, cycles/byte = 0.842
len = 4096, cyccnt = 3420, cycles/byte = 0.835
```

About **13x** faster than the original newlib-nano implementation! 🥳
