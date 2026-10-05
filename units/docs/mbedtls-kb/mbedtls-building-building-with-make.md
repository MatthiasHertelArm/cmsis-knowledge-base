---
id: "mbedtls-building-building-with-make"
type: "concept"
domain: "security"
title: "Building: Building with Make"
summary: "If using Make, you can build by running:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:getting_started/building.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/getting_started/building.md#building-with-make"
license: "Apache-2.0"
mode: "V"
---

If using Make, you can build by running:
```sh
make
```
To run the test suite, run:
```sh
make check
```

To select a different compiler, set the `CC` variable to the name or path of the
compiler and linker (default: `cc`) and set `AR` to a compatible archiver
(default: `ar`); for example:
```sh
make CC=arm-linux-gnueabi-gcc AR=arm-linux-gnueabi-ar
```
The provided makefiles pass options to the compiler that assume a GCC-like
command line syntax. To use a different compiler, you may need to pass different
values for `CFLAGS`, `WARNINGS_CFLAGS` and `LDFLAGS`.
