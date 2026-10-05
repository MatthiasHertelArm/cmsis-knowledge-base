---
id: "tfm-symmetric-key-algorithm-based-init-design-overview"
type: "concept"
domain: "security"
title: "Symmetric key algorithm based Initial Attestation: Design overview"
summary: "The symmetric Initial Attestation follows the existing IAT generation sequence for Initial Attestation based on asymmetric key algorithm (asymmetric Initial Attestation for short)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/symmetric_initial_attest.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/symmetric_initial_attest.html#design-overview"
license: "BSD-3-Clause"
mode: "V"
---

The symmetric Initial Attestation follows the existing IAT generation sequence
for Initial Attestation based on asymmetric key algorithm
(*asymmetric Initial Attestation* for short).

As Profile Small design [2]_ requests, a configuration flag
`SYMMETRIC_INITIAL_ATTESTATION` selects symmetric initial attestation during
build.

The top-level design is shown in overall-diagram-figure below.

Symmetric Initial Attestation adds its own implementations of some steps in IAT
generation in Initial Attestation secure service. More details are covered in
IAT generation in Initial Attestation secure service.

The interfaces and procedures of Initial Attestation secure service are not
affected. Refer to Initial Attestation Service Integration Guide [3]_ for
details of the implementation of Initial Attestation secure service.

Symmetric Initial Attestation invokes `t_cose` library to build up
`COSE_Mac0` structure. `COSE_Mac0` support was originally added to the
`t_cose` library fork in TF-M, however since `t_cose 2.0` it is part of
the upstream library [4]_ which is already used by TF-M too.

Several HAL APIs are defined to fetch platform specific assets required by
Symmetric Initial Attestation. For example, `tfm_plat_get_symmetric_iak()`
fetches symmetric Initial Attestation Key (IAK). Those HAL APIs are summarized
in HAL APIs.

Decoding and verification of symmetric Initial Attestation is also included in
this proposal for regression test.
The test suites and IAT decoding are discussed in TF-M Test suite.

`QCBOR` library and Crypto service are also invoked. But this proposal doesn't
require any modification to either `QCBOR` or Crypto service. Therefore,
descriptions of `QCBOR` and Crypto service are skipped in this document.
