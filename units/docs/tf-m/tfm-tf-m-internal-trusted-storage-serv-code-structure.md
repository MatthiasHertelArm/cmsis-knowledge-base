---
id: "tfm-tf-m-internal-trusted-storage-serv-code-structure"
type: "concept"
domain: "security"
title: "TF-M Internal Trusted Storage Service Integration Guide: Code Structure"
summary: "TF-M Internal Trusted Storage service code is located in secure_fw/partitions/internal_trusted_storage/ and is divided as follows:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_its_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_its_integration_guide.html#code-structure"
license: "BSD-3-Clause"
mode: "V"
---

TF-M Internal Trusted Storage service code is located in
`secure_fw/partitions/internal_trusted_storage/` and is divided as follows:

    - Core files
    - Flash filesystem interfaces
    - Flash interfaces

The PSA ITS interfaces for the TF-M ITS service are located in
`interface/include/psa`.


### PSA Internal Trusted Storage Interfaces


The TF-M ITS service exposes the following mandatory PSA ITS interfaces
version 1.0:

```c

psa_status_t psa_its_set(psa_storage_uid_t uid, size_t data_length, const void *p_data, psa_storage_create_flags_t create_flags);
psa_status_t psa_its_get(psa_storage_uid_t uid, size_t data_offset, size_t data_size, void *p_data, size_t *p_data_length);
psa_status_t psa_its_get_info(psa_storage_uid_t uid, struct psa_storage_info_t *p_info);
psa_status_t psa_its_remove(psa_storage_uid_t uid);
```
These PSA ITS interfaces and TF-M ITS types are defined and documented in
`interface/include/psa/storage_common.h`,
`interface/include/psa/internal_trusted_storage.h`, and
`interface/include/tfm_its_defs.h`


### Core Files

- `tfm_its_req_mngr.c` - Contains the ITS request manager implementation which
  handles all requests which arrive to the service. This layer extracts the
  arguments from the input and output vectors, and it calls the internal trusted
  storage layer with the provided parameters.

- `tfm_internal_trusted_storage.c` - Contains the TF-M internal trusted
  storage API implementations which are the entry points to the ITS service.
  Constructs a filesystem configuration using information from the ITS HAL,
  allocates a filesystem context for ITS and makes appropriate FS calls. Also
  handles requests from the PS partition with a separate FS config and context.

- `its_utils.c` - Contains common and basic functionalities used across the
  ITS service code.


### Flash Filesystem Interface

- `flash_fs/its_flash_fs.h` - Abstracts the flash filesystem operations used
  by the internal trusted storage service. The purpose of this abstraction is to
  have the ability to plug-in other filesystems or filesystem proxies
  (supplicant).

- `flash_fs/its_flash_fs.c` - Contains the `its_flash_fs` implementation for
  the required interfaces.

- `flash_fs/its_flash_fs_mblock.c` - Contains the metadata block manipulation
  functions required to implement the `its_flash_fs` interfaces in
  `flash_fs/its_flash_fs.c`.

- `flash_fs/its_flash_fs_dblock.c` - Contains the data block manipulation
  functions required to implement the `its_flash_fs` interfaces in
  `flash_fs/its_flash_fs.c`.

The system integrator **may** replace this implementation with its own
flash filesystem implementation or filesystem proxy (supplicant).


### Flash Interface

The ITS filesystem flash interface is defined by `struct its_flash_fs_ops_t`
in `flash_fs/its_flash_fs.h`.

Implementations of the ITS filesystem flash interface for different types of
storage can be found in the ``internal_trusted_storage/flash` directory.

- `flash/its_flash.h` - Helper header that includes the correct ITS flash
  interface implementation for the target, and abstracts the allocation of
  different flash device types.

- `flash/its_flash_nand.c` - Implements the ITS flash interface for a NAND
  flash device, on top of the CMSIS flash interface implemented by the target.
  This implementation writes entire block updates in one-shot, so the CMSIS
  flash implementation **must** be able to detect incomplete writes and return
  an error the next time the block is read.

- `flash/its_flash_nor.c` - Implements the ITS flash interface for a NOR flash
  device, on top of the CMSIS flash interface implemented by the target.

- `flash/its_flash_ram.c` - Implements the ITS flash interface for an emulated
  flash device using RAM, on top of the CMSIS flash interface implemented by the
  target.

The CMSIS flash interface **must** be implemented for each target based on its
flash controller.

The ITS flash interface depends on target-specific definitions from
`platform/ext/target/<TARGET_NAME>/partition/flash_layout.h`.
Please see the `Internal Trusted Storage Service HAL` section for details.
