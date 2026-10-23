---
id: "tfm-internal-trusted-storage-its-servi-new-tf-m-service"
type: "concept"
domain: "security"
title: "Internal Trusted Storage (ITS) Service: New TF-M service"
summary: "The proposal is to implement the PSA Internal Trusted Storage API with the TF-M Internal Trusted Storage service. It can be abbreviated to TF-M ITS service in general and to its in code."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_its_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_service.html#new-tf-m-service"
license: "BSD-3-Clause"
mode: "V"
---

The proposal is to implement the *PSA Internal Trusted Storage API* with the
*TF-M Internal Trusted Storage service*. It can be abbreviated to *TF-M ITS
service* in general and to `its` in code. This name has the advantage of
making clear the correspondence between the service and the API it implements.

If this name is adopted, then it may make sense to rename the *Secure Storage
service* to the *Protected Storage service* in the future to match. Then "secure
storage" could refer to the two services as a collective.

The TF-M ITS service will implement PSA ITS version 1.0. It will be provided by
a separate partition to Protected Storage, for a couple of reasons:

- To permit isolation between the services.

  - ITS is a PSA RoT Service, while Protected Storage is an Application RoT
    Service.

- To avoid circular dependencies.

  - The PSA Firmware Framework does not permit circular dependencies between
    partitions, which would occur if Protected Storage and ITS were provided by
    the same partition. Protected Storage depends on Crypto, which in turn
    depends on ITS.

The existing SST filesystem will be reused to provide the backend of the
service, with the flash layer modified to direct storage to internal flash,
rather than external.

Compared to Protected Storage, encryption, authentication and rollback
protection are not required, so the SST encrypted object layer and the crypto
and NV counter interfaces are not required. The rollback protection feature of
the object table is also not required.
