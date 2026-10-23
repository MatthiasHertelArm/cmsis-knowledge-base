---
id: "mbedtls-how-to-tune-elliptic-curves-resour"
type: "concept"
domain: "security"
title: "How to tune Elliptic Curves resource usage"
summary: "Like most parts of Mbed TLS, the implementation of elliptic curve operations can be tuned using various compilation flags."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md"
license: "Apache-2.0"
mode: "V"
---

Like most parts of Mbed TLS, the implementation of elliptic curve operations can be tuned using various [compilation flags](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md). This page explains the two parameters that control trade-offs between performance and footprint in more detail than our general documentation on [reducing footprint](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/reduce-polarssl-memory-and-storage-footprint.md).
