---
id: "tfm-rollback-protection-in-tf-m-secure-elements-of-software-upgrade"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Elements of software upgrade"
summary: "During a software upgrade the following entities are involved:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#elements-of-software-upgrade"
license: "BSD-3-Clause"
mode: "V"
---

During a software upgrade the following entities are involved:

 - Boot loader
 - Manifest data: Metadata of the software image: size, version, hash,
   signature, etc.
 - Software image: binary data, elf, etc.
