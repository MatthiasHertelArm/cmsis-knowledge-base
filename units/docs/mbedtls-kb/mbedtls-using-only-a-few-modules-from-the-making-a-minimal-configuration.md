---
id: "mbedtls-using-only-a-few-modules-from-the-making-a-minimal-configuration"
type: "concept"
domain: "security"
title: "Using only a few modules from the library: Making a minimal configuration"
summary: "The file include/mbedtls/mbedtls_config.h contains a list of features and build-time options. To design a minimal configuration, start with a blank file and add the options you need. The documentation of each option describes its dependencies, if any."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/using-loose-modules-without-the-full-library.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/using-loose-modules-without-the-full-library.md#making-a-minimal-configuration"
license: "Apache-2.0"
mode: "V"
---

The file `include/mbedtls/mbedtls_config.h` contains a list of features and build-time options. To design a minimal configuration, start with a blank file and add the options you need. The documentation of each option describes its dependencies, if any.

Where to put your own configuration file? There are three choices:

* You can edit the file in place, if you wish.
* You can place a file called `mbedtls/mbedtls_config.h` at some location in the include file search path that comes before the `include` directory from the Mbed TLS source tree.
* You can give your configuration file a different name and set the preprocessor symbol `MBEDTLS_CONFIG_FILE` to the location of that file, including surrounding quotes.

For more information, see [How to configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md).

### Random generator example

For example, suppose you want a cryptographically secure random generator and nothing else. A random generator consists of two parts: an entropy source, and a pseudorandom generator seeded by the entropy source. Mbed TLS provides an interface to the system's entropy sources in the `entropy` module enabled by `MBEDTLS_ENTROPY_C`. For the pseudorandom generator, there are two choices: CTR\_DRBG or HMAC\_DRBG, enabled with `MBEDTLS_CTR_DRBG_C` and `MBEDTLS_HMAC_DRBG_C` respectively.

The documentation of `MBEDTLS_ENTROPY_C` states that it requires either `MBEDTLS_SHA512_C` or `MBEDTLS_SHA256_C`. The CTR\_DRBG module requires `MBEDTLS_AES_C`. The HMAC\_DRBG module requires `MBEDTLS_MD_C`, which in turn requires at least one hash module.

You decide to use HMAC\_DRBG, and use SHA-512 as the hash function both for entropy and for the DRBG. As a consequence, you write the following configuration file:

```c
#define MBEDTLS_ENTROPY_C
#define MBEDTLS_HMAC_DRBG_C
#define MBEDTLS_MD_C
#define MBEDTLS_SHA512_C
```

### Notes about Mbed TLS 2.x

In Mbed TLS 2.x, the configuration file is located at `include/mbedtls/config.h`.

You should add the following line at the end of your configuration file:
```c
#include "mbedtls/check_config.h"
```
This will cause compilation errors with descriptive messages if the configuration is inconsistent.
