---
id: "mbedtls-psa-using-symmetric-ciphers"
type: "concept"
domain: "security"
title: "psa: Using PSA / Using symmetric ciphers"
summary: "The PSA Crypto API supports encrypting and decrypting messages using various symmetric cipher algorithms (both block and stream ciphers)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/getting_started/psa.md#using-symmetric-ciphers"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

The PSA Crypto API supports encrypting and decrypting messages using various
symmetric cipher algorithms (both block and stream ciphers).

**Prerequisites to working with the symmetric cipher API:**
* Initialize the library with a successful call to `psa_crypto_init()`.
* Have a symmetric key. This key's usage flags must include
  `PSA_KEY_USAGE_ENCRYPT` to allow encryption or `PSA_KEY_USAGE_DECRYPT` to
  allow decryption.

**To encrypt a message with a symmetric cipher:**
1. Allocate an operation (`psa_cipher_operation_t`) structure to pass to the
   cipher functions.
1. Initialize the operation structure to zero or to `PSA_CIPHER_OPERATION_INIT`.
1. Call `psa_cipher_encrypt_setup()` to specify the algorithm and the key to be
   used.
1. Call either `psa_cipher_generate_iv()` or `psa_cipher_set_iv()` to generate
   or set the initialization vector (IV). We recommend calling
   `psa_cipher_generate_iv()`, unless you require a specific IV value.
1. Call `psa_cipher_update()` with the message to encrypt. You may call this
   function multiple times, passing successive fragments of the message on
   successive calls.
1. Call `psa_cipher_finish()` to end the operation and output the encrypted
   message.

This example shows how to encrypt data using an AES (Advanced Encryption
Standard) key in CBC (Cipher Block Chaining) mode with no padding (assuming all
prerequisites have been fulfilled):
```c
void encrypt_with_symmetric_ciphers(const uint8_t *key, size_t key_len)
{
    enum {
        block_size = PSA_BLOCK_CIPHER_BLOCK_LENGTH(PSA_KEY_TYPE_AES),
    };
    psa_status_t status;
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    psa_algorithm_t alg = PSA_ALG_CBC_NO_PADDING;
    uint8_t plaintext[block_size] = SOME_PLAINTEXT;
    uint8_t iv[block_size];
    size_t iv_len;
    uint8_t output[block_size];
    size_t output_len;
    psa_key_id_t key_id;
    psa_cipher_operation_t operation = PSA_CIPHER_OPERATION_INIT;

    printf("Encrypt with cipher...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS)
    {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Import a key */
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_ENCRYPT);
    psa_set_key_algorithm(&attributes, alg);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_AES);
    psa_set_key_bits(&attributes, 128);
    status = psa_import_key(&attributes, key, key_len, &key_id);
    if (status != PSA_SUCCESS) {
        printf("Failed to import a key\n");
        return;
    }
    psa_reset_key_attributes(&attributes);

    /* Encrypt the plaintext */
    status = psa_cipher_encrypt_setup(&operation, key_id, alg);
    if (status != PSA_SUCCESS) {
        printf("Failed to begin cipher operation\n");
        return;
    }
    status = psa_cipher_generate_iv(&operation, iv, sizeof(iv), &iv_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to generate IV\n");
        return;
    }
    status = psa_cipher_update(&operation, plaintext, sizeof(plaintext),
                               output, sizeof(output), &output_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to update cipher operation\n");
        return;
    }
    status = psa_cipher_finish(&operation, output + output_len,
                               sizeof(output) - output_len, &output_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to finish cipher operation\n");
        return;
    }
    printf("Encrypted plaintext\n");

    /* Clean up cipher operation context */
    psa_cipher_abort(&operation);

    /* Destroy the key */
    psa_destroy_key(key_id);

    mbedtls_psa_crypto_free();
}
```

**To decrypt a message with a symmetric cipher:**
1. Allocate an operation (`psa_cipher_operation_t`) structure to pass to the
   cipher functions.
