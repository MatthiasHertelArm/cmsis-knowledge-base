---
id: "tfm-initial-attestation-service-integr-psa-interface"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / PSA interface"
summary: "The TF-M Initial Attestation Service exposes the following PSA interface:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#psa-interface"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

The TF-M Initial Attestation Service exposes the following PSA
interface:

```c

psa_status_t
psa_initial_attest_get_token(const uint8_t *auth_challenge,
                             size_t         challenge_size,
                             uint8_t       *token_buf,
                             size_t         token_buf_size,
                             size_t        *token_size);

psa_status_t
psa_initial_attest_get_token_size(size_t challenge_size,
                                  size_t *token_size);
```
The caller must allocate a large enough buffer, where the token is going to be
created by Initial Attestation Service. The size of the created token is highly
dependent on the number of software components in the system and the provided
attributes of these. The `psa_initial_attest_get_token_size()` function can be
called to get the exact size of the created token.

System integrators might need to port these interfaces to a custom secure
partition manager implementation (SPM). Implementations in TF-M project can be
found here:

-  `interface/src/tfm_attest_api.c`: interface implementation.
