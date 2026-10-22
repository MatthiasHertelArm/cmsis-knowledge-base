---
id: "tfm-internal-trusted-storage-its-servi-psa-internal-trusted-storage"
type: "concept"
domain: "security"
title: "Internal Trusted Storage (ITS) Service: PSA Internal Trusted Storage"
summary: "PSA Internal Trusted Storage (ITS) is a PSA RoT Service for storing the most security-critical device data (e.g. cryptographic keys) in internal storage, which is trusted to provide data confidentiality and authenticity."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_its_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_service.html#psa-internal-trusted-storage"
license: "BSD-3-Clause"
mode: "V"
---

PSA Internal Trusted Storage (ITS) is a PSA RoT Service for storing the most
security-critical device data (e.g. cryptographic keys) in internal storage,
which is trusted to provide data confidentiality and authenticity. This
contrasts with PSA Protected Storage, which is an Application RoT service that
allows larger data sets to be stored securely in external flash, with the option
for encryption, authentication and rollback protection to protect the
data-at-rest.
