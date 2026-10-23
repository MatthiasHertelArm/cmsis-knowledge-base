---
id: "mbedtls-random-data-generation-setting-up-the-entropy-source"
type: "concept"
domain: "security"
title: "Random data generation: Setting up the entropy source"
summary: "Mbed TLS includes the entropy collection module to provide a central pool of entropy from which to extract entropy."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-a-random-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-a-random-generator.md#setting-up-the-entropy-source"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS includes the [entropy collection module](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/entropy-source-code.html) to provide a central pool of entropy from which to extract entropy.

To use the entropy collector in your code, include the header file:

```
#include "mbedtls/entropy.h"
```

Add the following somewhere in your `main()`:

```c
    mbedtls_entropy_context entropy;
    mbedtls_entropy_init( &entropy );
```

If your platform has a hardware TRNG or PRNG in the processor or TPM, you can hook it up to the entropy collector with `entropy_add_source()` to enhance the entropy even further. Please see our article on [how to add an entropy source to the entropy pool](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-entropy-sources-to-entropy-pool.md) for more information.
