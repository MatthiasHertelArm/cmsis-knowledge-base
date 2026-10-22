---
id: "mbedtls-reducing-mbed-tls-memory-and-stora-binary-footprint"
type: "concept"
domain: "security"
title: "Reducing Mbed TLS memory and storage footprint: Binary footprint"
summary: "The binary footprint is the size of the actual file on disk, in the ROM or the flash."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/reduce-polarssl-memory-and-storage-footprint.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/reduce-polarssl-memory-and-storage-footprint.md#binary-footprint"
license: "Apache-2.0"
mode: "V"
---

The binary footprint is the size of the actual file on disk, in the ROM or the flash.

### Minimizing features

By default, Mbed TLS offers several compatibility options and frequently used functionalities. To reduce the footprint, adapt `mbedtls_config.h` to disable the functions that you do not need.
