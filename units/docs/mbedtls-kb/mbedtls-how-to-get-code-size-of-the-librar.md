---
id: "mbedtls-how-to-get-code-size-of-the-librar"
type: "concept"
domain: "security"
title: "How to get code size of the library"
summary: "Embedded platforms have memory limitations. Deciding what library to use on your product is important, to save overall code size. Therefore, you need the code size of Mbed TLS. This article is relevant for platforms running on Cortex M3/M4."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/code-size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/code-size.md"
license: "Apache-2.0"
mode: "V"
---

Embedded platforms have memory limitations. Deciding what library to use on your product is important, to save overall code size. Therefore, you need the code size of Mbed TLS. This article is relevant for platforms running on Cortex M3/M4.

Mbed TLS is a configurable library, so its code size varies, depending on the configuration used. For more information on how to control and reduce the code size, see [Reducing Mbed TLS memory and storage footprint](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/reduce-polarssl-memory-and-storage-footprint.md).

Obtain the code size of the library by using the `arm-none-eabi-size -t` command (when using the `arm-none-eabi` toolchain).

Mbed TLS supplies a script that checks the [footprint](https://github.com/Mbed-TLS/mbedtls/blob/development/scripts/footprint.sh) of the library. The script shows the code size of the library compiled with several configuration files:

* `include/mbedtls/mbedtls_config.h` (`include/mbedtls/config.h` in Mbed TLS 2.x) - The default configuration file, unless modified by the user.
* `configs/config-thread.h` - A minimal configuration example of Mbed TLS using Thread networking protocol.
* `configs/config-suite-b.h` - A minimal configuration example supporting NSA Suite B.
* `configs/config-ccm-psk-tls1_2.h` - A minimal configuration example supporting preshared key and with AES-CCM.
