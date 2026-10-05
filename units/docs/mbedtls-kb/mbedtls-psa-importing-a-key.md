---
id: "mbedtls-psa-importing-a-key"
type: "concept"
domain: "security"
title: "psa: Using PSA / Importing a key"
summary: "To use a key for cryptography operations in PSA, you need to first import it. The import operation returns the identifier of the key for use with other function calls."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:getting_started/psa.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/getting_started/psa.md#importing-a-key"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using PSA_

To use a key for cryptography operations in PSA, you need to first
import it. The import operation returns the identifier of the key for use
with other function calls.

**Prerequisites to importing keys:**
* Initialize the library with a successful call to `psa_crypto_init()`.

This example shows how to import a key:
```C
void import_a_key(const uint8_t *key, size_t key_len)
{
    psa_status_t status;
    psa_key_attributes_t attributes = PSA_KEY_ATTRIBUTES_INIT;
    psa_key_id_t key_id;

    printf("Import an AES key...\t");
    fflush(stdout);

    /* Initialize PSA Crypto */
    status = psa_crypto_init();
    if (status != PSA_SUCCESS) {
        printf("Failed to initialize PSA Crypto\n");
        return;
    }

    /* Set key attributes */
    psa_set_key_usage_flags(&attributes, 0);
    psa_set_key_algorithm(&attributes, 0);
    psa_set_key_type(&attributes, PSA_KEY_TYPE_AES);
    psa_set_key_bits(&attributes, 128);

    /* Import the key */
    status = psa_import_key(&attributes, key, key_len, &key_id);
    if (status != PSA_SUCCESS) {
        printf("Failed to import key\n");
        return;
    }
    printf("Imported a key\n");

    /* Free the attributes */
    psa_reset_key_attributes(&attributes);

    /* Destroy the key */
    psa_destroy_key(key_id);

    mbedtls_psa_crypto_free();
}
```
