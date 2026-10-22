---
id: "mbedtls-psa-authenticating-and-encrypting-or-decrypt"
type: "concept"
domain: "security"
title: "psa: Using PSA / Authenticating and encrypting or decrypting a message"
summary: "The PSA Crypto API provides a simple way to authenticate and encrypt with associated data (AEAD), supporting the PSA_ALG_CCM algorithm."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/getting_started/psa.md#authenticating-and-encrypting-or-decrypting-a-message"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

The PSA Crypto API provides a simple way to authenticate and encrypt with
associated data (AEAD), supporting the `PSA_ALG_CCM` algorithm.

**Prerequisites to working with the AEAD cipher APIs:**
* Initialize the library with a successful call to `psa_crypto_init()`.
* The key attributes for the key used for derivation must have the
  `PSA_KEY_USAGE_ENCRYPT` or `PSA_KEY_USAGE_DECRYPT` usage flags.

This example shows how to authenticate and encrypt a message:
```C
    psa_status_t status;
    static const uint8_t key[] = {
        0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7,
        0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF };
    static const uint8_t nonce[] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0A, 0x0B };
    static const uint8_t additional_data[] = {
        0xEC, 0x46, 0xBB, 0x63, 0xB0, 0x25,
        0x20, 0xC3, 0x3C, 0x49, 0xFD, 0x70 };
    static const uint8_t input_data[] = {
        0xB9, 0x6B, 0x49, 0xE2, 0x1D, 0x62, 0x17, 0x41,
        0x63, 0x28, 0x75, 0xDB, 0x7F, 0x6C, 0x92, 0x43,
        0xD2, 0xD7, 0xC2 };
    uint8_t *output_data = NULL;
    size_t output_size = 0;
    size_t output_length = 0;
    size_t tag_length = 16;
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    psa_key_id_t key_id;

    printf("Authenticate encrypt...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    output_size = sizeof(input_data) + tag_length;
    output_data = (uint8_t *)malloc(output_size);
    if (!output_data) {
        printf("Out of memory\n");
        return;
    }

    /* Import a key */
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_ENCRYPT);
    psa_set_key_algorithm(&attributes, PSA_ALG_CCM);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_AES);
    psa_set_key_bits(&attributes, 128);
    status = psa_import_key(&attributes, key, sizeof(key), &key_id);
    psa_reset_key_attributes(&attributes);

    /* Authenticate and encrypt */
    status = psa_aead_encrypt(key_id, PSA_ALG_CCM,
                              nonce, sizeof(nonce),
                              additional_data, sizeof(additional_data),
                              input_data, sizeof(input_data),
                              output_data, output_size,
                              &output_length);
    if (status != PSA_SUCCESS) {
        printf("Failed to authenticate and encrypt\n");
        return;
    }

    printf("Authenticated and encrypted\n");

    /* Clean up */
    free(output_data);

    /* Destroy the key */
    psa_destroy_key(key_id);

    mbedtls_psa_crypto_free();
```

This example shows how to authenticate and decrypt a message:

```C
    psa_status_t status;
    static const uint8_t key_data[] = {
        0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7,
        0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF };
    static const uint8_t nonce[] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0A, 0x0B };
    static const uint8_t additional_data[] = {
        0xEC, 0x46, 0xBB, 0x63, 0xB0, 0x25,
        0x20, 0xC3, 0x3C, 0x49, 0xFD, 0x70 };
    static const uint8_t input_data[] = {
        0x20, 0x30, 0xE0, 0x36, 0xED, 0x09, 0xA0, 0x45, 0xAF, 0x3C, 0xBA, 0xEE,
        0x0F, 0xC8, 0x48, 0xAF, 0xCD, 0x89, 0x54, 0xF4, 0xF6, 0x3F, 0x28, 0x9A,
        0xA1, 0xDD, 0xB2, 0xB8, 0x09, 0xCD, 0x7C, 0xE1, 0x46, 0xE9, 0x98 };
    uint8_t *output_data = NULL;
    size_t output_size = 0;
    size_t output_length = 0;
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    psa_key_id_t key_id;

    printf("Authenticate decrypt...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    output_size = sizeof(input_data);
    output_data = (uint8_t *)malloc(output_size);
    if (!output_data) {
        printf("Out of memory\n");
        return;
    }

    /* Import a key */
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_DECRYPT);
    psa_set_key_algorithm(&attributes, PSA_ALG_CCM);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_AES);
    psa_set_key_bits(&attributes, 128);
    status = psa_import_key(&attributes, key_data, sizeof(key_data), &key_id);
    if (status != PSA_SUCCESS) {
        printf("Failed to import a key\n");
        return;
    }
    psa_reset_key_attributes(&attributes);

    /* Authenticate and decrypt */
    status = psa_aead_decrypt(key_id, PSA_ALG_CCM,
                              nonce, sizeof(nonce),
                              additional_data, sizeof(additional_data),
                              input_data, sizeof(input_data),
                              output_data, output_size,
                              &output_length);
    if (status != PSA_SUCCESS) {
        printf("Failed to authenticate and decrypt %ld\n", status);
        return;
    }

    printf("Authenticated and decrypted\n");

    /* Clean up */
    free(output_data);

    /* Destroy the key */
    psa_destroy_key(key_id);

    mbedtls_psa_crypto_free();
```
