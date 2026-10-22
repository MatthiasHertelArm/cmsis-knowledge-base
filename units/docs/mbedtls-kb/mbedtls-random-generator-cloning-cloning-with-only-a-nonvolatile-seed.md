---
id: "mbedtls-random-generator-cloning-cloning-with-only-a-nonvolatile-seed"
type: "concept"
domain: "security"
title: "random generator cloning: Cloning with only a nonvolatile seed"
summary: "A nonvolatile seed (NV seed) is a file that contains entropy which is generated during the provisioning of a device, and is updated on each boot. This is a fallback mechanism for devices that lack an actual entropy source."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/random_generator_cloning.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/random_generator_cloning.md#cloning-with-only-a-nonvolatile-seed"
license: "Apache-2.0"
mode: "V"
---

### What is a nonvolatile seed?

A [nonvolatile seed](https://mbed-tls.readthedocs.io/en/latest/kb/how-to/how_to_integrate_nv_seed/) (NV seed) is a file that contains entropy which is generated during the provisioning of a device, and is updated on each boot. This is a fallback mechanism for devices that lack an actual entropy source. Note that although the nonvolatile seed is considered an entropy source in the API documentation, it does not have the same security properties. Thus applications that are secure in configurations with an actual entropy source may be insecure in configurations where only a nonvolatile seed is available.

In Mbed TLS 2.x or 3.x, a configuration uses only a nonvolatile seed if `MBEDTLS_ENTROPY_NV_SEED` and `MBEDTLS_NO_PLATFORM_ENTROPY` are enabled, but `MBEDTLS_ENTROPY_HARDWARE_ALT` is not enabled. Since TF-PSA-Crypto 1.0.0, a configuration without actual entropy sources must enable `MBEDTLS_ENTROPY_NO_SOURCES_OK`.

### Sharing the nonvolatile seed

The nonvolatile seed is stored in a file. This file is updated during the initial seeding of the [PSA random generator](#psa-random-generator), and during the initial seeding of any entropy object used for a [legacy random generator](#legacy-random-generators). Note that the seed file is not modified when reseeding.

Thus, merely reseeding is not sufficient to protect the random generator when using only a nonvolatile seed.

### Nonvolatile seed and forking

In an application that calls `fork()`, the parent and the child read the same seed file. Hence, reseeding the random generator in both processes would merely move both of them to the same new state. To avoid this, use different personalization strings when reseeding (`additional` parameter to `mbedtls_ctr_drbg_reseed()`, `additional` parameter to `mbedtls_hmac_drbg_reseed()`, or `perso` parameter to `psa_random_reseed()`).

If you only reseed in the child process but not in the parent parent process, or vice versa, then the two processes do end up in different states. However, beware that a compromise of the non-reseeded process may allow the attacker to find out the random generator state in the reseeded process. Also, identical reseeding sequences would lead to identical states: in particular, reseeding only in the child process after `fork()` is insecure in general, since multiple children may end up with the same state.

### Cloning a system with a nonvolatile seed

If the whole system is cloned including the seed file, you can give each instance its own random generator state by reseeding the random generator with distinct values for the personalization string (`additional` parameter to `mbedtls_ctr_drbg_reseed()`, `additional` parameter to `mbedtls_hmac_drbg_reseed()`, or `perso` parameter to `psa_random_reseed()`). For example:

* If each clone has a globally unique identifier, include that identifier in the additional data when reseeding in the clone. Note that the identifier must be unique in both time and space. For example, a process ID is insufficient since most operating systems reuse process ID values after a while.
* If the original instance produces a single clone at a time, systematically reseed before creating the next clone.
