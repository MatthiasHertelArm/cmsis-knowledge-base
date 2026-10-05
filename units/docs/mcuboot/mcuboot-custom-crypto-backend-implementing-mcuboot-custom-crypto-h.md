---
id: "mcuboot-custom-crypto-backend-implementing-mcuboot-custom-crypto-h"
type: "concept"
domain: "boot-update"
title: "Custom Crypto Backend: Implementing `mcuboot_custom_crypto.h`"
summary: "Your custom crypto header must define the context types and functions before any bootutil crypto headers are included."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/custom_crypto.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/custom_crypto.md#implementing-mcuboot-custom-crypto-h"
license: "Apache-2.0"
mode: "V"
---

Your custom crypto header must define the context types and functions before
any bootutil crypto headers are included. The sections below cover the symbols
required by each MCUboot feature; if a required symbol is missing, the
compiler will fail at the first use.

### Required always: image hash

MCUboot uses the `bootutil_sha_*` interface for image hashing. Your custom
implementation must match the hash algorithm selected by your MCUboot
configuration.

```c
/* Context type */
typedef <your_sha_ctx_type> bootutil_sha_context;

static inline int bootutil_sha_init(bootutil_sha_context *ctx);
static inline int bootutil_sha_drop(bootutil_sha_context *ctx);
static inline int bootutil_sha_update(bootutil_sha_context *ctx,
                                      const void *data, uint32_t data_len);
static inline int bootutil_sha_finish(bootutil_sha_context *ctx,
                                      uint8_t *output);
```

### Required for signature verification: ECDSA

Your custom ECDSA implementation must match the curve selected by your
MCUboot signing configuration. For `MCUBOOT_SIGN_EC256`, implement P-256.
For `MCUBOOT_SIGN_EC384`, implement P-384, including parsing `secp384r1`
public keys and verifying signatures against the selected hash.

```c
/* Context type */
typedef <your_ecdsa_ctx_type> bootutil_ecdsa_context;

static inline void bootutil_ecdsa_init(bootutil_ecdsa_context *ctx);
static inline void bootutil_ecdsa_drop(bootutil_ecdsa_context *ctx);

/* Parse the SubjectPublicKeyInfo blob; advance *cp past the wrapper. */
static inline int bootutil_ecdsa_parse_public_key(bootutil_ecdsa_context *ctx,
                                                  uint8_t **cp, uint8_t *end);

/* Verify a signature over hash[0..hash_len). Returns 0 on success. */
static inline int bootutil_ecdsa_verify(bootutil_ecdsa_context *ctx,
                                        uint8_t *pk, size_t pk_len,
                                        uint8_t *hash, size_t hash_len,
                                        uint8_t *sig, size_t sig_len);
```

The helper interfaces below are not direct MCUboot entry points. They are only
needed if your custom encrypted-image implementation reuses the same helper
abstractions as MCUboot's stock `boot/bootutil/src/encrypted.c` logic.

### Helpers used by the stock image encryption implementation: HMAC-SHA256

```c
typedef <your_hmac_ctx_type> bootutil_hmac_sha256_context;

static inline void bootutil_hmac_sha256_init(
        bootutil_hmac_sha256_context *ctx);
static inline void bootutil_hmac_sha256_drop(
        bootutil_hmac_sha256_context *ctx);
static inline int  bootutil_hmac_sha256_set_key(
        bootutil_hmac_sha256_context *ctx,
        const uint8_t *key, uint32_t key_len);
static inline int  bootutil_hmac_sha256_update(
        bootutil_hmac_sha256_context *ctx,
        const void *data, uint32_t data_len);
static inline int  bootutil_hmac_sha256_finish(
        bootutil_hmac_sha256_context *ctx,
        uint8_t *output, uint32_t output_len);
```

### Helpers used by the stock image encryption implementation: AES-CTR

```c
typedef <your_aes_ctx_type> bootutil_aes_ctr_context;

#define BOOT_ENC_BLOCK_SIZE  16  /* must equal 16 */

static inline void bootutil_aes_ctr_init(bootutil_aes_ctr_context *ctx);
static inline void bootutil_aes_ctr_drop(bootutil_aes_ctr_context *ctx);
static inline int  bootutil_aes_ctr_set_key(bootutil_aes_ctr_context *ctx,
                                             const uint8_t *key);
static inline int  bootutil_aes_ctr_encrypt(bootutil_aes_ctr_context *ctx,
                                             uint8_t *counter,
                                             const uint8_t *m, uint32_t mlen,
                                             size_t blk_off, uint8_t *output);
static inline int  bootutil_aes_ctr_decrypt(bootutil_aes_ctr_context *ctx,
                                             uint8_t *counter,
                                             const uint8_t *c, uint32_t clen,
                                             size_t blk_off, uint8_t *output);
```

### Helpers used by the stock image encryption implementation: ECDH-P256

```c
typedef <your_ecdh_ctx_type> bootutil_ecdh_p256_context;
typedef bootutil_ecdh_p256_context bootutil_key_exchange_ctx;

static inline void bootutil_ecdh_p256_init(bootutil_ecdh_p256_context *ctx);
static inline void bootutil_ecdh_p256_drop(bootutil_ecdh_p256_context *ctx);

/* Compute the shared secret z = ECDH(sk, pk). Returns 0 on success. */
static inline int bootutil_ecdh_p256_shared_secret(
        bootutil_ecdh_p256_context *ctx,
        const uint8_t *pk,  /* 65 bytes, uncompressed */
        const uint8_t *sk,  /* 32 bytes */
        uint8_t *z);        /* 32 bytes out */
```

### Image encryption entry points

When `MCUBOOT_ENC_IMAGES` is defined and you supply a custom backend, you are
also responsible for providing the `boot_enc_*` symbols and
`boot_decrypt_key()` that MCUboot normally gets from
`boot/bootutil/src/encrypted.c`. That file guards its entire body with
`#if !defined(MCUBOOT_USE_CUSTOM_CRYPTO)` so it will not be compiled, and no
manual exclusion from the build is required. Your translation unit must
export:

```c
int  boot_decrypt_key(const uint8_t *buf, uint8_t *enckey);
int  boot_enc_init(struct enc_key_data *enc_state);
int  boot_enc_drop(struct enc_key_data *enc_state);
int  boot_enc_set_key(struct enc_key_data *enc_state, const uint8_t *key);
int  boot_enc_load(struct boot_loader_state *state, int slot,
                   const struct image_header *hdr,
                   const struct flash_area *fap,
                   struct boot_status *bs);
bool boot_enc_valid(const struct enc_key_data *enc_state);
void boot_enc_encrypt(struct enc_key_data *enc_state,
                      uint32_t off, uint32_t sz, uint32_t blk_off,
                      uint8_t *buf);
void boot_enc_decrypt(struct enc_key_data *enc_state,
                      uint32_t off, uint32_t sz, uint32_t blk_off,
                      uint8_t *buf);
void boot_enc_zeroize(struct enc_key_data *enc_state);
```
