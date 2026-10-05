---
id: "tfm-initial-attestation-service-integr-crypto-interface"
type: "concept"
domain: "security"
title: "Initial Attestation Service Integration Guide: Code structure / Crypto interface"
summary: "Device must contain an asymmetric key pair. The private part of it is used to sign the initial attestation token. Current implementation supports only the ECDSA P256 signature over SHA256."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_attestation_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_attestation_integration_guide.html#crypto-interface"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Code structure_

#### Asymmetric key algorithm based attestation

Device **must** contain an asymmetric key pair. The private part of it is used
to sign the initial attestation token. Current implementation supports only the
ECDSA P256 signature over SHA256. The public part of the key pair is used to
create the key identifier (kid) in the unprotected part of the COSE header. The
kid is used by the verification entity to look up the corresponding public key
to verify the signature in the token. The `t_cose` part of the initial
attestation service implements the signature generation and kid creation. But
the actual calculation of token's hash and signature is done by the Crypto
service in the device. System integrators might need to re-implement the
following functions if they want to use initial attestation service with a
different cryptographic library than Crypto service:

- `t_cose_crypto_pub_key_sign()`: Calculates the signature over a hash value.
- `t_cose_crypto_get_ec_pub_key()`: Get the public key to create the key
  identifier.
- `t_cose_crypto_hash_start()`: Start a multipart hash operation.
- `t_cose_crypto_hash_update()`: Add a message fragment to a multipart hash
  operation.
- `t_cose_crypto_hash_finish()`:Finish the calculation of the hash of a
  message.

Interface needed by verification code:

-  `t_cose_crypto_pub_key_verify()`: Verify the signature over a hash value.


##### Key handling

The provisioning of the initial attestation key is out of scope of the service
and this document. It is assumed that device maker provisions the unique
asymmetric key pair during the manufacturing process. Software integrators
**must** make sure that `TFM_BUILTIN_KEY_SLOT_IAK` is available via the Crypto
service, which will then be used by the Attestation partition to perform the
required signing operations via the PSA crypto interface.


#### Symmetric key algorithm based attestation

Device **must** contain a symmetric key to generate the authentication tag of
the initial attestation token. A key identifier (kid) can be encoded in the
unprotected part of the COSE header. It helps verification entity look up the
symmetric key to verify the authentication tag in the token.

The `t_cose` part of the initial attestation service implements the
authentication tag generation. The authentication tag generation is done by the
Crypto service. System integrators might need to re-implement the following
functions if platforms provide a different cryptographic library than Crypto
service:

- `t_cose_crypto_hmac_sign_setup()`: Set up a multi-part HMAC calculation
  operation.
- `t_cose_crypto_hmac_update()`: Add a message fragment to a multi-part HMAC
  operation.
- `t_cose_crypto_hmac_sign_finish()`: Finish the calculation of the HMAC of a
  message.

Interface needed by verification code:

- `t_cose_crypto_hmac_verify_setup()`: Set up a multi-part HMAC verification
  operation.
- `t_cose_crypto_hmac_verify_finish()`: Finish the verification of the HMAC of
  a message.

It also requires the same hash operations as listed in asymmetric key algorithm
based initial attestation above, in attestation test cases.


##### Key handling

The provisioning of the initial attestation key is out of scope of the service
and this document. It is assumed that device maker provisions the symmetric key
during the manufacturing process. The following API is defined to retrieve the
symmetric attestation key from platform layer. Software integrators **must**
port this interface according to their SoC design and make sure that key is
available by Crypto service:

- `tfm_plat_get_symmetric_iak()`: Get the symmetric initial attestation key
  raw data.
- `tfm_plat_get_symmetric_iak_id()`: Get the key identifier of the symmetric
  initial attestation key. The key identifier can be used as `kid` parameter
  in COSE header. Optional.


**Note:** Asymmetric initial attestation and symmetric initial attestation may share the same HAL APIs in future development.
