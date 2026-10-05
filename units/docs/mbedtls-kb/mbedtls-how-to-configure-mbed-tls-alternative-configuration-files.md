---
id: "mbedtls-how-to-configure-mbed-tls-alternative-configuration-files"
type: "concept"
domain: "security"
title: "How to configure Mbed TLS: Alternative configuration files"
summary: "You might want to keep the custom configuration file for your application outside the Mbed TLS source tree. You can do this by defining the macro MBEDTLS_CONFIG_FILE for the desired filename (including the quote or angular brackets) at compile time."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/compiling-and-building/how-do-i-configure-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/compiling-and-building/how-do-i-configure-mbedtls.md#alternative-configuration-files"
license: "Apache-2.0"
mode: "V"
---

You might want to keep the custom configuration file for your application outside the Mbed TLS source tree. You can do this by defining the macro `MBEDTLS_CONFIG_FILE` for the desired filename (including the quote or angular brackets) at compile time. For example, using **make**: (Note: The angle brackets `<>` are included in the command, but they could be replaced with properly escaped double quotes `\"\"`.)
    ```
     CFLAGS="-Ipath/to/config -DMBEDTLS_CONFIG_FILE='<my_config.h>'" make
    ```
or, using **Cmake**:

* If it is not the first run, **clear its cache** before running:
    ```
    find . -iname '*cmake*' -not -name CMakeLists.txt -exec rm -rf {} +
    CFLAGS="-Ipath/to/config -DMBEDTLS_CONFIG_FILE='<my_config.h>'" cmake .
    make
    ```
**Mbed TLS 2.2x only:** We provide a `check_config.h` file that checks the consistency of the configuration file. We highly recommended to `include` it at the end of your custom configuration file. If you use the above setup, you may need to adapt the `include` directive depending on your compiler. (Since Mbed TLS 3.0, `check_config.h` is included automatically.)
