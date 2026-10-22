---
id: "tfm-tf-m-builtin-keys-technical-details"
type: "concept"
domain: "security"
title: "TF-M builtin keys: Technical details"
summary: "TF-M builtin key IDs are defined in interface/include/crypto_keys/tfm_builtin_key_ids.h through the enum tfm_key_id_builtin_t. They are allocated inside the range that PSA specifies for the builtin keys, i.e. between MBEDTLS_PSA_KEY_ID_BUILTIN_MIN and MBEDLTS_PSA_KEY_ID_BUILTIN_MAX."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_builtin_keys.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_builtin_keys.html#technical-details"
license: "BSD-3-Clause"
mode: "V"
---

### Builtin key IDs and overriding


TF-M builtin key IDs are defined in
`interface/include/crypto_keys/tfm_builtin_key_ids.h` through the enum
`tfm_key_id_builtin_t`. They are allocated inside the range that PSA
specifies for the builtin keys, i.e. between `MBEDTLS_PSA_KEY_ID_BUILTIN_MIN`
and `MBEDLTS_PSA_KEY_ID_BUILTIN_MAX`. A platform can specify extra builtin key
IDs by setting the `PLATFORM_DEFAULT_CRYPTO_KEYS` variable to `OFF`,
creating the header `tfm_builtin_key_ids.h`, and specifying new keys and IDs.


### Builtin key access control


A builtin key is accessible by all callers since the `key_id` associated to it
is public information. Access to the keys must be mediated, which is done by
matching the user requesting the `key_id` against the policies available for
that user on that particular key in the policy table. If no policies are
specified for a specific combination of user and `key_id`, the usage flags in
the key attributes will be all set to zeros, meaning the key will be unusable
for any operation for that particular user.


### Multi-partition key derivation


The HUK is used for key derivation by any secure partition or NS caller that
requires keys that are bound to a particular context. For example, Protected
Storage derives keys uniquely for each user of the service which are used to
encrypt user files. In order to provide HUK derivation to every secure
partition / NS caller, it must be ensured that no service that utilises HUK
derivation can derive the same key as another service (simply by using the same
inputs for the KDF APIs, i.e. accessing the same base key for derivation).

This is accomplished by deriving a further "platform key" for each builtin key
that has `PSA_KEY_USAGE_DERIVE` set in its attributes. These platform keys
are derived from the builtin key, using the partition ID as a KDF input, and
can then be used for safely for further derivations by the user, without risks
to derive the same keys as other users. This is enforced directly by the
`tfm_builtin_key_loader` driver.

If the NS client ID feature is disabled, all NS callers share a partition ID
of `-1`, and therefore will share a platform key and be therefore be able
to derive the same keys as other NS callers.
For keys that are not exposed outside the device, this is transparent to the
service that is using the key derivation, as they have no access to the builtin
key material and cannot distinguish between keys derived directly from it and
keys derived from the platform key. For some builtin keys, deriving platform
keys is not acceptable, as the key is used outside the device (i.e. the IAK
public key is used to verify attestation tokens) so the actual builtin key is
used.

The decision has been taken to derive platform keys for any key that can be used
for key derivation (`PSA_KEY_USAGE_DERIVE`), and not derive platform keys
otherwise. For builtin keys that do not derive platform keys but are directly
used, care must be taken with access control where multiple partitions have
access to the same raw key material.


### TF-PSA-Crypto transparent builtin keys


TF-PSA-Crypto does not natively support transparent builtin keys (transparent
keys are keys where the key material is directly accessible by the PSA Crypto
core), so some modifications had to be made. Opaque keyslots have the same basic
structure as standard transparent key slots, and can be passed to the functions
usually reserved for transparent keys, though this is a private implementation
detail of the TF-PSA-Crypto library and is not specified in the driver interface.
Therefore, the only modification required currently is to allow keys that have
the location `TFM_BUILTIN_KEY_LOADER_KEY_LOCATION` to be passed to the
functions that usually accept transparent keys only, i.e. with the location
`PSA_KEY_LOCATION_LOCAL_STORAGE`. This is due to the fact that the standard
assumption of the PSA Crypto core is that, if a driver that provides an
additional location, will also provide dedicated cryptographic mechanisms to act
on those keys, but this is not the case of the `tfm_builtin_key_loader`, as it
just provides a mechanism to load keys (which act as a transparent key with
local storage, once loaded), but TF-PSA-Crypto does not support such "transparent
builtin key" concept. Note that the modifications on TF-PSA-Crypto are relying
on non standard implementation details hence this particular integration can
change between releases [3]_.
