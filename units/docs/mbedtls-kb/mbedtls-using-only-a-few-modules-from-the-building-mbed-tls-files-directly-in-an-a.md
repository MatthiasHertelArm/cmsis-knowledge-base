---
id: "mbedtls-using-only-a-few-modules-from-the-building-mbed-tls-files-directly-in-an-a"
type: "concept"
domain: "security"
title: "Using only a few modules from the library: Building Mbed TLS files directly in an application"
summary: "Mbed TLS comes with build scripts for GNU make (Makefile), CMake (CMakeLists.txt) and Visual Studio (visualc/VS2010/mbedTLS.sln). By default, these create static libraries mbedcrypto, mbedx509 and mbedtls which you can link into your application."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/using-loose-modules-without-the-full-library.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/using-loose-modules-without-the-full-library.md#building-mbed-tls-files-directly-in-an-application"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS comes with build scripts for GNU make (`Makefile`), CMake (`CMakeLists.txt`) and Visual Studio (`visualc/VS2010/mbedTLS.sln`). By default, these create static libraries `mbedcrypto`, `mbedx509` and `mbedtls` which you can link into your application. (You don't need to link `mbedx509` or `mbedtls` if you don't use these features.) For more information, see [How to compile and build Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../compiling-and-building/how-do-i-build-compile-mbedtls.md).

If you prefer, you can include the Mbed TLS source files in your own build scripts. All the library code is in the `library` subdirectory, except for a few features that use code from the `3rdparty` directory tree. All the public headers are in the `include` directory tree.

### Compiling with Mbed TLS headers

Both when building your application and when building Mbed TLS source files, make sure that the `include` directory of the Mbed TLS source tree is present in the header search path. For example, if Mbed TLS is in the subdirectory `external/mbedtls`:
```console
$ cc -I external/mbedtls/include …
```

If you have a custom configuration file with the same name in a different directory, it must come first on the header search path. For example, if your Mbed TLS configuration file is located at `configs/mbedtls/mbedtls_config.h` and the Mbed TLS source tree is located at `external/mbedtls`:
```console
$ cc -I configs -I external/mbedtls/include …
```

Recall that alternatively, you can give your configuration file a different name and specify its location with the preprocessor symbol `MBEDTLS_CONFIG_FILE`. For example, if your Mbed TLS configuration file is located at `my_mbedtls_config.h` and the Mbed TLS source tree is located at `external/mbedtls`.

```console
$ cc -DMBEDTLS_CONFIG_FILE='"my_mbedtls_config.h"' -I configs -I external/mbedtls/include …
```

Note that **you must pass the same configuration when building Mbed TLS and building your application**. Passing a different configuration is likely to result in misbehavior at runtime.

### Linking Mbed TLS objects

When you build Mbed TLS with the provided build scripts, all the source files are compiled. However, the resulting object files are empty for features that are disabled.

If you wish, you can link selectively with just the object files you need. Generally speaking, a feature called `MBEDTLS_XXX_C` is provided by the file `library/xxx.c`. There are a few exceptions:

* The Everest implementation of Curve25519 (`MBEDTLS_ECDH_VARIANT_EVEREST_ENABLED`) requires files from `3rdparty/everest`.
* The PSA cryptography interface (`MBEDTLS_PSA_CRYPTO_C`) requires several files `library/psa_crypto_*.c` in addition to `library/psa_crypto.c` itself.
* The TLS protocol implementation requires `library/ssl_msg.c` and possibly more files `ssl_tls1*.c` depending on which protocol versions are enabled, in addition to `library/ssl_tls.c`.
