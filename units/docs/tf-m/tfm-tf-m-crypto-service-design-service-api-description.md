---
id: "tfm-tf-m-crypto-service-design-service-api-description"
type: "concept"
domain: "security"
title: "TF-M Crypto Service design: Service API description"
summary: "The Alloc and Init modules implement public APIs which are specific to the TF-M Crypto service, and are available only internally to other components of the TF-M Crypto partition."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_crypto_design.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_crypto_design.html#service-api-description"
license: "BSD-3-Clause"
mode: "V"
---

The `Alloc` and `Init` modules implement public APIs which are specific to
the TF-M Crypto service, and are available only internally to other components
of the TF-M Crypto partition. For a detailed description of the prototypes
please refer to the `tfm_crypto_api.h` header.


+--------------------------------+--------------+-----------------+------------------------------------------------------+
| **Function**                   | **Module**   | **Caller**      | **Scope**                                            |
+================================+==============+=================+======================================================+
| tfm_crypto_init()              | Init         | SPM             | Called during TF-M boot for initialisation. It       |
|                                |              |                 | does modules initialisation (it initializes the Alloc|
|                                |              |                 | module) and initializes the `backend` library. Being |
|                                |              |                 | the partition enabled for the SFN model, it does not |
|                                |              |                 | implement any IPC specific message handler, instead  |
|                                |              |                 | it relies on the SPM being able to schedule SFN      |
|                                |              |                 | partitions using the SFN dispatcher with little      |
|                                |              |                 | overhead                                             |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
| tfm_crypto_sfn()               | Init         | SPM             | Function to handle an SFN request or to interface    |
|                                |              |                 | with the message handler when running in IPC model   |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
| tfm_crypto_init_alloc()        | Alloc        | Init            | Called by `tfm_crypto_init()`, it initialises the  |
|                                |              |                 | internal memory storage in the TF-M Crypto partition |
|                                |              |                 | that the service uses to store multipart operation   |
|                                |              |                 | contexts as requested by clients.                    |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
| tfm_crypto_operation_alloc()   | Alloc        | Service modules | It allocates a new operation context for a multipart |
|                                |              |                 | operation. It returns an handle to the allocated     |
|                                |              |                 | context in secure memory.                            |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
| tfm_crypto_operation_lookup()  | Alloc        | Service modules | It retrieves a previously allocated operation context|
|                                |              |                 | of a multipart operation, based on the handle given  |
|                                |              |                 | as input.                                            |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
| tfm_crypto_operation_release() | Alloc        | Service modules | It releases a previously allocated operation context |
|                                |              |                 | of a multipart operation, based on the handle given  |
|                                |              |                 | as input.                                            |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
| tfm_crypto_*_interface()       | `*`        | Init            | Interface functions called by the dispatcher to      |
|                                |              |                 | service PSA Crypto APIs requests                     |
+--------------------------------+--------------+-----------------+------------------------------------------------------+
