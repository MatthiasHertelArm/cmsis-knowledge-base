---
id: "mbedtls-reducing-mbed-tls-memory-and-stora"
type: "concept"
domain: "security"
title: "Reducing Mbed TLS memory and storage footprint"
summary: "This page includes some of the optimizations that can help you reduce the RAM and ROM footprint of the Mbed TLS library. These are generic optimizations that do not require massive modifications to the code."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/reduce-polarssl-memory-and-storage-footprint.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/reduce-polarssl-memory-and-storage-footprint.md"
license: "Apache-2.0"
mode: "V"
---

This page includes some of the optimizations that can help you reduce the RAM and ROM footprint of the Mbed TLS library. These are generic optimizations that do not require massive modifications to the code. This page discusses reductions of the compiled library (see [Binary footprint](#binary-footprint)) and reductions to the runtime memory (see [Memory footprint](#memory-footprint)).

All of the settings described on this page are available in `mbedtls_config.h`, see [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md).

If you need to reduce your memory footprint even more or have related questions, please submit a query in our [support forum](https://forums.mbed.com/c/mbed-tls.html) or open an issue in our [GitHub repository](https://github.com/Mbed-TLS/mbedtls/issues.html). We welcome ideas you may have to further reduce the size in RAM or ROM storage. Please, let us know if you have suggestions for improvements.
