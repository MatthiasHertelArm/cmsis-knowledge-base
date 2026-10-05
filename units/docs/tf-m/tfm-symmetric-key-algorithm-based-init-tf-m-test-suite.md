---
id: "tfm-symmetric-key-algorithm-based-init-tf-m-test-suite"
type: "concept"
domain: "security"
title: "Symmetric key algorithm based Initial Attestation: TF-M Test suite"
summary: "Symmetric Initial Attestation adds dedicated non-secure and secure test suites. The test suites also follow asymmetric Initial Attestation test suites implementation but optimize the memory footprint."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/symmetric_initial_attest.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/symmetric_initial_attest.html#tf-m-test-suite"
license: "BSD-3-Clause"
mode: "V"
---

Symmetric Initial Attestation adds dedicated non-secure and secure test suites.
The test suites also follow asymmetric Initial Attestation test suites
implementation but optimize the memory footprint.
Symmetric Initial Attestation non-secure and secure test suites request Initial
Attestation secure service to generate IATs. After IATs are generated
successfully, test suites decode IATs and parse the claims.
Secure test suite also verifies the authentication tag in `COSE_Mac0`
structure.

Symmetric Initial Attestation implements its dedicated
`attest_token_decode_validate_token()` in `attest_symmetric_iat_decoded.c`
to perform IAT decoding required by test suites.
If `SYMMETRIC_INITIAL_ATTESTATION` is selected,
`attest_symmetric_iat_decoded.c` is included in build.
Otherwise, asymmetric Initial Attestation dedicated implementations are included
instead.

The workflow of symmetric Initial Attestation dedicated
`attest_token_decode_validate_token()` is shown below.

If the decoding is required from secure test suite,
`attest_token_decode_validate_token()` will fetch symmetric IAK to verify the
authentication tag in `COSE_Mac0` structure.
If the decoding is required from non-secure test suite,
`attest_token_decode_validate_token()` will only decode `COSE_Mac0` by
setting `T_COSE_OPT_DECODE_ONLY` option flag. Non-secure must not access the
symmetric IAK.
