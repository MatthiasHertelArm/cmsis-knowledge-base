---
id: "tfm-rollback-protection-in-tf-m-secure-security-counter"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Security counter"
summary: "The aim of a security counter is to have an independent (from the image version) counter in the image manifest to ensure anti-rollback protection."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#security-counter"
license: "BSD-3-Clause"
mode: "V"
---

The aim of a security counter is to have an independent (from the image version)
counter in the image manifest to ensure anti-rollback protection. During
software release the value of this counter must be increased if a security flaw
was fixed in the current version. Later when this image is installed on the
device then it is not allowed to go back to earlier versions. It is beneficial
to handle this counter independently from image main version number:

 - It does not need to increase with each software release
 - It makes it possible to do software downgrade to some extent: if the security
   counter has the same value in the older image then it is accepted.
 - If the boot loader verifies multiple images then these can be handled
   independently.

However, as an alternative solution the image version number also could serve
as the security counter of the image. Even the version number itself could be
checked during the anti-rollback verification or the value of the security
counter could be derived from the image main version. It is the responsibility
of the software issuer to define which policy to apply.
