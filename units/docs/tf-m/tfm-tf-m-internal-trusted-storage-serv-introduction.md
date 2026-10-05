---
id: "tfm-tf-m-internal-trusted-storage-serv-introduction"
type: "concept"
domain: "security"
title: "TF-M Internal Trusted Storage Service Integration Guide: Introduction"
summary: "TF-M Internal Trusted Storage (ITS) service implements PSA Internal Trusted Storage APIs."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_its_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_its_integration_guide.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Internal Trusted Storage (ITS) service implements PSA Internal Trusted
Storage APIs.

The service is backed by hardware isolation of the flash access domain and
relies on hardware to isolate the flash area from access by the Non-secure
Processing Environment, as well as the Application Root of Trust at higher
levels of isolation.

The current ITS service design relies on hardware abstraction provided by TF-M.
The ITS service provides a non-hierarchical storage model, as a filesystem,
where all the assets are managed by a linearly indexed list of metadata.

The design addresses the following high level requirements as well:

- **Confidentiality** - Resistance to unauthorised accesses through
  hardware/software attacks. Assumed to be provided by the internal flash
  device, backed by hardware isolation.

- **Access Authentication** - Mechanism to establish requester's identity (a
  non-secure entity, secure entity, or a remote server).

- **Integrity** - Resistance to tampering by attackers with physical access is
  assumed to be provided by the internal flash device itself, while resistance
  to tampering by Non-secure or App RoT attackers also requires hardware
  isolation.

- **Reliability** - Resistance to power failure scenarios and incomplete write
  cycles.

- **Configurability** - High level of configurability to scale up/down memory
  footprint to cater for a variety of devices with varying requirements.

- **Performance** - Optimized to be used for resource constrained devices with
  very small silicon footprint, the PPA (power, performance, area) should be
  optimal.
