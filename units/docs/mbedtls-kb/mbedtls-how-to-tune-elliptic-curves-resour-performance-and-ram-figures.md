---
id: "mbedtls-how-to-tune-elliptic-curves-resour-performance-and-ram-figures"
type: "concept"
domain: "security"
title: "How to tune Elliptic Curves resource usage: Performance and RAM figures"
summary: "Since this page discusses performance-footprint trade-offs, it's useful to have some performance figures. For convenience, the figures quoted in this article were collected with Mbed TLS 2.2 on a machine with a 64-bit CPU."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/how-do-i-tune-elliptic-curves-resource-usage.md#performance-and-ram-figures"
license: "Apache-2.0"
mode: "V"
---

Since this page discusses performance-footprint trade-offs, it's useful to have some performance figures. For convenience, the figures quoted in this article were collected with Mbed TLS 2.2 on a machine with a 64-bit CPU. You can reproduce those results on your machine using [scripts/ecc-heap.sh](https://github.com/Mbed-TLS/mbedtls/blob/development/scripts/ecc-heap.sh) from the Mbed TLS sources.

The RAM figures only include heap usage, not the stack. This is a limitation of the measurement script. However, these should still be useful, as most memory used by elliptic curve operations will be on the heap. Remember, however, that RAM figures may be slightly lower on a 32-bit machine.
