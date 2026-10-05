---
id: "tfm-secure-boot-signature-algorithms"
type: "concept"
domain: "security"
title: "Secure boot: Signature algorithms"
summary: "TF-PSA-Crypto library is used to sign the images. The list of supported signing algorithms:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html#signature-algorithms"
license: "BSD-3-Clause"
mode: "V"
---

TF-PSA-Crypto library is used to sign the images. The list of supported signing
algorithms:

  - `RSA-2048`
  - `RSA-3072`: default

Example keys stored in:

 - `root-RSA-2048.pem`   : Used to sign single image (S+NS) or secure image
   in case of multiple image boot
 - `root-RSA-2048_1.pem` : Used to sign non-secure image in case of multiple
   image boot
 - `root-RSA-3072.pem`   : Used to sign single image (S+NS) or secure image
   in case of multiple image boot
 - `root-RSA-3072_1.pem` : Used to sign non-secure image in case of multiple
   image boot
