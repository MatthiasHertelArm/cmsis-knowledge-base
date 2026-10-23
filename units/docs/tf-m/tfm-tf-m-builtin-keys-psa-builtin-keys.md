---
id: "tfm-tf-m-builtin-keys-psa-builtin-keys"
type: "concept"
domain: "security"
title: "TF-M builtin keys: PSA builtin keys"
summary: "The PSA Cryptographic API provides a mechanism for accessing keys that are stored in platform-specific locations (often hardware accelerators or OTP). A builtin key is assigned a specific key_id, i.e."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_builtin_keys.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_builtin_keys.html#psa-builtin-keys"
license: "BSD-3-Clause"
mode: "V"
---

The PSA Cryptographic API provides a mechanism for accessing keys that are
stored in platform-specific locations (often hardware accelerators or OTP). A
builtin key is assigned a specific key_id, i.e. a handle, which is hardcoded at
build time and must be selected in the range [MBEDTLS_PSA_KEY_ID_BUILTIN_MIN,
MBEDLTS_PSA_KEY_ID_BUILTIN_MAX]. A user of the PSA Crypto API can reference
those keys directly by using these handles. It is up to the platform to specify
policy restrictions for specific users of the keys, e.g. an NS entity, or a
secure partition. The PSA Crypto core will then check those policies to grant
or deny access to the builtin key for that user.
