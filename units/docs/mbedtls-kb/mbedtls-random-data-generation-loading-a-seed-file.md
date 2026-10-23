---
id: "mbedtls-random-data-generation-loading-a-seed-file"
type: "concept"
domain: "security"
title: "Random data generation: Loading a seed file"
summary: "Another way to add entropy at the start of your application is to use a seed file. The Mbed TLS random generator can read and update a seed file with mbedtls_ctr_drbg_update_seed_file() to increase entropy."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-a-random-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-a-random-generator.md#loading-a-seed-file"
license: "Apache-2.0"
mode: "V"
---

Another way to add entropy at the start of your application is to use a seed file. The Mbed TLS random generator can read and update a seed file with `mbedtls_ctr_drbg_update_seed_file()` to increase entropy.
