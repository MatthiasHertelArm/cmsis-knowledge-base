---
id: "mbedtls-random-data-generation"
type: "concept"
domain: "security"
title: "Random data generation"
summary: "When making a security application, you may require a random data generator. Arm Mbed TLS includes the CTR-DRBG module for random generation."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-a-random-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-a-random-generator.md"
license: "Apache-2.0"
mode: "V"
---

When making a security application, you may require a random data generator. Arm Mbed TLS includes the [CTR-DRBG module](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/ctr-drbg-source-code.html) for random generation.

Setting up CTR-DRBG in your code requires an entropy source and a personalization string.
