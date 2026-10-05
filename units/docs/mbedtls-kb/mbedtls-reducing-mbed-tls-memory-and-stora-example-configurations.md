---
id: "mbedtls-reducing-mbed-tls-memory-and-stora-example-configurations"
type: "concept"
domain: "security"
title: "Reducing Mbed TLS memory and storage footprint: Example configurations"
summary: "We provide a few example configurations in the configs directory. Two of them feature footprint optimization for a specific usage profile:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/reduce-polarssl-memory-and-storage-footprint.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/reduce-polarssl-memory-and-storage-footprint.md#example-configurations"
license: "Apache-2.0"
mode: "V"
---

We provide a few example configurations in the `configs` directory. Two of them feature footprint optimization for a specific usage profile:

* [`config-suite-b.h`](https://github.com/Mbed-TLS/mbedtls/blob/development/configs/config-suite-b.h) is a minimal configuration supporting NSA Suite B.
* [`config-ccm-psk-tls1_2.h`](https://github.com/Mbed-TLS/mbedtls/blob/development/configs/config-ccm-psk-tls1_2.h) is a minimal configuration supporting pre-shared key and with AES-CCM.
