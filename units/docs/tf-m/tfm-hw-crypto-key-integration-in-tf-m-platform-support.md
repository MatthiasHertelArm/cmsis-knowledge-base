---
id: "tfm-hw-crypto-key-integration-in-tf-m-platform-support"
type: "concept"
domain: "security"
title: "HW crypto key integration in TF-M secure boot: Platform support"
summary: "A new platform API used by the bootloader must be introduced to retrieve the image corresponding hash of ROTPK:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_hw_key_integration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_hw_key_integration.html#platform-support"
license: "BSD-3-Clause"
mode: "V"
---

A new platform API used by the bootloader must be introduced to retrieve the
image corresponding hash of ROTPK:

``enum tfm_plat_err_t tfm_plat_get_rotpk_hash(uint8_t image_id,
uint8_t *rotpk_hash, uint32_t *rotpk_hash_size);``

The mapping between image identity and public key can be hard-code in the
platform layer. This simplifies the validation of the public key, because no
look-up would be needed. It is assumed that the memory area of the ROTPK hash is
not directly accessible, therefore a buffer is allocated by the caller to store
the hash there.
