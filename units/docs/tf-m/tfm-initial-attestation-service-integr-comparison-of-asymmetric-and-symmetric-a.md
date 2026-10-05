---
id: "tfm-initial-attestation-service-integr-comparison-of-asymmetric-and-symmetric-a"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Comparison of asymmetric and symmetric algorithm based token authentication"
summary: "The symmetric key based authentication requires a more complex infrastructure for key management. Symmetric keys must be kept secret because they are sensitive asset, like the private key in case of asymmetric cryptographic algorithms."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#comparison-of-asymmetric-and-symmetric-algorithm-based-token-authentication"
license: "BSD-3-Clause"
mode: "V"
---

The symmetric key based authentication requires a more complex infrastructure
for key management. Symmetric keys must be kept secret because they are
sensitive asset, like the private key in case of asymmetric cryptographic
algorithms. The main difference is that private keys are only stored on
device, with proper hardware protection against external access, but symmetric
keys must be known by both party (device and verifier), so they must also be
stored in a central server of a relying party (who verifies the tokens).
If keys are revealed then devices can be impersonated. If the database with
the symmetric keys becomes compromised then all corresponding devices become
untrusted. Since a centralised database of symmetric keys may need to be network
connected, this can be considered to be a valuable target for attackers. The
advantage of ECDSA based token authentication is that sensitive assets is only
stored one place (in the device) and only one unique key per device. So if a
device is compromised then only that single device become untrusted. In this
case, the database of the relying party contains the corresponding public keys,
which are not considered to be a confidential assets, so they can be shared with
anybody. This shows the main advantage of asymmetric based authentication,
because verification of attestation tokens can be done by a third party,
such as cloud service providers (CSP). Thus Device Maker (DM) or Chip Maker (CM)
does not need to operate such a service.

+-------------------------+-----------------------------------------+-----------------------------------------+
|                         | Symmetric                               | Asymmetric                              |
+=========================+=========================================+=========================================+
| Authentication mode     | HMAC over SHA256                        | ECDSA P256 over SHA256                  |
+-------------------------+-----------------------------------------+-----------------------------------------+
| Crypto key type in HW   | Symmetric key                           | ECDSA private key (secp256r1)           |
+-------------------------+-----------------------------------------+-----------------------------------------+
| Secrets are stored      | Device and database                     | Device only                             |
+-------------------------+-----------------------------------------+-----------------------------------------+
| Verification database   | Same symmetric key                      | Public keys                             |
| contains                |                                         |                                         |
+-------------------------+-----------------------------------------+-----------------------------------------+
| COSE authentication tag | COSE_Mac0                               | COSE_Sign1                              |
| in the token            |                                         |                                         |
+-------------------------+-----------------------------------------+-----------------------------------------+
| Verification entity     | CM or DM, who provisioned the           | Can be anybody: third party provisioning|
|                         | symmetric key                           | service, cloud service provider, CM, DM |
+-------------------------+-----------------------------------------+-----------------------------------------+
