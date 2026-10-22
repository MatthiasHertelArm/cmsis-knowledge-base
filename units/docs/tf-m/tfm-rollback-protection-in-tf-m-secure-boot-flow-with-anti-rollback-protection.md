---
id: "tfm-rollback-protection-in-tf-m-secure-boot-flow-with-anti-rollback-protection"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Boot flow with anti-rollback protection"
summary: "During software upgrade as part of the image validation process the new and active image security counters must be compared."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#boot-flow-with-anti-rollback-protection"
license: "BSD-3-Clause"
mode: "V"
---

During software upgrade as part of the image validation process the new and
active image security counters must be compared. The new image can be accepted
if its security counter has a greater or equal value than the active image
security counter. From where to extract the active image security counter it
can be platform dependent. It might read out directly from active image
manifest data (only if it is in trusted memory) or the corresponding
non-volatile counter is read.

If non-volatile counters are used to save security counters then their value
must be updated:

 - If the boot loader does not support to revert previous images (just
   overwrites the previously active image with the new one) in case of faulty
   update then the non-volatile counter can be updated to be equal with the
   new image security counter after successful authentication of the new image.
 - If revert is supported then non-volatile counter can be updated just after
   a test run of the new software when its health check is done. Just in case
   of successful health check can the counter updated to avoid the prevention
   of the revert. This might require a secondary restart of the device.
