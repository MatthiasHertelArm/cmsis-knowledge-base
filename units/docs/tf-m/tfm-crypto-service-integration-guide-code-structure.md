---
id: "tfm-crypto-service-integration-guide-code-structure"
type: "concept"
domain: "security"
title: "Crypto Service Integration Guide: Code structure"
summary: "The PSA interfaces for the Crypto service are located in interface/include. The only header to be included by applications that want to use functions from the PSA API is psa/crypto.h. The TF-M Crypto service source files are located in secure_fw/partitions/crypto."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_crypto_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_crypto_integration_guide.html#code-structure"
license: "BSD-3-Clause"
mode: "V"
---

The PSA interfaces for the Crypto service are located in `interface/include`.
The only header to be included by applications that want to use functions from
the PSA API is `psa/crypto.h`. The TF-M Crypto service source files are
located in `secure_fw/partitions/crypto`.


### PSA interfaces

The TF-M Crypto service exposes the PSA interfaces detailed in the header
`psa/crypto.h`. This header, in turn, includes several other headers which
are not meant to be included directly by user applications. For a detailed
description of the PSA API interface, please refer to the comments in the
`psa/crypto.h` header itself.


### Service source files

A brief description of what is implemented by each source file is as below:

 - `crypto_cipher.c` : Dispatcher for symmetric crypto operations
 - `crypto_hash.c` : Dispatcher for hash operations
 - `crypto_mac.c` : Dispatcher for MAC operations
 - `crypto_aead.c` : dispatcher for AEAD operations
 - `crypto_key_derivation.c` : Dispatcher for key derivation and key agreement
   operations
 - `crypto_key_management.c` : Dispatcher for key management operations
   towards the key slot management system provided by the backend library
 - `crypto_rng.c` : Dispatcher for the random number generation requests
 - `crypto_asymmetric.c` : Dispatcher for message signature/verification and
   encryption/decryption using asymmetric crypto
 - `crypto_init.c` : Init module for the service. The modules stores also the
   internal buffer used to allocate temporarily the IOVECs needed, which is not
   required in case of SFN model. The size of this buffer is controlled by the
   `CRYPTO_IOVEC_BUFFER_SIZE` config define
 - `crypto_library.c` : Library abstractions to interface the dispatchers
   towards the underlying library providing *backend* crypto functions.
   Currently this only supports the TF-PSA-Crypto library. In particular, the
   TF-PSA-Crypto library requires to provide a static buffer to be used as heap
   for its internal allocation. The size of this buffer is controlled by the
   `CRYPTO_ENGINE_BUF_SIZE` config define
 - `crypto_alloc.c` : Takes care of storing multipart operation contexts in a
   secure memory not visible outside of the crypto service. The
   `CRYPTO_CONC_OPER_NUM` config define determines how many concurrent
   contexts are supported at once. In a multipart operation, the client view of
   the contexts is much simpler (i.e. just an handle), and the Alloc module
   keeps track of the association between handles and contexts
 - `tfm_crypto_api.c` :  This module is contained in `interface/src` and
   implements the PSA Crypto API client interface exposed to both S/NS clients.
   This module allows a configuration option `CONFIG_TFM_CRYPTO_API_RENAME`
   to be set to 1 in case the NS environment or integrators want to rename the
   API symbols exported by the TF-M Crypto service. The renaming adds a default
   prefix, `tfm_crypto__` to all functions. The prefix can be changed editing
   the interface file. This config option is for the NS environment or
   integration setup only, hence it is not accessible through the TF-M config
 - `tfm_mbedcrypto_alt.c` : This module is specific to the Mbed TLS [3]_
   library integration and provides some alternative implementation of Mbed TLS
   APIs that can be used when a optimised profile is chosen. Through the
   `_ALT` mechanism it is possible to replace at link time default
   implementations available in Mbed TLS with the ones available in this file

The `_ALT` mechanism will be deprecated in future releases of the Mbed
TLS library
