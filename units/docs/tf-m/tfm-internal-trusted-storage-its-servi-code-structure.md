---
id: "tfm-internal-trusted-storage-its-servi-code-structure"
type: "concept"
domain: "security"
title: "Internal Trusted Storage (ITS) Service: Code structure"
summary: "The code structure of the service will be as follows:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_its_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_service.html#code-structure"
license: "BSD-3-Clause"
mode: "V"
---

The code structure of the service will be as follows:

TF-M repo:

`interface/`

- `include/psa/internal_trusted_storage.h` - PSA ITS API
- `src/tfm_its_api.c` - PSA ITS API implementation for NSPE

`secure_fw/ns_callable/tfm_veneers.c` - ITS veneers (auto-generated from
manifest)

`secure_fw/partitions/internal_trusted_storage/`

- `tfm_internal_trusted_storage.yaml` - Partition manifest
- `tfm_its_secure_api.c` - PSA ITS API implementation for SPE
- `tfm_its_req_mngr.c` - Uniform secure functions and IPC request handlers
- `tfm_internal_trusted_storage.h` - TF-M ITS API (with client_id parameter)
- `tfm_internal_trusted_storage.c` - TF-M ITS implementation, using the
  flash_fs as a backend
- `its_crypto_interface.h` - APIs for encrypting ITS assets used by ITS implementation  (optional)
- `its_crypto_interface.c` - Implementation for ITS encryption (optional)
- `platform/ext/target/.../tfm_hal_its_encryption.c` - Platform implementation for ITS encryption HAL APIs (optional)
- `flash_fs/` - Filesystem
- `flash/` - Flash interface

tf-m-tests repo:

`test/secure_fw/suites/its/`

- `non_secure/psa_its_ns_interface_testsuite.c` - Non-secure interface tests
- `secure/psa_its_s_interface_testsuite.c` - Secure interface tests


### TF-M ITS implementation

The following APIs will be exposed by `tfm_internal_trusted_storage.h`::
```
psa_status_t tfm_its_init(void);

psa_status_t tfm_its_set(int32_t client_id,
                         psa_storage_uid_t uid,
                         size_t data_length,
                         const void *p_data,
                         psa_storage_create_flags_t create_flags);

psa_status_t tfm_its_get(int32_t client_id,
                         psa_storage_uid_t uid,
                         size_t data_offset,
                         size_t data_size,
                         void *p_data,
                         size_t *p_data_length);

psa_status_t tfm_its_get_info(int32_t client_id,
                              psa_storage_uid_t uid,
                              struct psa_storage_info_t *p_info);

psa_status_t tfm_its_remove(int32_t client_id,
                            psa_storage_uid_t uid);
```
That is, the TF-M ITS APIs will have the same prototypes as the PSA ITS APIs,
but with the addition of a `client_id` parameter, which will be passed from
the ITS request manager. A `tfm_its_init` function will also be present, which
will be called at initialisation time and not exposed through a veneer or SID.

The implementation in `tfm_internal_trusted_storage.c` must validate the
parameters (excepting memory references, which are validated by the SPM),
translate the UID and client ID into a file ID and then make appropriate calls
to the filesystem layer. It must also take care ensure that any PSA Storage
flags associated with the UID are honoured.


### Filesystem

The ITS filesystem will be copied and modified from the SST filesystem. The
modifications required will be to rename symbols from `sst` to `its` and to
update the implementation to be aligned with the latest version of the PSA
Storage spec (which consists mainly of moving to the `psa_status_t` error type
and using common error codes from `psa/error.h`).

The filesystem will also be modified to align the size of each file stored to
the alignment requirement exposed by the flash interface, by adding appropriate
padding.

The filesystem code will be de-duplicated again once the ITS service is
implemented (see below).


### Flash layer

The flash layer will be copied from SST, and modified to direct writes to the
internal flash device. It too needs to be updated to use `psa_status_t` error
types.


### Platform layer

The TF-M platform layer must be be updated to distinguish between the external
flash device used for Protected Storage and internal flash device used for ITS.
A flash region for the relevant storage service needs to be allocated in each.

On test platforms these may just be two distinct regions of the same flash
device, but in general they will separate devices with their own drivers.