1. Initialize the operation structure to zero or to `PSA_CIPHER_OPERATION_INIT`.
1. Call `psa_cipher_decrypt_setup()` to specify the algorithm and the key to be
   used.
1. Call `psa_cipher_set_iv()` with the IV for the decryption.
1. Call `psa_cipher_update()` with the message to encrypt. You may call this
   function multiple times, passing successive fragments of the message on
   successive calls.
1. Call `psa_cipher_finish()` to end the operation and output the decrypted
   message.

This example shows how to decrypt encrypted data using an AES key in CBC mode
with no padding (assuming all prerequisites have been fulfilled):
```c
void decrypt_with_symmetric_ciphers(const uint8_t *key, size_t key_len)
{
    enum {
        block_size = PSA_BLOCK_CIPHER_BLOCK_LENGTH(PSA_KEY_TYPE_AES),
    };
    psa_status_t status;
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    psa_algorithm_t alg = PSA_ALG_CBC_NO_PADDING;
    psa_cipher_operation_t operation = PSA_CIPHER_OPERATION_INIT;
    uint8_t ciphertext[block_size] = SOME_CIPHERTEXT;
    uint8_t iv[block_size] = ENCRYPTED_WITH_IV;
    uint8_t output[block_size];
    size_t output_len;
    psa_key_id_t key_id;

    printf("Decrypt with cipher...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS)
    {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Import a key */
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_DECRYPT);
    psa_set_key_algorithm(&attributes, alg);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_AES);
    psa_set_key_bits(&attributes, 128);
    status = psa_import_key(&attributes, key, key_len, &key_id);
    if (status != PSA_SUCCESS) {
        printf("Failed to import a key\n");
        return;
    }
    psa_reset_key_attributes(&attributes);

    /* Decrypt the ciphertext */
    status = psa_cipher_decrypt_setup(&operation, key_id, alg);
    if (status != PSA_SUCCESS) {
        printf("Failed to begin cipher operation\n");
        return;
    }
    status = psa_cipher_set_iv(&operation, iv, sizeof(iv));
    if (status != PSA_SUCCESS) {
        printf("Failed to set IV\n");
        return;
    }
    status = psa_cipher_update(&operation, ciphertext, sizeof(ciphertext),
                               output, sizeof(output), &output_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to update cipher operation\n");
        return;
    }
    status = psa_cipher_finish(&operation, output + output_len,
                               sizeof(output) - output_len, &output_len);
    if (status != PSA_SUCCESS) {
        printf("Failed to finish cipher operation\n");
        return;
    }
    printf("Decrypted ciphertext\n");

    /* Clean up cipher operation context */
    psa_cipher_abort(&operation);

    /* Destroy the key */
    psa_destroy_key(key_id);

    mbedtls_psa_crypto_free();
}
```

#### Handling cipher operation contexts

After you've initialized the operation structure with a successful call to
`psa_cipher_encrypt_setup()` or `psa_cipher_decrypt_setup()`, you can terminate
the operation at any time by calling `psa_cipher_abort()`.

The call to `psa_cipher_abort()` frees any resources associated with the
operation, except for the operation structure itself.

The PSA Crypto API implicitly calls `psa_cipher_abort()` when:
* A call to `psa_cipher_generate_iv()`, `psa_cipher_set_iv()` or
  `psa_cipher_update()` fails (returning any status other than `PSA_SUCCESS`).
* A call to `psa_cipher_finish()` succeeds or fails.

After an implicit or explicit call to `psa_cipher_abort()`, the operation
structure is invalidated; in other words, you cannot reuse the operation
structure for the same operation. You can, however, reuse the operation
structure for a different operation by calling either
`psa_cipher_encrypt_setup()` or `psa_cipher_decrypt_setup()` again.

You must call `psa_cipher_abort()` at some point for any operation that is
initialized successfully (by a successful call to `psa_cipher_encrypt_setup()`
or `psa_cipher_decrypt_setup()`).

Making multiple sequential calls to `psa_cipher_abort()` on an operation that
is terminated (either implicitly or explicitly) is safe and has no effect.
