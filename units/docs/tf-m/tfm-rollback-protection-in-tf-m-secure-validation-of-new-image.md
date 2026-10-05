---
id: "tfm-rollback-protection-in-tf-m-secure-validation-of-new-image"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Validation of new image"
summary: "Boot loader is responsible to authenticate the new image according to the required policies and decide whether the new image is fulfilling all the requirements."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#validation-of-new-image"
license: "BSD-3-Clause"
mode: "V"
---

Boot loader is responsible to authenticate the new image according to the
required policies and decide whether the new image is fulfilling all the
requirements. Boot loader verifies the image integrity (hash calculation) and
the origination (signature validation), and might verify other requirements as
well. If the new image is successfully authenticated then the boot loader is in
charge to do the necessary steps (load to execute address, etc.) to enable the
new image to be executed. During the validation process the image and the
manifest data is checked.
