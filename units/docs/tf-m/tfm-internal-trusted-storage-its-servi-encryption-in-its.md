---
id: "tfm-internal-trusted-storage-its-servi-encryption-in-its"
type: "concept"
domain: "security"
title: "Internal Trusted Storage (ITS) Service: Encryption in ITS"
summary: "The ITS can optionally be configured to encrypt the internal trusted storage data. To support encryption in ITS the target platform must provide an implementation of the APIs defined in platform/include/tfm_hal_its_encryption.h::"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_its_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_service.html#encryption-in-its"
license: "BSD-3-Clause"
mode: "V"
---

The ITS can optionally be configured to encrypt the internal trusted storage
data.
To support encryption in ITS the target platform must provide an
implementation of the APIs defined in `platform/include/tfm_hal_its_encryption.h`::
```
enum tfm_hal_status_t tfm_hal_its_aead_generate_nonce(uint8_t *nonce,
                                                      const size_t nonce_size);

enum tfm_hal_status_t tfm_hal_its_aead_encrypt(
                                     struct tfm_hal_its_auth_crypt_ctx *ctx,
                                     const uint8_t *plaintext,
                                     const size_t plaintext_size,
                                     uint8_t *ciphertext,
                                     const size_t ciphertext_size,
                                     uint8_t *tag,
                                     const size_t tag_size);

enum tfm_hal_status_t tfm_hal_its_aead_decrypt(
                                     struct tfm_hal_its_auth_crypt_ctx *ctx,
                                     const uint8_t *ciphertext,
                                     const size_t ciphertext_size,
                                     uint8_t *tag,
                                     const size_t tag_size,
                                     uint8_t *plaintext,
                                     const size_t plaintext_size);
```
Then encryption can be enabled by setting the build option `-DITS_ENCRYPTION=ON`.

The figure fig-tfm_eits describes the encryption and decryption
process happening when calling `tfm_its_set` and `tfm_its_get`.

By using an AEAD scheme, it is possible to not only encrypt the file data but
also authenticate the file meta data, which include:

- File id
- File size
- File flags

The key used to perform the AEAD operation must be derived from a long-term
key-derivation key and the file id, which is used as a derivation label.
The long-term key-derivation key must be managed by the target platform.

There is a generic implementation of the abovementioned functions under
`platform/ext/common/template/tfm_hal_its_encryption.c` using PSA crypto calls
similar to Protected Storage solution. When used, the default NV seed template
under `platform/ext/common/template/crypto_nv_seed.c` must be disabled, as it
relies on ITS. If there is a need for NV seed usage, an ITS independent
implementation is required. If NV seed is not necessary, it can be turned off by
setting `CRYPTO_NV_SEED=0`.


--------------

*Copyright (c) 2019-2024, Arm Limited. All rights reserved.*
