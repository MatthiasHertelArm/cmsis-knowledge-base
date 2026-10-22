---
id: "mbedtls-tips-for-debugging-mbed-tls-reproducing-ci-builds-with-debugging"
type: "concept"
domain: "security"
title: "Tips for debugging Mbed TLS: Reproducing CI builds with debugging"
summary: "Normally, all.sh cleans up after itself. However, it will leave build products around if a compilation or runtime step fails. If you want to see build products from a passing component, add the command false after the build steps."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/debugging_tips.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/debugging_tips.md#reproducing-ci-builds-with-debugging"
license: "Apache-2.0"
mode: "V"
---

### Getting the build products from `all.sh`

Normally, `all.sh` cleans up after itself. However, it will leave build products around if a compilation or runtime step fails. If you want to see build products from a passing component, add the command `false` after the build steps.

If you have a wrapper around `all.sh`, note that passing `--keep-going` (`-k`) makes it clean up on errors as well.

Cancelling `all.sh` with `Ctrl+C` (SIGINT) makes it clean up. But using `Ctrl+\\` (SIGQUIT) bypassing the cleanup. Also, you can use `Ctrl+Z` to inspect an intermediate step.

### Editing `all.sh` for debugging

To reproduce an `all.sh` component locally, but with debugging enabled:

* For most builds using `make` (without CMake), in particular including all driver builds: add `ASAN_CFLAGS='-Og -g3'` or `ASAN_CFLAGS='-O0 -g3'` before the build step.
* For builds using CMake: add or change the build type to `Debug` or `ASanDbg`, e.g. `cmake -DCMAKE_BUILD_TYPE=Debug`.

After changing the source, you'll need to re-run `all.sh`, including its initial cleanup state which is not trivial to bypass. To speed this up, enable [ccache](https://ccache.dev/). In most `all.sh` components, you can enable ccache by setting
```
CC="ccache ${CC:cc}" ASAN_CC="ccache clang"
```
