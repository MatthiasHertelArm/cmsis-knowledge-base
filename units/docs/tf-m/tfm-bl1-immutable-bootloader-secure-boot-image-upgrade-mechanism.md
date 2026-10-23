---
id: "tfm-bl1-immutable-bootloader-secure-boot-image-upgrade-mechanism"
type: "concept"
domain: "security"
title: "BL1 Immutable bootloader: Secure boot / Image upgrade mechanism"
summary: "BL1_2 verifies the authenticity of the next stage image via asymmetric cryptography, using a public key that is provisioned into OTP."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/bl1.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/bl1.html#secure-boot-image-upgrade-mechanism"
license: "BSD-3-Clause"
mode: "V"
---

BL1_2 verifies the authenticity of the next stage image via asymmetric
cryptography, using a public key that is provisioned into OTP.

BL1_2 implements a rollback protection counter in OTP, which is used to prevent
the next stage image being downgraded to a less secure version.

BL1_2 has two image slots, which allows image upgrades to be performed. The
primary slot is always booted first, and then if verification of this fails
(either due to an invalid signature or due to a version lower than the rollback
protection counter) the secondary slot is then booted (subject to the same
checks).

BL1_2 contains no image upgrade logic, in order for OTA of the next stage image
to be implemented, a later stage in the system must handle downloading new
images and placing them in the required slot.
