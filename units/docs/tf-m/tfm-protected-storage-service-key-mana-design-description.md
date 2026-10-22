---
id: "tfm-protected-storage-service-key-mana-design-description"
type: "concept"
domain: "security"
title: "Protected Storage service key management: Design description"
summary: "Each time the system boots, PS will request that the Crypto service uses a key derivation function (KDF) to derive a storage key from the HUK, by referring to the builtin key handle for the HUK."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/ps_key_management.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/ps_key_management.html#design-description"
license: "BSD-3-Clause"
mode: "V"
---

Each time the system boots, PS will request that the Crypto service uses a key
derivation function (KDF) to derive a storage key from the HUK, by referring to
the builtin key handle for the HUK. The storage key could be kept in on-chip
volatile memory private to the Crypto partition, or it could remain inside a
secure element. Either way it will not be returned to PS.

For each call to the PSA Protected Storage APIs, PS will make requests to the
Crypto service to perform AEAD encryption and/or decryption operations using the
storage key (providing a fresh nonce for each encryption).

At no point will PS access the key material itself, only referring to the HUK
and storage key by their handles in the Crypto service.
