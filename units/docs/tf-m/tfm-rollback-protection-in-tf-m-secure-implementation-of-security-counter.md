---
id: "tfm-rollback-protection-in-tf-m-secure-implementation-of-security-counter"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Implementation of security counter"
summary: "The value of the security counter is a security critical data. Any change in its value has a security implication. Therefore it must be in the integrity protected part of the image manifest."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#implementation-of-security-counter"
license: "BSD-3-Clause"
mode: "V"
---

The value of the security counter is a security critical data. Any change in
its value has a security implication. Therefore it must be in the integrity
protected part of the image manifest. Because the image header is almost fully
utilized (few unused fields) and the change of image header structure could
lead to compatibility issues between boot loader and runtime software, it is
proposed to extend the integrity protection to some part of the TLV section.
One of the unused fields in the image header can be used to store the size of
the integrity protected area of the TLV section. This is necessary to know how
to calculate properly the image hash and signature. With this extension of the
integrity protected area other attributes that require integrity protection
can easily be added to the image manifest.
