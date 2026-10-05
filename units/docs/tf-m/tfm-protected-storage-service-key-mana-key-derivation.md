---
id: "tfm-protected-storage-service-key-mana-key-derivation"
type: "concept"
domain: "security"
title: "Protected Storage service key management: Key derivation"
summary: "PS will make key derivation requests to the Crypto service with calls to the PSA Crypto APIs. In order to derive the storage key, the following calls are required:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/ps_key_management.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/ps_key_management.html#key-derivation"
license: "BSD-3-Clause"
mode: "V"
---

PS will make key derivation requests to the Crypto service with calls to the
PSA Crypto APIs. In order to derive the storage key, the following calls are
required:

```c

status = psa_key_derivation_setup(&op, PSA_ALG_HKDF(PSA_ALG_SHA_256));

/* Set up a key derivation operation with HUK  */
status = psa_key_derivation_input_key(&op, PSA_KEY_DERIVATION_INPUT_SECRET,
                                      TFM_BUILTIN_KEY_ID_HUK);

/* Supply the PS key label as an input to the key derivation */
status = psa_key_derivation_input_bytes(&op, PSA_KEY_DERIVATION_INPUT_INFO,
                                        key_label,
                                        key_label_len);

/* Create the storage key from the key derivation operation */
status = psa_key_derivation_output_key(&attributes, &op, &ps_key);
```

**Note:** `TFM_BUILTIN_KEY_ID_HUK` is a static key ID that is used to identify the HUK. It has an arbitrary value defined in `tfm_crypto_defs.h` `ps_key` is a PSA Crypto key handle to a volatile key, set by the derivation operation. After the call to `psa_key_derivation_output_key`, it can be used to refer the storage key. `key_label` can be any string that is independent of the input key material and different to the label used in any other derivation from the same input key. It prevents two different contexts from deriving the same output key from the same input key.

The key derivation function used by the crypto service to derive the storage key
will be HKDF, with SHA-256 as the underlying hash function. HKDF is suitable
because:

- It is simple and efficient, requiring only two HMAC operations when the length
  of the output key material is less than or equal to the hash length (as is the
  case here).
- The trade-off is that HKDF is only suitable when the input key material has at
  least as much entropy as required for the output key material. But this is the
  case here, as the HUK has 128 bits of entropy, the same as required by PS.
- HKDF is standardised in RFC 5869 [RFC5869]_ and its security has been formally
  analysed. [HKDF]_
- It is supported by the TF-M Crypto service.

The choice of underlying hash function is fairly straightforward: it needs to be
a modern standardised algorithm, considered to be secure and supported by TF-M
Crypto. This narrows it down to just the SHA-2 family. Of the hash functions in
the family, SHA-256 is the simplest and provides more than enough output length.


### Keeping the storage key private to PS


The Crypto service derives a platform key from the HUK, using the partition ID
as the input to that derivation, and that platform key is used for the key
derivation by PS. This happens transparently, and to PS is indistinguishable
from deriving from the HUK except that other partitions cannot derive the
storage key even if they know the derivation parameters.
