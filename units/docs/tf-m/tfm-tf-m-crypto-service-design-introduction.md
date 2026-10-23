---
id: "tfm-tf-m-crypto-service-design-introduction"
type: "concept"
domain: "security"
title: "TF-M Crypto Service design: Introduction"
summary: "The TF-M Crypto service provides an implementation of the PSA Certified Crypto APIs in a PSA RoT secure partition in TF-M."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_crypto_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_crypto_design.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The TF-M Crypto service provides an implementation of the PSA Certified Crypto
APIs in a PSA RoT secure partition in TF-M. It is based on the TF-PSA-Crypto
project, which provides a reference implementation of the PSA Crypto APIs as a
`C` software library. For more details on the PSA Crypto APIs refer to [1]_,
while for the TF-PSA-Crypto reference software refer to [2]_ and [3]_

The service can be requested by other services running in the SPE, or by
applications running in the NSPE, and its aim is to provide cryptographic
primitives in a secure and efficient way, either via software or by routing the
calls to any underlying crypto hardware accelerator or secure element that the
platform might provide.
