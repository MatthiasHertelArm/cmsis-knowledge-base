---
id: "mbedtls-why-to-add-an-entropy-source-adding-own-sources"
type: "concept"
domain: "security"
title: "Why to add an entropy source: Adding own sources"
summary: "When you run Mbed TLS on a different platform, such as an embedded platform, you have to add platform-specific or application-specific entropy sources."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/add-entropy-sources-to-entropy-pool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/add-entropy-sources-to-entropy-pool.md#adding-own-sources"
license: "Apache-2.0"
mode: "V"
---

When you run Mbed TLS on a different platform, such as an embedded platform, you have to add platform-specific or application-specific entropy sources.

To add a source to the entropy collector, you can use `mbedtls_entropy_add_source()`. It requires you to provide a callback (`f_source`) that you can call whenever the entropy pool tries to gather entropy, the data (`p_source`) that you need with your callback and a `threshold`. This threshold indicates the minimum number of bytes the entropy pool should wait on from this callback before releasing entropy. Choose this value wisely. Choosing a value that is higher than your callback can provide will block entropy collection.

Starting with the 2.0 branch, you also need to indicate if this source is strong or not. For example, **/dev/urandom** and `CryptGenRandom()` are strong. Hardware RNG is a strong source if your platform has it, but the `mbedtls_timing_hardclock()` value and HAVEGE are weak. The entropy module refuses to deliver entropy unless it has at least one strong source.
