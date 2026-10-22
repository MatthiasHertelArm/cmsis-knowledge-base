---
id: "tfm-protected-storage-service-key-mana-key-use"
type: "concept"
domain: "security"
title: "Protected Storage service key management: Key use"
summary: "To encrypt and decrypt data, PS will call the PSA Crypto AEAD APIs in the same way as the current implementation, but ps_key will refer to the storage key, rather than the imported HUK."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/ps_key_management.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/ps_key_management.html#key-use"
license: "BSD-3-Clause"
mode: "V"
---

To encrypt and decrypt data, PS will call the PSA Crypto AEAD APIs in the same
way as the current implementation, but `ps_key` will refer to the storage key,
rather than the imported HUK. For each encryption operation, the following call
is made (and analogously for decryption):

```c

psa_aead_encrypt(ps_key, PS_CRYPTO_ALG,
                 crypto->ref.iv, PS_IV_LEN_BYTES,
                 add, add_len,
                 in, in_len,
                 out, out_size, out_len);
```
