---
id: "mbedtls-psa-hashing-a-message"
type: "concept"
domain: "security"
title: "psa: Using PSA / Hashing a message"
summary: "The PSA Crypto API lets you compute and verify hashes using various hashing algorithms."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/getting_started/psa.md#hashing-a-message"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

The PSA Crypto API lets you compute and verify hashes using various hashing
algorithms.

**Prerequisites to working with the hash APIs:**
* Initialize the library with a successful call to `psa_crypto_init()`.

**To calculate a hash:**
1. Allocate an operation structure (`psa_hash_operation_t`) to pass to the hash
   functions.
1. Initialize the operation structure to zero or to `PSA_HASH_OPERATION_INIT`.
1. Call `psa_hash_setup()` to specify the hash algorithm.
1. Call `psa_hash_update()` with the message to encrypt. You may call this
   function multiple times, passing successive fragments of the message on
   successive calls.
1. Call `psa_hash_finish()` to calculate the hash, or `psa_hash_verify()` to
   compare the computed hash with an expected hash value.

This example shows how to calculate the SHA-256 hash of a message:
```c
    psa_status_t status;
    psa_algorithm_t alg = PSA_ALG_SHA_256;
    psa_hash_operation_t operation = PSA_HASH_OPERATION_INIT;
    unsigned char input[] = { 'a', 'b', 'c' };
    unsigned char actual_hash[PSA_HASH_MAX_SIZE];
    size_t actual_hash_len;

    printf("Hash a message...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Compute hash of message  */
    status = psa_hash_setup(&operation, alg);
    if (status != PSA_SUCCESS) {
        printf("Failed to begin hash operation\n");
        return;
    }
    status = psa_hash_update(&operation, input, sizeof(input));
    if (status != PSA_SUCCESS) {
        printf("Failed to update hash operation\n");
        return;
    }
    status = psa_hash_finish(&operation, actual_hash, sizeof(actual_hash),
                             &actual_hash_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to finish hash operation\n");
        return;
    }

    printf("Hashed a message\n");

    /* Clean up hash operation context */
    psa_hash_abort(&operation);

    mbedtls_psa_crypto_free();
```

This example shows how to verify the SHA-256 hash of a message:
```c
    psa_status_t status;
    psa_algorithm_t alg = PSA_ALG_SHA_256;
    psa_hash_operation_t operation = PSA_HASH_OPERATION_INIT;
    unsigned char input[] = { 'a', 'b', 'c' };
    unsigned char expected_hash[] = {
        0xba, 0x78, 0x16, 0xbf, 0x8f, 0x01, 0xcf, 0xea, 0x41, 0x41, 0x40, 0xde,
        0x5d, 0xae, 0x22, 0x23, 0xb0, 0x03, 0x61, 0xa3, 0x96, 0x17, 0x7a, 0x9c,
        0xb4, 0x10, 0xff, 0x61, 0xf2, 0x00, 0x15, 0xad
    };
    size_t expected_hash_len = PSA_HASH_LENGTH(alg);

    printf("Verify a hash...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Verify message hash */
    status = psa_hash_setup(&operation, alg);
    if (status != PSA_SUCCESS) {
        printf("Failed to begin hash operation\n");
        return;
    }
    status = psa_hash_update(&operation, input, sizeof(input));
    if (status != PSA_SUCCESS) {
        printf("Failed to update hash operation\n");
        return;
    }
    status = psa_hash_verify(&operation, expected_hash, expected_hash_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to verify hash\n");
        return;
    }

    printf("Verified a hash\n");

    /* Clean up hash operation context */
    psa_hash_abort(&operation);

    mbedtls_psa_crypto_free();
```

The API provides the macro `PSA_HASH_LENGTH`, which returns the expected hash
length (in bytes) for the specified algorithm.

#### Handling hash operation contexts

After a successful call to `psa_hash_setup()`, you can terminate the operation
at any time by calling `psa_hash_abort()`. The call to `psa_hash_abort()` frees
any resources associated with the operation, except for the operation structure
itself.

The PSA Crypto API implicitly calls `psa_hash_abort()` when:
1. A call to `psa_hash_update()` fails (returning any status other than
   `PSA_SUCCESS`).
1. A call to `psa_hash_finish()` succeeds or fails.
1. A call to `psa_hash_verify()` succeeds or fails.

After an implicit or explicit call to `psa_hash_abort()`, the operation
structure is invalidated; in other words, you cannot reuse the operation
structure for the same operation. You can, however, reuse the operation
structure for a different operation by calling `psa_hash_setup()` again.

You must call `psa_hash_abort()` at some point for any operation that is
initialized successfully (by a successful call to `psa_hash_setup()`) .

Making multiple sequential calls to `psa_hash_abort()` on an operation that has
already been terminated (either implicitly or explicitly) is safe and has no
effect.
