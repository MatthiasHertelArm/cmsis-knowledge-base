---
id: "mbedtls-tips-for-debugging-mbed-tls-sanitizers"
type: "concept"
domain: "security"
title: "Tips for debugging Mbed TLS: Sanitizers"
summary: "Valgrind mostly duplicates Asan+Msan, but very occasionally finds something that they don't."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/debugging_tips.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/debugging_tips.md#sanitizers"
license: "Apache-2.0"
mode: "V"
---

### Sanitizers used in test scripts

#### ASan: AddressSanitizer

* Documentation: https://github.com/google/sanitizers/wiki/addresssanitizer
* Detects: buffer overflows, use after free, memory leaks
* Compilers: GCC, Clang
* Compiler flags: `-fsanitize=address -fno-sanitize-recover=all` (in both `CFLAGS` and `LDFLAGS`)
* CMake build types: `ASan`, `ASanDbg`
* Used in: most builds in `all.sh`

#### MSan: MemorySanitizer

* Documentation: https://github.com/google/sanitizers/wiki/memorysanitizer
* Detects: uninitialized memory
* Compilers: GCC, Clang
* Compiler flags: `-fsanitize=memory` (in both `CFLAGS` and `LDFLAGS`)
* CMake build types: `MemSan`, `MemSanDbg`
* Used in: `component_test_memsan*`

#### TSan: ThreadSanitizer

* Documentation: https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual
* Detects: race conditions
* Compilers: GCC, Clang
* Compiler flags: `-fsanitize=thread` (in both `CFLAGS` and `LDFLAGS`)
* CMake build types: `TSan`, `TSanDbg`
* Used in: `component_test_tsan*`

#### UBSan: UndefinedBehaviorSanitizer

* Documentation: https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html
* Detects: null pointer misuse, bitwise shift amount out of range, signed integer overflow, …
* Compilers: GCC, Clang
* Compiler flags: `-fsanitize=undefined` (in both `CFLAGS` and `LDFLAGS`)
* CMake build types: `ASan`, `ASanDbg`
* Used in: most builds in `all.sh`

### Valgrind

Valgrind mostly duplicates Asan+Msan, but very occasionally finds something that they don't.

* Documentation: https://valgrind.org/docs/manual/manual.html
* Detects: buffer overflows, use after free, memory leaks, uninitialized memory
    * We don't currently use it for race conditions.
* Compilers: any
* Compiler flags: N/A — runtime instrumentation only
* CMake target: `make memcheck`
* Run with:
    ```
    valgrind -q --tool=memcheck --leak-check=yes --show-reachable=yes --num-callers=50 --log-file=myprogram.MemoryChecker.log myprogram
    grep . myprogram.MemoryChecker.log myprogram
    ```
* Used in: `component_release_test_valgrind*`

### Getting symbolic backtraces from symbolizers

By default, ASan/MSan/TSan/UBSan display traces without symbolic information. For traces with symbol names, you need to set environment variables:

```
export ASAN_OPTIONS=symbolize=1
export MSAN_OPTIONS=symbolize=1
export TSAN_OPTIONS=symbolize=1
export UBSAN_OPTIONS=print_stacktrace=1
```

With Clang, depending on how it's installed, you may need to specify the path to the correct version of `llvm-symbolizer` in `ASAN_SYMBOLIZER_PATH`, `MSAN_SYMBOLIZER_PATH` and `TSAN_SYMBOLIZER_PATH`. For example:

```
if ASAN_SYMBOLIZER_PATH=$(readlink -f "$(command -v clang)") &&
   ASAN_SYMBOLIZER_PATH="${ASAN_SYMBOLIZER_PATH%/*}/llvm-symbolizer"
then
  export ASAN_SYMBOLIZER_PATH
  export MSAN_SYMBOLIZER_PATH="$ASAN_SYMBOLIZER_PATH"
  export TSAN_SYMBOLIZER_PATH="$ASAN_SYMBOLIZER_PATH"
fi
```

See [SanitizerCommonFlags](https://github.com/google/sanitizers/wiki/SanitizerCommonFlags) for more flags you can use in `$xxSAN_OPTIONS`.

### Sanitizers for constant-time testing

See “[Mbed TLS test guidelines — Constant-flow testing](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../development/test_suites.md#constant-flow-testing)”.
