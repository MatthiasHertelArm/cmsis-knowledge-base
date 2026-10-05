---
id: "tfm-symmetric-key-algorithm-based-init-iat-generation-in-initial-attestation-se"
type: "concept"
domain: "security"
title: "Symmetric key algorithm based Initial Attestation: IAT generation in Initial Attestation secure service"
summary: "The sequence of IAT generation of symmetric Initial Attestation is shown in ia-service-figure below."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/symmetric_initial_attest.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/symmetric_initial_attest.html#iat-generation-in-initial-attestation-secure-service"
license: "BSD-3-Clause"
mode: "V"
---

The sequence of IAT generation of symmetric Initial Attestation is shown in
ia-service-figure below. Note that the `Register symmetric IAK` stage
is no longer required due to changes in the Crypto partition
(`attest_symmetric_key.c` is now responsible only for calculating the instance
ID).

In Initial Attestation secure service, symmetric Initial Attestation implements
the following steps in `attest_create_token()`, which are different from those
of asymmetric Initial Attestation.

    - `attest_token_start()`,
    - Instance ID claims,
    - `attest_token_finish()`.

If `SYMMETRIC_INITIAL_ATTESTATION` is selected, symmetric Initial Attestation
dedicated implementations of those steps are included in build.
Otherwise, asymmetric Initial Attestation dedicated implementations are included
instead. Symmetric Initial Attestation implementation resides a new file
`attest_symmetric_key.c` to handle symmetric Instance ID related operations.
Symmetric Initial Attestation dedicated `attest_token_start()` and
`attest_token_finish()` are added in `attestation_token.c`.
The details are covered in following sections.


### Symmetric Instance ID


Symmetric Initial Attestation dedicated `attest_symmetric_key.c` implements
the `attest_get_instance_id()` function. This function returns the Instance ID
value, calculating it if it has not already been calculated. Refer to
Instance ID claim for more details.

.. note ::

    Only symmetric IAK for HMAC algorithm is allowed so far.


#### Instance ID calculation


In symmetric Initial Attestation, Instance ID is also calculated the first time
it is requested. It can protect critical symmetric IAK from being frequently
fetched, which increases the risk of asset disclosure.

The Instance ID value is the output of hashing symmetric IAK raw data *twice*,
as requested in PSA Attestation API [1]_. HMAC-SHA256 may be hard-coded as the
hash algorithm of Instance ID calculation.

.. note ::

    According to RFC2104 [5]_, if a HMAC key is longer than the HMAC block size,
    the key will be first hashed. The hash output is used as the key in HMAC
    computation.

    In current design, HMAC is used to calculate the authentication tag of
    `COSE_Mac0`. Assume that symmetric IAK is longer than HMAC block size
    (HMAC-SHA256 by default), the Instance ID is actually the HMAC key for
    `COSE_Mac0` authentication tag generation, if Instance ID value is the
    output of hashing IAK only *once*.
    Therefore, attackers may request an valid IAT from device and fake malicious
    ones by using Instance ID to calculate valid authentication tags, to cheat
    others.

    As a result, symmetric IAK raw data should be hashed *twice* to generate the
    Instance ID value.

The Instance ID calculation result is stored in a static buffer.
Token generation process can call `attest_get_instance_id()` to
fetch the data from that static buffer.


### attest_token_start()


Symmetric Initial Attestation dedicated `attest_token_start()` initializes the
`COSE_Mac0` computation context and builds up the `COSE_Mac0` Header.

The workflow inside `attest_token_start()` is shown in
attest-token-start-figure below.

Descriptions of each step are listed below:

#. `t_cose_mac0_sign_init()` is invoked to initialize `COSE_Mac0` signing
   context in `t_cose`.

#. The symmetric IAK handle is set into `COSE_Mac0` signing context via
   `t_cose_mac0_set_signing_key()`.

#. Initialize `QCBOR` encoder.

#. The header parameters are encoded into `COSE_Mac0` structure in
   `t_cose_mac0_encode_parameters()`.

#. `QCBOREncode_OpenMap()` prepares for encoding the `COSE_Mac0` payload,
   which is filled with IAT claims.

For detailed description and documentation of the `COSE_Mac0` functionalities
please refer to the `t_cose` repository [4]_.


### Instance ID claim


Symmetric Initial Attestation also implements Instance ID claims in
`attest_add_instance_id_claim()`. The Instance ID value is fetched via
`attest_get_instance_id()`. The value has already been calculated during
symmetric IAK registration. See Instance ID calculation for details.

The other steps are the same as those in asymmetric Initial Attestation
implementation. The UEID type byte is set to 0x01.


### attest_token_finish()


Symmetric Initial Attestation dedicated `attest_token_finish()` calls
`t_cose_mac0_encode_tag()` to calculate and encode the authentication tag of
`COSE_Mac0` structure. The whole COSE and CBOR encoding are completed in
`attest_token_finish()`. The simplified flow in `attest_token_finish()` is
shown in attest-token-finish-figure below.
