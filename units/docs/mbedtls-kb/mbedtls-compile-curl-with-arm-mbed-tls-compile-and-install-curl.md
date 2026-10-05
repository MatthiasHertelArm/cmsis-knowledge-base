---
id: "mbedtls-compile-curl-with-arm-mbed-tls-compile-and-install-curl"
type: "concept"
domain: "security"
title: "Compile cURL with Arm Mbed TLS: Compile and install cURL"
summary: "To compile cURL with Mbed TLS, you need to configure the build system. Normally you would use the configure script without any options, but in this case some options are needed. Enter:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/compile-curl-with-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/compile-curl-with-mbedtls.md#compile-and-install-curl"
license: "Apache-2.0"
mode: "V"
---

To compile cURL with Mbed TLS, you need to configure the build system. Normally you would use the configure script without any options, but in this case some options are needed. Enter:

```
./configure --without-ssl --with-mbedtls
```

The `without-ssl` and `with-mbedtls` parameters instruct the build system to use Mbed TLS instead of the default SSL library. When the configure script finishes, it states something like this:

Compile and install cURL

To compile and install cURL, enter:

```
make
sudo make install
```

You need administrator privileges to execute the second command. The cURL program is now installed in `/usr/local/bin`.
