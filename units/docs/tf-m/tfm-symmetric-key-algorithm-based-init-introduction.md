---
id: "tfm-symmetric-key-algorithm-based-init-introduction"
type: "concept"
domain: "security"
title: "Symmetric key algorithm based Initial Attestation: Introduction"
summary: "This document proposes a design of symmetric key algorithm based Initial Attestation in TF-M."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/symmetric_initial_attest.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/symmetric_initial_attest.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

This document proposes a design of symmetric key algorithm based Initial
Attestation in TF-M.

Symmetric key algorithm based Initial Attestation
(*symmetric Initial Attestation* for short) signs and verifies Initial
Attestation Token (IAT) with a symmetric cryptography signature scheme, such as
HMAC.
It can reduce TF-M binary size and memory footprint on ultra-constrained devices
without integrating asymmetric ciphers.

This proposal follows PSA Attestation API document [1]_.

.. note ::

    As pointed out by PSA Attestation API [1]_, the use cases of Initial
    Attestation based on symmetric key algorithms can be limited due to
    the associated infrastructure costs for key management and operational
    complexities. It may also restrict the ability to interoperate with
    scenarios that involve third parties.
