---
id: "mbedtls-random-data-generation-enabling-prediction-resistance"
type: "concept"
domain: "security"
title: "Random data generation: Enabling prediction resistance"
summary: "To prevent an adversary from reading your random data, you can enable prediction resistance:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/add-a-random-generator.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/add-a-random-generator.md#enabling-prediction-resistance"
license: "Apache-2.0"
mode: "V"
---

To prevent an adversary from reading your random data, you can enable prediction resistance:

```c
mbedtls_ctr_drbg_set_prediction_resistance( &ctr_drbg, MBEDTLS_CTR_DRBG_PR_ON );
```

**Note:** If enabled, entropy is gathered before each call. Only use this if you have ample supply of good entropy.
