---
id: "tfm-initial-attestation-service-integr-code-structure"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure"
summary: "The PSA interface for the Initial Attestation Service is located in interface/include. The only header to be included by applications that want to use functions from the PSA API is psa/initial_attestation.h."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#code-structure"
license: "BSD-3-Clause"
mode: "V"
---

The PSA interface for the Initial Attestation Service is located in
`interface/include`. The only header to be included by applications that want
to use functions from the PSA API is `psa/initial_attestation.h`.

The TF-M Initial Attestation Service source files are located in
`secure_fw/partitions/initial_attestation`.
