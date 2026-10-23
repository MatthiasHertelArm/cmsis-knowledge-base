---
id: "mbedtls-random-data-generation-multithreaded-use"
type: "concept"
domain: "security"
title: "Random data generation: Multithreaded use"
summary: "If you intend to use the CTR-DRBG module in multiple threads, please read our article on entropy collection, random generation with threads."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-a-random-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-a-random-generator.md#multithreaded-use"
license: "Apache-2.0"
mode: "V"
---

If you intend to use the CTR-DRBG module in multiple threads, please read our article on [entropy collection, random generation with threads](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../development/entropy-collection-and-random-generation-in-threaded-environment.md).

<!--- "add-a-random-generator","Short article on how to add a good random generator to your application. Complete with source code examples!",,"entropy, random data, random number generator, RNG, ctr-drbg, entropy pool, security",published,"2013-09-11 12:10:00",2,11128,"2017-04-24 11:16:00","Paul Bakker" --->
