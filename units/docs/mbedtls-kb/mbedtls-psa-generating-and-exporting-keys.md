---
id: "mbedtls-psa-generating-and-exporting-keys"
type: "concept"
domain: "security"
title: "psa: Using PSA / Generating and exporting keys"
summary: "The PSA Crypto API provides a simple way to generate a key or key pair."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/getting_started/psa.md#generating-and-exporting-keys"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

The PSA Crypto API provides a simple way to generate a key or key pair.

**Prerequisites to using key generation and export APIs:**
* Initialize the library with a successful call to `psa_crypto_init()`.

**To generate an ECDSA key:**
1. Set the desired key attributes for key generation by calling
   `psa_set_key_algorithm()` with the chosen ECDSA algorithm (such as
   `PSA_ALG_DETERMINISTIC_ECDSA(PSA_ALG_SHA_256)`). You only want to export the
   public key, not the key pair (or private key); therefore, do not
   set `PSA_KEY_USAGE_EXPORT`.
1. Generate a key by calling `psa_generate_key()`.
1. Export the generated public key by calling `psa_export_public_key()`:
```C
    enum {
        key_bits = 256,
    };
    psa_status_t status;
    size_t exported_length = 0;
    static uint8_t exported[PSA_KEY_EXPORT_ECC_PUBLIC_KEY_MAX_SIZE(key_bits)];
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    psa_key_id_t key_id;

    printf("Generate a key pair...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Generate a key */
    psa_set_key_usage_flags(&attributes, PSA_KEY_USAGE_SIGN_HASH);
    psa_set_key_algorithm(&attributes,
                          PSA_ALG_DETERMINISTIC_ECDSA(PSA_ALG_SHA_256));
    psa_set_key_type(&attributes,
                     PSA_KEY_TYPE_ECC_KEY_PAIR(PSA_ECC_FAMILY_SECP_R1));
    psa_set_key_bits(&attributes, key_bits);
    status = psa_generate_key(&attributes, &key_id);
    if (status != PSA_SUCCESS) {
        printf("Failed to generate key\n");
        return;
    }
    psa_reset_key_attributes(&attributes);

    status = psa_export_public_key(key_id, exported, sizeof(exported),
                                   &exported_length);
    if (status != PSA_SUCCESS) {
        printf("Failed to export public key %ld\n", status);
        return;
    }

    printf("Exported a public key\n");

    /* Destroy the key */
    psa_destroy_key(key_id);

    mbedtls_psa_crypto_free();
```
