---
id: "mbedtls-compile-curl-with-arm-mbed-tls-compile-and-install-mbed-tls"
type: "concept"
domain: "security"
title: "Compile cURL with Arm Mbed TLS: Compile and install Mbed TLS"
summary: "Now compile the source code by entering:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/compile-curl-with-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/compile-curl-with-mbedtls.md#compile-and-install-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Now compile the source code by entering:

```
make CFLAGS=-fPIC
```

Optionally, you can check that Mbed TLS works correctly by entering:

```
make check
```

To install the library, enter:

```
sudo make install
```

Note that you need administrator privileges to execute this command. The Mbed TLS library is now installed in `/usr/local/lib`.
