---
id: "mbedtls-entropy-collection-random-generati-random-generators-and-entropy"
type: "concept"
domain: "security"
title: "Entropy collection, random generation with threads: Random generators and entropy"
summary: "The random generators themselves, like CTR-DRBG, do not require new entropy every time they are called."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/entropy-collection-and-random-generation-in-threaded-environment.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/entropy-collection-and-random-generation-in-threaded-environment.md#random-generators-and-entropy"
license: "Apache-2.0"
mode: "V"
---

The random generators themselves, like CTR-DRBG, do not require new entropy every time they are called. Instead, they expand the available entropy to produce random without compromising the original entropy and being secure as long as not too much random is generated from one state. Therefore, the random generators occasionally gather entropy from the entropy collector to refresh their state.
