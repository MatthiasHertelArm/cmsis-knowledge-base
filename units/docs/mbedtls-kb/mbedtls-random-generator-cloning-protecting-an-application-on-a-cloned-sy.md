---
id: "mbedtls-random-generator-cloning-protecting-an-application-on-a-cloned-sy"
type: "concept"
domain: "security"
title: "random generator cloning: Protecting an application on a cloned system"
summary: "This section discusses how to protect the random generator in an application that runs on a cloned system, for example in a cloned virtual machine or as part of a hibernation image that can be resumed multiple times."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/random_generator_cloning.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/random_generator_cloning.md#protecting-an-application-on-a-cloned-system"
license: "Apache-2.0"
mode: "V"
---

This section discusses how to protect the random generator in an application that runs on a cloned system, for example in a cloned virtual machine or as part of a hibernation image that can be resumed multiple times.

To give each instance of the application a distinct random generator state, you need to reseed the random generator after cloning. This section discusses how to do it.

Note that additional considerations apply in configurations where the only entropy source is a nonvolatile seed. See “[Cloning with only a nonvolatile seed](#cloning-with-only-a-nonvolatile-seed)”.

### Reseeding the PSA random generator with modern library versions

In Mbed TLS 3.6.6 and later 3.6.x version, in TF-PSA-Crypto 1.1.0 and later versions, and in Mbed TLS 4.1.0 and later versions, the API includes functions to protect the [PSA random generator](#psa-random-generator) from cloning events. You can use one of the following methods:

* [`psa_random_reseed()`](https://mbed-tls.readthedocs.io/projects/api/en/development/api/group/group__psa__rng.html#ga89ab88e6bf0f001e8392f001145c4ef6) reseeds the random generator immediately. Call this function after cloning, before any use of the random generator.
* [`psa_random_deplete()`](https://mbed-tls.readthedocs.io/projects/api/en/development/api/group/group__psa__rng.html#gaf3195d46644616a257c41e2018ae4ed0) forces the random generator to reseed the next time it is used. Call this function before cloning, and ensure that the random generator is not used until after cloning.
* [`psa_random_set_prediction_resistance()`](https://mbed-tls.readthedocs.io/projects/api/en/development/api/group/group__psa__rng.html#ga16531bdabd1335c75e80167a7e086a68) enables or disables prediction resistance. When prediction resistance is enabled, the random generator reseeds on every use. Enable prediction resistance before cloning, and if desired, disable it after calling the random generator at least once after cloning.

### Protecting the PSA random generator with older library versions

TF-PSA-Crypto 1.0.0, Mbed TLS 4.0.0, and versions of Mbed TLS up to 3.6.5, do not offer APIs to control the reseeding of the [PSA random generator](#psa-random-generator). (If you obtain Mbed TLS from an operating system distribution package, it may have backported these functions — consult the package documentation.)

Here are some workarounds that you can use if your application uses PSA (either directly, or indirectly via TLS 1.3, or indirectly when `MBEDTLS_USE_PSA_CRYPTO` is enabled).

* The simplest approach, if doable, is to deinstantiate the PSA subsystem with `mbedtls_psa_crypto_free()` before cloning, and reinstantiate it with `psa_crypto_init()` after cloning. Note that this destroys all keys in the parent except persistent keys.
* If you configure the library for prediction resistance (see “[Automatic reseeding through prediction resistance](#automatic-reseeding-through-prediction-resistance)”), your application is protected.

### Reseeding a legacy random generator

If your application instantiates a [legacy random generator](#legacy-random-generators) and is cloned, call `mbedtls_ctr_drbg_reseed()` or `mbedtls_hmac_drbg_reseed()` after cloning, before using the random generator.

Note that additional considerations apply in configurations where the only entropy source is a nonvolatile seed. See “[Cloning with only a nonvolatile seed](#cloning-with-only-a-nonvolatile-seed)”.

### Operating system random generator after virtual machine cloning

By default, on Windows and Unix-like platforms, Mbed TLS and TF-PSA-Crypto rely on the operating system's random generator (`getrandom()`, `/dev/urandom`, `BCryptGenRandom()`, etc.). If your application runs as part of a [virtual machine which is cloned](#virtual-machine-cloning), beware that the operating system's random generator may itself be cloned, and your application may start running before the operating system has reseeded. Reseeding inside the library before the operating system would not provide any security.
