---
id: "mbedtls-tools-for-testing-constant-flow-co-dynamic-analyzers"
type: "concept"
domain: "security"
title: "Tools for testing constant-flow code: Dynamic analyzers"
summary: "Listed for historical reference. This was a dynamic library and patch to valgrind, built on the following fundamental observation by its author, Adam Langley:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/testing-constant-flow.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-constant-flow.md#dynamic-analyzers"
license: "Apache-2.0"
mode: "V"
---

### ctgrind (obsolete)

Listed for historical reference. This was a dynamic library and patch to valgrind, built on the following fundamental observation by its author, Adam Langley:

> This would mean keeping track of every bit in memory to know if it's secret or not, likewise for all the CPU registers. Preferably at the bit level. The tool would also have to know that adding secret and non-secret data results in secret data etc. That suggests that it would be quite a complex tool.
> But memcheck already does this! In order to keep track of uninitialised data it shadows every bit of memory and will warn you if you use uninitialised data in a branch or to index a memory access. So if we could tell memcheck to treat our secret data as uninitialised, everything should just work.

https://github.com/agl/ctgrind

The project is now obsolete thanks to the options below, which are built on the same idea: (ab)use existing tools checking for use of undefined memory.

### Valgrind's memcheck

It turns out patching valgrind and using a helper library is not necessary, as everything we need is already provided by memcheck: after including `valgrind/memcheck.h` we can use the macros `VALGRIND_MAKE_MEM_UNDEFINED(addr, len)` and `VALGRIND_MAKE_MEM_DEFINED(addr, len)` to mark data as secret (undefined) or no longer secret (defined).

These macros have been available under that name since [3.2.0 (7 June 2006)](https://www.valgrind.org/docs/manual/dist.news.old.html).

References:
- https://valgrind.org/docs/manual/mc-manual.html
- https://github.com/mozilla-b2g/valgrind/blob/master/memcheck/memcheck.h

Pros:
- valgrind/memcheck is already used in our CI
- large number of [supported architectures/platforms](https://valgrind.org/info/platforms.html)
- works with any compiler
- works with inline asm
- already used by other projects such as [in BoringSSL](https://boringssl.googlesource.com/boringssl/+/a6a049a6fb51a052347611d41583a0622bc89d60)

Cons:
- just like normal use of valgrind's memcheck, slows down execution by about 20-30x.
- preliminary testing (by Manuel on a personal project) suggests there may be issues with relative ordering of calls to the macros and use of the values in some uses cases (for example, doing a simple sanity check before marking the value as secret flags the sanity check as accessing undefined memory).

Note: since 2.24.0 we're using this: see `MBEDTLS_TEST_CONSTANT_FLOW_VALGRIND` in `config.h`; components `test_valgrind_constant_flow` and `test_valgrind_constant_flow_psa` in `all.sh`; and `tests/suites/test_suite_constant_time`.

### MemSan

Works in a very similar way to valgrind's memcheck: compiling with `clang -fsanitize=memory`, after including `sanitizer/msan_interface.h`, the two following functions (and a couple more) can be used to mark memory areas as secret/undefined or public/defined.
```
  /* Make memory region fully initialized (without changing its contents). */
  void __msan_unpoison(const volatile void *a, size_t size);

  /* Tell MSan about newly allocated memory (ex.: custom allocator).
     Memory will be marked uninitialized, with origin at the call site. */
  void __msan_allocated_memory(const volatile void* data, size_t size);
```

References:
- https://clang.llvm.org/docs/MemorySanitizer.html
- https://github.com/google/sanitizers/wiki/MemorySanitizer
- https://github.com/llvm-mirror/compiler-rt/blob/master/include/sanitizer/msan_interface.h

Pros:
- clang/memsan is already used in our CI
- much faster than valgrind/memcheck (only 2-3x slowdown, so about 10x faster than using valgrind)

Cons:
- only works with clang on Linux, FreeBSD, NetBSD
- being compile-time instrumentation, limited with respect to inline assembly
- for the same reason, misses branches in toolchain-provided functions (for example long multiplication, see Kaufmann et al. [^1]) which valgrind would see
- has an annoying bug where it [misses secret-dependent memory accesses via libc functions](https://github.com/google/sanitizers/issues/1296)

Note: since 2.24.0 we're using this: see `MBEDTLS_TEST_CONSTANT_FLOW_MEMSAN` in `config.h`; components `test_memsan_constant_flow` and ``test_memsan_constant_flow_psa` in `all.sh`; and `tests/suites/test_suite_constant_time`.

[^1]: When Constant-time Source Yields Variable-time Binary: Exploiting Curve25519-donna Built with MSVC 2015. Thierry Kaufmann, Hervé Pelletier, Serge Vaudenay, and Karine Villegas. 21 December 2016, Springer Science and Business Media LLC. DOI: 10.1007/978-3-319-48965-0_36. https://core.ac.uk/reader/148026376

### Custom tools

From looking at papers, it seems that various researchers are using various custom tools for finding leaks in cryptographic software. However it is unclear if those are publicly available, and being developed by academics mainly for their own use, it's also unclear how easy they would be to deploy on our CI infrastructure.
