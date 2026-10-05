---
id: "tfm-tf-m-crypto-service-design-components"
type: "concept"
domain: "security"
title: "TF-M Crypto Service design: Components"
summary: "The TF-M Crypto service is implemented by a number of different firmware components residing in the Crypto partition, which are listed below:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_crypto_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_crypto_design.html#components"
license: "BSD-3-Clause"
mode: "V"
---

The TF-M Crypto service is implemented by a number of different firmware
components residing in the Crypto partition, which are listed below:


+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| **Component name**          | **Description**                                               | **Location**                                                         |
+=============================+===============================================================+======================================================================+
| Client API interface        | This module exports the PSA Crypto API to be callable from the| `interface/src/tfm_crypto_api.c`                                   |
|                             | users, which are called also `clients`. They could be either  |                                                                      |
|                             | other secure partitions or Non Secure world based callers.    |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| TF-PSA-Crypto               | The TF-PSA-Crypto `libtfpsacrypto.a` library is used in the | Needed as dependency specified by the `TF_PSA_CRYPTO_PATH` CMake   |
|                             | service as a cryptographic `backend` library which provides   | configuration option                                                 |
|                             | the APIs to implement a PSA Crypto `core`, SW based crypto    |                                                                      |
|                             | primitives and wrappers for HW crypto accelerators and Secure |                                                                      |
|                             | Elements. It exposes those through the PSA Crypto APIs        |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| Init module                 | This module handles the initialisation of the service objects | `secure_fw/partitions/crypto/crypto_init.c`                        |
|                             | during TF-M boot and provides the infrastructure to service   |                                                                      |
|                             | requests when TF-M is built for IPC or SFN model.             |                                                                      |
|                             | The dispatching mechanism of IPC requests is based on a look  |                                                                      |
|                             | up table of function pointers.                                |                                                                      |
|                             | This design allows for better scalability and support of a    |                                                                      |
|                             | higher number of Secure functions with minimal overhead and   |                                                                      |
|                             | duplication of code.                                          |                                                                      |
|                             | This module is in charge of providing an ID of the caller of  |                                                                      |
|                             | each API in the backend, allowing to enforce key ownership    |                                                                      |
|                             | policies.                                                     |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| Alloc module                | This module handles the allocation of contexts for multipart  | `secure_fw/partitions/crypto/crypto_alloc.c`                       |
|                             | operations in the Secure world. This is required because the  |                                                                      |
|                             | caller view of contexts, i.e. `clients`, does not contain any |                                                                      |
|                             | sensible information but just a number handle which is then   |                                                                      |
|                             | used by the service itself to match the context to the actual |                                                                      |
|                             | context information which will be stored securely in the TF-M |                                                                      |
|                             | crypto partition private memory. This is enabled by setting   |                                                                      |
|                             | `MBEDTLS_PSA_CRYPTO_CLIENT` option on the caller side. Note |                                                                      |
|                             | that setting this option on the client side is a hard         |                                                                      |
|                             | requirement in order for the clients to work correctly        |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| Service modules             | These modules (AEAD, Asymmetric, Cipher, Hash, Key Derivation,| `secure_fw/partitions/crypto/crypto_aead.c`                        |
|                             | Key Management, MAC, Random Number Generation) represent a    | `secure_fw/partitions/crypto/crypto_asymmetric.c`                  |
|                             | thin layer which is in charge of servicing the calls from the | `secure_fw/partitions/crypto/crypto_cipher.c`                      |
|                             | clients. They provide parameter sanitization and context      | `secure_fw/partitions/crypto/crypto_hash.c`                        |
|                             | retrieval for multipart operations, and dispatching to the    | `secure_fw/partitions/crypto/crypto_key_derivation.c`              |
|                             | corresponding backend library function exposed by the         | `secure_fw/partitions/crypto/crypto_key_management.c`              |
|                             | underlying library.                                           | `secure_fw/partitions/crypto/crypto_mac.c`                         |
|                             |                                                               | `secure_fw/partitions/crypto/crypto_rng.c`                         |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| Backend library abstraction | This module contains several APIs to abstract the interface   | `secure_fw/partitions/crypto/crypto_library.*`                     |
|                             | towards the backend library, which must provide the PSA Crypto|                                                                      |
|                             | core layer, key management, SW based crypto and possibly      |                                                                      |
|                             | interfaces for HW crypto accelerators and Secure Elements     |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| Manifest                    | The manifest file is a description of the service components. | `secure_fw/partitions/crypto/tfm_crypto.yaml`                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| CMake, Kconfig and headers  | The CMake files are used by the TF-M CMake build system to    | `secure_fw/partitions/crypto/CMakeLists.txt`                       |
|                             | build the service as part of the Secure FW build. The service | `secure_fw/partitions/crypto/Kconfig`                              |
|                             | is built as a static library                                  | `secure_fw/partitions/crypto/Kconfig.comp`                         |
|                             | (`libtfm_psa_rot_partition_crypto.a`).                      | `secure_fw/partitions/crypto/config_crypto_check.h`                |
|                             | The service itself depends on the build of the underlying     | `secure_fw/partitions/crypto/config_engine_buf.h`                  |
|                             | backend library, by default the `libtfpsacrypto.a` target,  | `secure_fw/partitions/crypto/tfm_crypto_api.h`                     |
|                             | a static library built by the TF-PSA-Crypto build system.     | `secure_fw/partitions/crypto/crypto_spe.h`                         |
|                             | The `tfm_crypto_api.h` header contains public service APIs, | `interface/include/tfm_crypto_defs.h`                              |
|                             | which expose each module's interface. The header available in |                                                                      |
|                             | the interface, `tfm_crypto_defs.h`, contains types and      |                                                                      |
|                             | definitions to build the client interface of the service, i.e.|                                                                      |
|                             | towards other services or NS world.                           |                                                                      |
|                             | Finally, the `crypto_spe.h` header is used during the       |                                                                      |
|                             | build of the TF-PSA-Crypto library, when the configuration    |                                                                      |
|                             | option `MBEDTLS_PSA_CRYPTO_SPM` is defined, to add a custom |                                                                      |
|                             | prefix to the PSA API symbols so that duplication of symbol   |                                                                      |
|                             | names is avoided. The prefix used for the symbols of the      |                                                                      |
|                             | library is chosen to be `tfpsacrypto__`.                    |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| TF-M Crypto key abstraction | The TF-M Crypto service has its own type definition to be able| `secure_fw/partitions/crypto/tfm_crypto_key.h`                     |
|                             | to identify a key ID with its own owner. The definition of an |                                                                      |
|                             | owner is provided by the TF-M Firmware Framework and is out of|                                                                      |
|                             | the scope of the service itself and the PSA Crypto APIs spec. |                                                                      |
|                             | The underlying library in practice must provide the same      |                                                                      |
|                             | functionality, i.e handle key IDs with associated owner info. |                                                                      |
|                             | For TF-PSA-Crypto, this is accomplished by the type           |                                                                      |
|                             | `mbedtls_svc_key_id_t` when the config option               |                                                                      |
|                             | `MBEDTLS_PSA_CRYPTO_KEY_ID_ENCODES_OWNER` of TF-PSA-Crypto  |                                                                      |
|                             | is defined. Note that setting this option in TF-PSA-Crypto is |                                                                      |
|                             | a hard requirement for when the library is built on the       |                                                                      |
|                             | service side, while it shall never be set when the headers    |                                                                      |
|                             | are included for client side components                       |                                                                      |
|                             | (i.e. other partitions or NS interface).                      |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
| Documentation               | The                                                           | `docs/integration_guide/services/tfm_crypto_integration_guide.rst` |
|                             | integration guide |                                                                      |
|                             | contains the description of the TF-M Crypto service modules   |                                                                      |
|                             | and interfaces.                                               |                                                                      |
+-----------------------------+---------------------------------------------------------------+----------------------------------------------------------------------+
The interaction between the different components is described by the
block diagram in block_diagram-label
