---
id: "tfm-protected-storage-service-integrat-code-structure"
type: "concept"
domain: "security"
title: "Protected Storage Service Integration Guide: Code Structure"
summary: "Protected storage service code is located in secure_fw/partitions/protected_storage/ and is divided as follows:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_ps_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_ps_integration_guide.html#code-structure"
license: "BSD-3-Clause"
mode: "V"
---

Protected storage service code is located in
`secure_fw/partitions/protected_storage/` and is divided as follows:

    - Core files
    - Cryptographic interfaces
    - Non-volatile (NV) counters interfaces

The PSA PS interfaces for PS service are located in `interface/include/psa`


### PSA Protected Storage Interfaces


The PS service exposes the following mandatory PSA PS interfaces, version 1.0:

```c

psa_status_t psa_ps_set(psa_storage_uid_t uid, size_t data_length, const void *p_data, psa_storage_create_flags_t create_flags);
psa_status_t psa_ps_get(psa_storage_uid_t uid, size_t data_offset, size_t data_size, void *p_data, size_t *p_data_length);
psa_status_t psa_ps_get_info(psa_storage_uid_t uid, struct psa_storage_info_t *p_info);
psa_status_t psa_ps_remove(psa_storage_uid_t uid);
uint32_t psa_ps_get_support(void);
```
For the moment, it does not support the extended version of those APIs.

These PSA PS interfaces and PS TF-M types are defined and documented in
`interface/include/psa/protected_storage.h`,
`interface/include/psa/storage_common.h` and
`interface/include/tfm_ps_defs.h`


### Core Files

- `tfm_ps_req_mngr.c` - Contains the PS request manager implementation which
  handles all requests which arrive to the service. This layer extracts the
  arguments from the input and output vectors, and it calls the protected
  storage layer with the provided parameters.

- `tfm_protected_storage.c` - Contains the TF-M protected storage API
  implementations which are the entry points to the PS service.

- `ps_object_system.c` - Contains the object system implementation to manage
  all objects in PS area.

- `ps_object_table.c` - Contains the object system table implementation which
  complements the object system to manage all object in the PS area.
  The object table has an entry for each object stored in the object system
  and keeps track of its version and owner.

- `ps_encrypted_object.c` - Contains an implementation to manipulate
  encrypted objects in the PS object system.

- `ps_utils.c` - Contains common and basic functionalities used across the
  PS service code.

- `ps_filesystem_interface.c` - Contains the interface to directly use ITS
  implementation of services.


### Flash Filesystem and Flash Interfaces


The non-hierarchical filesystem and flash interfaces reside under
Internal Trusted Storage service directory. The way PS service uses
them depends on the config option `TFM_PARTITION_INTERNAL_TRUSTED_STORAGE`.

When TF-M Internal trusted storage service is active (i.e.
`TFM_PARTITION_INTERNAL_TRUSTED_STORAGE` = ON), all file system and storage
interfaces are built as part of ITS service library. Thus, the PS service stores
encrypted, authenticated objects by making service calls to the ITS service.

When TF-M Internal trusted storage service is disabled (i.e.
`TFM_PARTITION_INTERNAL_TRUSTED_STORAGE` = OFF), all file system and storage
interfaces are built as part of PS service library. Thus, the PS service stores
encrypted, authenticated objects by making standard function calls to the file
system within its own partition code.

The ITS filesystem and flash interfaces and their implementation can be found in
`secure_fw/partitions/internal_trusted_storage/flash_fs` and
`secure_fw/partitions/internal_trusted_storage/flash` respectively. More
information about the filesystem and flash interfaces can be found in the
:doc:`ITS integration guide
</integration_guide/services/tfm_its_integration_guide>`.

The ITS service implementation in
`secure_fw/partitions/internal_trusted_storage/tfm_internal_trusted_storage.c`,
constructs a filesystem configuration for Protected Storage based on
target-specific definitions from the Protected Storage HAL. Please see the
`Protected Storage Service HAL` section for details of these.


### Cryptographic Interface

- `crypto/ps_crypto_interface.h` - Abstracts the cryptographic operations for
  the protected storage service.

- `crypto/ps_crypto_interface.c` - Implements the PS service cryptographic
  operations with calls to the TF-M Crypto service.


### Non-volatile (NV) Counters Interface

The current PS service provides rollback protection based on NV
counters.
PS defines and implements the following NV counters functionalities:

- `nv_counters/ps_nv_counters.h` - Abstracts PS non-volatile
  counters operations. This API detaches the use of NV counters from the TF-M NV
  counters implementation, provided by the platform, and provides a mechanism to
  compile in a different API implementation for test purposes. A PS test suite
  **may** provide its own custom implementation to be able to test different PS
  service use cases.

- `nv_counters/ps_nv_counters.c` - Implements the PS NV counters interfaces
  based on TF-M NV counters implementation provided by the platform.
