---
id: "tfm-protected-storage-service-integrat-introduction"
type: "concept"
domain: "security"
title: "Protected Storage Service Integration Guide: Introduction"
summary: "TF-M Protected Storage (PS) service implements PSA Protected Storage APIs."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_ps_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_ps_integration_guide.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Protected Storage (PS) service implements PSA Protected Storage APIs.

The service is usually backed by hardware isolation of the flash
access domain and, in the current version, relies on hardware to
isolate the flash area from non-secure access. In absence of hardware
isolation, the secrecy and integrity of data is still maintained.

The PS service implements an AES-GCM based AEAD encryption policy, as a
reference, to protect data integrity and authenticity.

The PS reuses the non-hierarchical filesystem provided by the TF-M
Internal Trusted Storage service to store encrypted, authenticated
objects.

The design addresses the following high level requirements as well:

- **Confidentiality** - Resistance to unauthorised accesses through
  hardware/software attacks.

- **Access Authentication** - Mechanism to establish requester's identity (a
  non-secure entity, secure entity, or a remote server).

- **Integrity** - Resistant to tampering by either the normal users of a
  product, package, or system or others with physical access to it. If the
  content of the protected storage is changed maliciously, the service is able
  to detect it.

- **Reliability** - Resistant to power failure scenarios and incomplete write
  cycles.

- **Configurability** - High level configurability to scale up/down memory
  footprint to cater for a variety of devices with varying security
  requirements.

- **Performance** - Optimized to be used for resource constrained devices with
  very small silicon footprint, the PPA (power, performance, area) should be
  optimal.
