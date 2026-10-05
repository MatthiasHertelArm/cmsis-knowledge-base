---
id: "mbedtls-mbed-tls-ci-tooling"
type: "concept"
domain: "security"
title: "Mbed TLS CI: Tooling"
summary: "This section describes some of the tooling needed to reproduce CI failures locally. Typical Linux or Mac developer machines have most of the necessary tooling, but not all."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/testing-ci.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-ci.md#tooling"
license: "Apache-2.0"
mode: "V"
---

This section describes some of the tooling needed to reproduce CI failures locally. Typical Linux or Mac developer machines have most of the necessary tooling, but not all. Note in particular that the SSL test scripts are written with specific versions of GnuTLS and OpenSSL in mind, and tend to have spurious failure when run against different versions.

For Linux-based tests, you can download Docker files with all the tools from the [mbedtls-test repository](https://github.com/Mbed-TLS/mbedtls-test/tree/main/resources/docker_files).

### Tooling for all.sh

To run `tests/scripts/all.sh`, you need at least the following tools:

* basic Unix/POSIX shell utilities. Currently any modern `sh` should do, but a dependency on `bash` may be added in 2020.
* Git. `all.sh` requires a Git checkout. The following files may be restored to their checked-in version: `include/mbedtls/config.h`, `**/Makefile`.

`all.sh` is composed of many components, some of which have additional requirements. Most components require the following tools:

* `gcc` or `clang` (depending on the component) for native builds.
* GNU make or CMake (depending on the component).
* Perl 5.
* Python ≥3.6 (different branches may have different version requirements).
* The commands `openssl`, `gnutls-cli` and `gnutls-serv` must be present in the `$PATH` to run any test component (otherwise `all.sh` refuses to start). If you don't have them, you can still run some test components that don't do any interoperability testing with `env OPENSSL=false GNUTLS_CLI=false GNUTLS_SERV=false tests/scripts/all.sh …`.

### Running `all.sh` on Ubuntu

Our reference Linux platform is Ubuntu 16.04 x86 64-bit. More recent Ubuntu versions should also work.

On Ubuntu 16.04, the following packaged tools are known to cause problems with `all.sh`:

* The `gnutls-bin` package on Ubuntu 16.04 does not work with our test scripts because Ubuntu has removed some obsolete features.

On Ubuntu 20.04, the following packaged tools are known to cause problems with `all.sh`:

* `all.sh check_doxygen_warnings` fails. Doxygen 1.8.11 and 1.8.13 are known to work.

On Ubuntu, for the 32-bit builds, install the following packages:
```
apt-get install gcc-multilib libc6-dev-i386 linux-libc-dev:i386 libc6:386
```
Instead of `gcc-multilib`, which conflicts with cross-compilers for non-Intel architectures, a versioned package (e.g. `gcc5-multilib`) will do, but you need to create an additional symbolic link:
```
ln -s x86_64-linux-gnu/asm /usr/include/asm
```

### Notes about networking

The tests attempt to establish an IPv6 connection to the local host. This is optional, and will be skipped if IPv6 is not available. However, if IPv6 is possible but IPv6 connections to localhost are blocked by a firewall, the test will fail.
