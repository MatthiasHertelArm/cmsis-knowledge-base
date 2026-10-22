---
id: "mbedtls-why-to-add-an-entropy-source-seed-files"
type: "concept"
domain: "security"
title: "Why to add an entropy source: Seed files"
summary: "In addition to platform specific sources, such as timing of network packets, keyboard input and so on, you can also use a seed file to produce entropy for your system."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-entropy-sources-to-entropy-pool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-entropy-sources-to-entropy-pool.md#seed-files"
license: "Apache-2.0"
mode: "V"
---

In addition to platform specific sources, such as timing of network packets, keyboard input and so on, you can also use a seed file to produce entropy for your system. The advantage of a seed file is that you can generate it on a high-entropy system and then update and use it on your low-entropy system. 

**Note:** You must make sure the seed file is unique for each device.

<!---add-entropy-sources-to-entropy-pool
,"Good entropy is the fundamental basis for good cryptography and SSL or TLS. This article shows how to add nonstandard sources to the Mbed TLS entropy collector",,"entropy, entropy pool, entropy collection, windows, unix, random, entropy source, security",published,"2013-09-10 11:55:00",2,10679,"2015-07-24 11:48:00","Paul Bakker"--->
