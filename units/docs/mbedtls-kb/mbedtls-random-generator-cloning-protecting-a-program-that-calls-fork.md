---
id: "mbedtls-random-generator-cloning-protecting-a-program-that-calls-fork"
type: "concept"
domain: "security"
title: "random generator cloning: Protecting a program that calls `fork()`"
summary: "In Mbed TLS 3.6.6 and later 3.6.x version, in TF-PSA-Crypto 1.1.0 and later versions, and in Mbed TLS 4.1.0 and later versions, the library automatically protects the PSA random generator from the fork() system call on Unix-like platforms, …"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/random_generator_cloning.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/random_generator_cloning.md#protecting-a-program-that-calls-fork"
license: "Apache-2.0"
mode: "V"
---

### Automatic fork protection for PSA in modern library versions

In Mbed TLS 3.6.6 and later 3.6.x version, in TF-PSA-Crypto 1.1.0 and later versions, and in Mbed TLS 4.1.0 and later versions, the library automatically protects the [PSA random generator](#psa-random-generator) from the `fork()` system call on Unix-like platforms, except in a few edge cases discussed below. So applications using `fork()` and using only PSA APIs do not need to do anything, as long as they use a sufficiently recent library version.

Since TF-PSA-Crypto 1.1.0 (and Mbed TLS 3.6.6 for the 3.6 long-time support branch), the library uses an approach that is similar to the one [introduced in OpenSSL 0.9.5](https://github.com/openssl/openssl/commit/c1e744b9125a883450c2239ec55ea606c618a5c0) and in use since [OpenSSL 3.0.0](https://github.com/openssl/openssl/blob/openssl-3.6.0/providers/implementations/rands/drbg.c#L673): force a reseed if a process ID change is detected. This protection generally ensures that the parent and the child process will have unique RNG states. There are rare edge cases where forking can happen without a PID change, such as:

- If the child forks another process before invoking the random generator, but after the original process has died. In this case, it is rare but possible for the grandchild to have the same PID as the original process.
- When using the Linux `clone()` system call with the `CLONE_NEWPID` flag to put the child process in its own PID namespace, and the original process has PID 1.
- When the child is moved to a new or existing PID namespace before any call to the PSA random generator, and the PID in the child's namespace might match the PID of the original process.
- When using the Linux `clone3()` system call with a `set_tid` array to force the PID of the new process.

If your application might be concerned by these edge cases, you will need to treat forking as an external cloning event, as discussed in “[Protecting an application on a cloned system](#protecting-an-application-on-a-cloned-system)”.

### Protecting the PSA random generator with older library versions

TF-PSA-Crypto 1.0.0, Mbed TLS 4.0.0, and versions of Mbed TLS up to 3.6.5, do not protect the [PSA random generator](#psa-random-generator) against `fork()`. (If you obtain Mbed TLS from an operating system distribution package, it may have backported the fix — consult the package documentation.)

Here are some workarounds that you can use if your application uses PSA (either directly, or indirectly via TLS 1.3, or indirectly when `MBEDTLS_USE_PSA_CRYPTO` is enabled).

* If you instantiate the PSA subsystem with `psa_crypto_init()` only in the child process, i.e. if you never call `fork()` after `psa_crypto_init()`, then each child process gets an independent PSA random generator, and there is no problem.
* If a child does not use crypto APIs (for example, if a child only calls a few system functions and then `execve()`), the temporary existence of the PSA random generator in the child is irrelevant, and you do not need any special precautions.
* If you need the PSA subsystem in both the parent and the child, call `mbedtls_psa_crypto_free()` before forking and `psa_crypto_init()` after forking. Note that this destroys all keys in the parent except persistent keys.
* If you configure the library for prediction resistance (see “[Automatic reseeding through prediction resistance](#automatic-reseeding-through-prediction-resistance)”), your application is protected.

### Handling random generator objects in a forking program

If your application instantiates a [legacy random generator](#legacy-random-generators) in a parent process and uses them in a child created by `fork()`, you must reseed the random generator after forking, before using it. Call `mbedtls_ctr_drbg_reseed()` or `mbedtls_hmac_drbg_reseed()` in both the parent process and the child process, before using the random generator.

Note that additional considerations apply in configurations where the only entropy source is a nonvolatile seed. See “[Cloning with only a nonvolatile seed](#cloning-with-only-a-nonvolatile-seed)”.
