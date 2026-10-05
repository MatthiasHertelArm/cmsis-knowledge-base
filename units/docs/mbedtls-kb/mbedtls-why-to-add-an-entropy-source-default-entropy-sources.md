---
id: "mbedtls-why-to-add-an-entropy-source-default-entropy-sources"
type: "concept"
domain: "security"
title: "Why to add an entropy source: Default entropy sources"
summary: "In the default Mbed TLS, the entropy collector tries to use what the platform you run can provide. For Linux and UNIX-like systems, this is /dev/urandom. For Windows, this is CryptGenRandom of the CryptoAPI. These are considered strong entropy sources."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/add-entropy-sources-to-entropy-pool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/add-entropy-sources-to-entropy-pool.md#default-entropy-sources"
license: "Apache-2.0"
mode: "V"
---

In the default Mbed TLS, the entropy collector tries to use what the platform you run can provide. For Linux and UNIX-like systems, this is **/dev/urandom**. For Windows, this is `CryptGenRandom` of the **CryptoAPI**. These are considered strong entropy sources.

If you have **MBEDTLS_TIMING_C** enabled, the entropy collector also adds the `mbedtls_timing_hardclock()` value. This is only a little entropy, but every bit helps.

If you have **MBEDTLS_HAVEGE_C** enabled, Mbed TLS also uses the HAVEGE RNG. 

**Note:** The HAVEGE random generator is considered reasonable but not good. Please do not base your full entropy on this.
