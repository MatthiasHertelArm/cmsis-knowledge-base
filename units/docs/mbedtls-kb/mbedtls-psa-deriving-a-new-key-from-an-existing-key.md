---
id: "mbedtls-psa-deriving-a-new-key-from-an-existing-key"
type: "concept"
domain: "security"
title: "psa: Using PSA / Deriving a new key from an existing key"
summary: "The PSA Crypto API provides a key derivation API that lets you derive new keys from existing ones."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/getting_started/psa.md#deriving-a-new-key-from-an-existing-key"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

The PSA Crypto API provides a key derivation API that lets you derive new keys
from existing ones. The key derivation API has functions to take inputs,
including other keys and data, and functions to generate outputs, such as
new keys or other data.

You must first initialize and set up a key derivation context,
provided with a key and, optionally, other data. Then, use the key derivation
context to either read derived data to a buffer or send derived data directly
to a key slot.

See the documentation for the particular algorithm (such as HKDF or the
TLS 1.2 PRF) for information about which inputs to pass when, and when you can
obtain which outputs.

**Prerequisites to working with the key derivation APIs:**
* Initialize the library with a successful call to `psa_crypto_init()`.
* Use a key with the appropriate attributes set:
    * Usage flags set for key derivation (`PSA_KEY_USAGE_DERIVE`)
    * Key type set to `PSA_KEY_TYPE_DERIVE`.
    * Algorithm set to a key derivation algorithm
      (for example, `PSA_ALG_HKDF(PSA_ALG_SHA_256)`).

**To derive a new AES-CTR 128-bit encryption key into a given key slot using HKDF
with a given key, salt and info:**

1. Set up the key derivation context using the `psa_key_derivation_setup()`
function, specifying the derivation algorithm `PSA_ALG_HKDF(PSA_ALG_SHA_256)`.
1. Provide an optional salt with `psa_key_derivation_input_bytes()`.
1. Provide info with `psa_key_derivation_input_bytes()`.
1. Provide a secret with `psa_key_derivation_input_key()`, referencing a key
   that can be used for key derivation.
1. Set the key attributes desired for the new derived key. We'll set
   the `PSA_KEY_USAGE_ENCRYPT` usage flag and the `PSA_ALG_CTR` algorithm for
   this example.
1. Derive the key by calling `psa_key_derivation_output_key()`.
1. Clean up the key derivation context.

At this point, the derived key slot holds a new 128-bit AES-CTR encryption key
derived from the key, salt and info provided:
```C
    psa_status_t status;
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    static const unsigned char key[] = {
        0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b,
        0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b,
        0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b,
        0x0b };
    static const unsigned char salt[] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06,
        0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c };
    static const unsigned char info[] = {
        0xf0, 0xf1, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6,
        0xf7, 0xf8, 0xf9 };
    psa_algorithm_t alg = PSA_ALG_HKDF(PSA_ALG_SHA_256);
    psa_key_derivation_operation_t operation =
        PSA_KEY_DERIVATION_OPERATION_INIT;
    size_t derived_bits = 128;
    size_t capacity = PSA_BITS_TO_BYTES(derived_bits);
    psa_key_id_t base_key;
    psa_key_id_t derived_key;

    printf("Derive a key (HKDF)...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Import a key for use in key derivation. If such a key has already been
     * generated or imported, you can skip this part. */
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_DERIVE);
    psa_set_key_algorithm(&attributes, alg);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_DERIVE);
    status = psa_import_key(&attributes, key, sizeof(key), &base_key);
    if (status != PSA_SUCCESS) {
        printf("Failed to import a key\n");
        return;
    }
    psa_reset_key_attributes(&attributes);

    /* Derive a key */
    status = psa_key_derivation_setup(&operation, alg);
    if (status != PSA_SUCCESS) {
        printf("Failed to begin key derivation\n");
        return;
    }
    status = psa_key_derivation_set_capacity(&operation, capacity);
    if (status != PSA_SUCCESS) {
        printf("Failed to set capacity\n");
        return;
    }
    status = psa_key_derivation_input_bytes(&operation,
                                            PSA_KEY_DERIVATION_INPUT_SALT,
                                            salt, sizeof(salt));
    if (status != PSA_SUCCESS) {
        printf("Failed to input salt (extract)\n");
        return;
    }
    status = psa_key_derivation_input_key(&operation,
                                          PSA_KEY_DERIVATION_INPUT_SECRET,
                                          base_key);
    if (status != PSA_SUCCESS) {
        printf("Failed to input key (extract)\n");
        return;
    }
    status = psa_key_derivation_input_bytes(&operation,
                                            PSA_KEY_DERIVATION_INPUT_INFO,
                                            info, sizeof(info));
    if (status != PSA_SUCCESS) {
        printf("Failed to input info (expand)\n");
        return;
    }
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_ENCRYPT);
    psa_set_key_algorithm(&attributes, PSA_ALG_CTR);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_AES);
    psa_set_key_bits(&attributes, 128);
    status = psa_key_derivation_output_key(&attributes, &operation,
                                           &derived_key);
    if (status != PSA_SUCCESS) {
        printf("Failed to derive key\n");
        return;
    }
    psa_reset_key_attributes(&attributes);

    printf("Derived key\n");

    /* Clean up key derivation operation */
    psa_key_derivation_abort(&operation);

    /* Destroy the keys */
    psa_destroy_key(derived_key);
    psa_destroy_key(base_key);

    mbedtls_psa_crypto_free();
```
