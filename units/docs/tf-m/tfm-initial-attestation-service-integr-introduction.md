---
id: "tfm-initial-attestation-service-integr-introduction"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Introduction"
summary: "TF-M Initial Attestation Service allows the application to prove the device identity during an authentication process to a verification entity. The initial attestation service can create a token on request, which contains a fix set of device specific data."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Initial Attestation Service allows the application to prove the device
identity during an authentication process to a verification entity. The initial
attestation service can create a token on request, which contains a fix set of
device specific data.

TF-M Initial Attestation Service by default enables asymmetric key algorithm
based attestation (*asymmetric attestation* for short). Symmetric key algorithm
based attestation (*symmetric attestation* for short) can be enabled instead by
selecting build option `SYMMETRIC_INITIAL_ATTESTATION`.

    - In asymmetric attestation, device must contain an attestation key pair,
      which is unique per device. The token is signed with the private part of
      attestation key pair. The public part of the key pair is known by the
      verification entity. The public key is used to verify the token
      authenticity.
    - In symmetric attestation, device should contain a symmetric attestation
      key to generate the authentication tag of token content. The verification
      entity uses the same symmetric key to verify the token authenticity.

The data items in the token used to verify the device integrity and assess its
trustworthiness. Attestation key provisioning is out of scope for the
attestation service and is expected to take part during manufacturing of the
device.
