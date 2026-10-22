---
id: "mbedtls-how-to-configure-mbed-tls-the-configuration-script"
type: "concept"
domain: "security"
title: "How to configure Mbed TLS: The configuration script"
summary: "You can edit the configuration file manually with a text editor of your choice. In some cases, however, it may be useful to set options in a more programmatic way. We provide a Python script scripts/config.py for doing so:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/how-do-i-configure-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/how-do-i-configure-mbedtls.md#the-configuration-script"
license: "Apache-2.0"
mode: "V"
---

You can edit the configuration file manually with a text editor of your choice. In some cases, however, it may be useful to set options in a more programmatic way. We provide a Python script `scripts/config.py` for doing so:
    ```
    scripts/config.py unset <name>
    scripts/config.py set <name> [<value>]
    ```
The `config.py` script automatically finds the `mbedtls_config.h` file when it runs this way from Mbed TLS' root directory. If you want to run it from another directory or on another configuration file (see below), you need to use the `-f` option.
