---
id: "mbedtls-how-to-configure-mbed-tls-the-configuration-file"
type: "concept"
domain: "security"
title: "How to configure Mbed TLS: The configuration file"
summary: "The default configuration file is located in include/mbedtls/mbedtls_config.h (include/mbedtls/config.h up to Mbed TLS 2.28). It is fully documented and contains the following sections:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/compiling-and-building/how-do-i-configure-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/compiling-and-building/how-do-i-configure-mbedtls.md#the-configuration-file"
license: "Apache-2.0"
mode: "V"
---

The default configuration file is located in `include/mbedtls/mbedtls_config.h` (`include/mbedtls/config.h` up to Mbed TLS 2.28). It is [fully documented](https://github.com/api/config_8h.html) and contains the following sections:

* Select options depending on your platform in **System support**: does your compiler support inline assembly, does your libc/network stack provide IPv6, and so on.
* Select which features you want to enable for corresponding modules in **Mbed TLS feature support**: which TLS version to support, which key exchanges, which specific elliptic curves, and so on.
* Select modules to build in **Mbed TLS modules**. You can, for example, completely disable RSA or MD5 if you don't need them.
* Set specific options for each module, such as the maximum size of multi-precision integers, or the size of the internal I/O buffers for SSL, in **Module configuration options**. All of these options have default values.
