---
id: "mbedtls-random-generator-cloning-automatic-reseeding-through-prediction-r"
type: "concept"
domain: "security"
title: "random generator cloning: Automatic reseeding through prediction resistance"
summary: "If the random generator has prediction resistance, it will automatically reseed every time it is used, so cloning does not require any special handling. You can enable prediction resistance in any of the following ways:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/random_generator_cloning.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/random_generator_cloning.md#automatic-reseeding-through-prediction-resistance"
license: "Apache-2.0"
mode: "V"
---

If the random generator has prediction resistance, it will automatically reseed every time it is used, so cloning does not require any special handling. You can enable prediction resistance in any of the following ways:

* Since TF-PSA-Crypto 1.0, you can enable prediction resistance at compile time by setting the reseed internal `MBEDTLS_PSA_RNG_RESEED_INTERVAL` to 1.
* Since TF-PSA-Crypto 1.1.0, you can enable prediction resistance at run time by calling `psa_random_set_prediction_resistance()`. This function is also available for the PSA random generator in Mbed TLS 3.6.x since version 3.6.6.
* In Mbed TLS 3.x, you can enable prediction resistance at compile time by setting the reseed interval (`MBEDTLS_CTR_DRBG_RESEED_INTERVAL` or `MBEDTLS_HMAC_DRBG_RESEED_INTERVAL`) to 1.
* In the Mbed TLS legacy API up to Mbed TLS 3.x, you can enable prediction resistance by calling `mbedtls_ctr_drbg_set_prediction_resistance()` or `mbedtls_hmac_drbg_set_prediction_resistance()` either when setting up the DRBG context, or on an active DRBG context.

Note that prediction resistance requires an actual entropy source. If the system only has a nonvolatile seed, as discussed in [“Reseeding with only a nonvolatile seed”](#reseeding-with-only-a-nonvolatile-seed), then prediction resistance in the DRBG is not sufficient in general to handle cloning securely.
