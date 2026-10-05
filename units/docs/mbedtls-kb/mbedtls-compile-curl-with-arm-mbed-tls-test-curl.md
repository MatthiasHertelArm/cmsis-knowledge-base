---
id: "mbedtls-compile-curl-with-arm-mbed-tls-test-curl"
type: "concept"
domain: "security"
title: "Compile cURL with Arm Mbed TLS: Test cURL"
summary: "To test the installation, you can enter:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/compile-curl-with-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/compile-curl-with-mbedtls.md#test-curl"
license: "Apache-2.0"
mode: "V"
---

To test the installation, you can enter:

```
curl -V
```

This confirms that cURL is using Mbed TLS. To test the SSL capabilities of cURL, you can retrieve an HTML header with an HTTPS request:

```
curl -I https://www.google.com/
```

The result is something like this:

Test cURL

**Note:** If you see the `libcurl.so.4: cannot open shared object file: No such file or directory` error, you need to type `ldconfig` first.

**Note:** You may need to add the path to `libcurl.so` ( `/usr/local/lib`) to your `LD_LIBRARY_PATH`.
