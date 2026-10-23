---
id: "mbedtls-sample-applications-random"
type: "concept"
domain: "security"
title: "Sample Applications: *`random`*"
summary: "These applications demonstrate how to use Mbed TLS TRNG and PRNG APIs."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/sample_applications.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/sample_applications.md#random"
license: "Apache-2.0"
mode: "V"
---

These applications demonstrate how to use Mbed TLS TRNG and PRNG APIs.

- `gen_entropy` - An application that generates multiple entropy calls from the TRNG engine, writing them to a file. (only available in versions prior to 4.0)
- `gen_random_ctr_drbg` - An application demonstrating how to use the Mbed TLS Deterministic Random Bit Generators (DRBG) API, using AES, defined in NIST [800-90A](http://csrc.nist.gov/publications/nistpubs/800-90A/SP800-90A.pdf). (only available in versions prior to 4.0)
- `gen_random_havege` - An application demonstrating how to use the HArdware Volatile Entropy Gathering and Expansion ([havege](http://www.irisa.fr/caps/projects/hipsor/)) entropy API.
