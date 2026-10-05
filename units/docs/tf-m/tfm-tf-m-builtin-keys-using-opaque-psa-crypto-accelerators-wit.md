---
id: "tfm-tf-m-builtin-keys-using-opaque-psa-crypto-accelerators-wit"
type: "concept"
domain: "security"
title: "TF-M builtin keys: Using Opaque PSA crypto accelerators with TF-M"
summary: "For platforms which have a cryptographic accelerator which has a corresponding Opaque PSA crypto accelerator driver, the TF-M builtin key loader driver can be disabled using the -DCRYPTO_TFM_BUILTIN_KEYS_DRIVER=OFF cmake option."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/tfm_builtin_keys.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_builtin_keys.html#using-opaque-psa-crypto-accelerators-with-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

For platforms which have a cryptographic accelerator which has a corresponding
Opaque PSA crypto accelerator driver, the TF-M builtin key loader driver can be
disabled using the `-DCRYPTO_TFM_BUILTIN_KEYS_DRIVER=OFF` cmake option. The
platform can then redefine the HAL function
`tfm_plat_builtin_key_get_desc_table_ptr` to point to a table where the
location and slot number of the keys corresponds instead to the opaque driver.
The PSA driver wrapper will then route the calls into the opaque driver, with no
other changes needed. If the description table is altered but the builtin key
loader driver is not disabled, it is possible to mix software builtin keys with
keys stored in opaque accelerators on a per-key level. Note that because the key
policy enforcement via `tfm_plat_builtin_key_get_desc_table_ptr` is currently
applied by the builtin key loader driver, other opaque drivers must apply either
this policy or their own policy (Though this may be changed in future).
