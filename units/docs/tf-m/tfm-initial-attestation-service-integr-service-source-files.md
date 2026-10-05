---
id: "tfm-initial-attestation-service-integr-service-source-files"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Service source files"
summary: "Initial Attestation Service Integration Guide: Code structure / Service source files"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#service-source-files"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

- CBOR library
    - `lib/ext/qcbor` This library is used to create a proper CBOR token.
      It can be used on 32-bit and 64-bit machines. It was designed to suite
      constrained devices with low memory usage and without dynamic memory
      allocation.
      Its source code is fetched automatically during the build configuration
      step from an external repository: [QCBOR library](https://github.com/laurencelundblade/QCBOR).
    - `<qcbor_src>/inc/qcbor/qcbor_encode.h`: Public API documentation of
      CBOR library (encoding).
    - `<qcbor_src>/inc/qcbor/qcbor_decode.h`: Public API documentation of
      CBOR library (decoding).

- COSE library:
    - `lib/ext/t_cose`: This library is used to sign a CBOR token and create
      the COSE header and signature around the initial attestation token. Only
      a subset of the [COSE](https://tools.ietf.org/html/rfc8152) standard
      is implemented. The COSE_Sign, COSE_Sign1, COSE_Mac0 signature and the
      COSE_Encrypt, COSE_Encrypt0 encryption schemes are supported.
      Its source code is fetched automatically during the build configuration
      step from an external repository: [t_cose library](https://github.com/laurencelundblade/t_cose).
    - `<t_cose_src>/src/t_cose_crypto.h`: Expose an API to bind `t_cose`
      library with available crypto library in the device.
    - `<t_cose_src>/crypto_adapters/t_cose_psa_crypto.c`: Implements the
      exposed API and ports `t_cose` to the PSA Crypto API.

- Initial Attestation Service:
    - `attest_core.c` : Implements core functionalities such as implementation
      of APIs, retrieval of claims and token creation.
    - `attest_boot_data.c` : Implements core functionalities for measured
      boot.
    - `attest_token_encode.c`: Implements the token creation functions such as
      start and finish token creation and adding claims to the token.
    - `attest_asymmetric_key.c`: Calculate the Instance ID value based on
      asymmetric initial attestation key.
    - `tfm_attest.c`: Implements the SPM abstraction layer, and bind the
      attestation service to the SPM implementation in TF-M project.
    - `tfm_attest_req_mngr.c`: Includes the initialization entry of
      attestation service and handles attestation service requests in IPC
      model.
    - `attest_symmetric_key.c`: Calculate the Instance ID value based on
      symmetric initial attestation key.
