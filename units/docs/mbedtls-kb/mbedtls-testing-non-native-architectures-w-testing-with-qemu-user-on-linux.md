---
id: "mbedtls-testing-non-native-architectures-w-testing-with-qemu-user-on-linux"
type: "concept"
domain: "security"
title: "Testing non-native architectures with QEMU: Testing with qemu-user on Linux"
summary: "With mtest:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/testing/testing-qemu.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/testing/testing-qemu.md#testing-with-qemu-user-on-linux"
license: "Apache-2.0"
mode: "V"
---

### Cmake build

For example for aarch64:

```
mkdir build-aarch64
cd build-aarch64
CC=clang CFLAGS="--target=aarch64-linux-gnu" cmake -DCMAKE_BUILD_TYPE=Release ..
make -j2
cd tests
qemu-aarch64 -L /usr/aarch64-linux-gnu ./test_suite_mpi
```

### mtest

With [mtest](https://github.com/Mbed-TLS/mbedtls-docs/blob/main/tools/bin/mtest):

```
mtest <arch> <test names>
```

e.g.

```
mtest aarch64 cmac
```

### mbedtls-prepare-build

With [mbedtls-prepare-build](https://github.com/Mbed-TLS/mbedtls-docs/blob/main/tools/bin/mbedtls-prepare-build):

```
mbedtls-prepare-build -d build-aarch64 --cc=clang --cflags='-O2 -target aarch64-linux-gnu' --qemu-ld-prefix=aarch64-linux-gnu
make -C build-aarch64 test
```
