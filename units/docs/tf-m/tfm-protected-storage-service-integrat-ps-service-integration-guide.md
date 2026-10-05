---
id: "tfm-protected-storage-service-integrat-ps-service-integration-guide"
type: "concept"
domain: "security"
title: "Protected Storage Service Integration Guide: PS Service Integration Guide"
summary: "This section describes mandatory (i.e. must implement) or optional (i.e. may implement) interfaces which the system integrator have to take in to account in order to integrate the protected storage service in a new platform."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_ps_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_ps_integration_guide.html#ps-service-integration-guide"
license: "BSD-3-Clause"
mode: "V"
---

This section describes mandatory (i.e. **must** implement) or optional
(i.e. **may** implement) interfaces which the system integrator have to take
in to account in order to integrate the protected storage service in a new
platform.


### Maximum Asset Size

An asset is stored in a contiguous space in a block/sector. The maximum
size of an asset can be up-to the size of the data block/sector minus the object
header size (`PS_OBJECT_HEADER_SIZE`) which is defined in
`ps_object_defs.h`. The `PS_OBJECT_HEADER_SIZE` changes based on the
`PS_ENCRYPTION` flag status.


### Protected Storage Service HAL

The PS service requires the platform to implement the PS HAL, defined in
`platform/include/tfm_hal_ps.h`.

The following C definitions in the HAL are mandatory, and must be defined by the
platform in a header named `flash_layout.h`:

- `TFM_HAL_PS_FLASH_DRIVER` - Defines the identifier of the CMSIS Flash
  ARM_DRIVER_FLASH object to use for PS. It must have been allocated by the
  platform and will be declared extern in the HAL header.

- `TFM_HAL_PS_PROGRAM_UNIT` - Defines the size of the PS flash device's
  physical program unit (the smallest unit of data that can be individually
  programmed to flash). It must be equal to
  `TFM_HAL_PS_FLASH_DRIVER.GetInfo()->program_unit`, but made available at
  compile time so that filesystem structures can be statically sized. Valid
  values are powers of two between 1 and the flash sector size, inclusive.

The following C definitions in the HAL may optionally be defined by the platform
in the `flash_layout.h` header:

- `TFM_HAL_PS_FLASH_AREA_ADDR` - Defines the base address of the dedicated
  flash area for PS.

- `TFM_HAL_PS_FLASH_AREA_SIZE` - Defines the size of the dedicated flash area
  for PS in bytes.

- `TFM_HAL_PS_SECTORS_PER_BLOCK` - Defines the number of contiguous physical
  flash erase sectors that form a logical erase block in the filesystem. The
  typical value is `1`, but it may be increased so that the maximum required
  asset size will fit in one logical block.

If any of the above definitions are not provided by the platform, then the
`tfm_hal_ps_fs_info()` HAL API must be implemented instead. This function is
documented in `tfm_hal_ps.h`.

The sectors reserved to be used for Protected Storage **must** be contiguous
sectors starting at `TFM_HAL_PS_FLASH_AREA_ADDR`.

The design requires either 2 blocks, or any number of blocks greater than or
equal to 4. Total number of blocks can not be 0, 1 or 3. This is a design choice
limitation to provide power failure safe update operations.


### Protected Storage Service Optional Platform Definitions

The following optional platform definitions may be defined in
`flash_layout.h`:

- `PS_RAM_FS_SIZE` - Defines the size of the RAM FS buffer when using the
  RAM FS emulated flash implementation. The buffer must be at least as large as
  the area earmarked for the filesystem by the HAL.
- `PS_FLASH_NAND_BUF_SIZE` - Defines the size of the write buffer when using
  the NAND flash implementation. The buffer must be at least as large as a
  logical filesystem block.

More information about the `flash_layout.h` content, not ITS related, is
available in platform_ext_folder along with other
platform information.


### TF-M NV Counter Interface

To have a platform independent way to access the NV counters, TF-M defines a
platform NV counter interface. For API specification, please check:
`platform/include/tfm_plat_nv_counters.h`

The system integrators **may** implement this interface based on the target
capabilities and set the `PS_ROLLBACK_PROTECTION` flag to compile in
the rollback protection code.

If this flag is enabled, the lifecycle of the PS service depends on the
shorter write endurance of the assets storage device and the NV counters
storage device.

### Secret Platform Unique Key

The encryption policy relies on a secret hardware unique key (HUK) per device.
It is system integrator's responsibility to provide an implementation which
**must** be a non-mutable target implementation.
For API specification, please check:
`platform/include/tfm_plat_crypto_keys.h`

A stub implementation is provided in
`platform/ext/common/template/crypto_keys.c`


### Non-Secure Identity Manager

TF-M core tracks the current client IDs running in the secure or non-secure
processing environment. It provides a dedicated API to retrieve the client ID
which performs the service request.

Non-secure Client Extension Integration Guide
provides further details on how client identification works.

PS service uses that TF-M core API to retrieve the client ID and associate it
as the owner of an asset. Only the owner can read, write or delete that asset
based on the creation flags.

The integration guide
provides further details of non-secure implementation requirements for TF-M.


### Cryptographic Interface

The reference encryption policy is built on AES-GCM, and it **may** be replaced
by a vendor specific implementation.

The PS service abstracts all the cryptographic requirements and specifies the
required cryptographic interface in
`secure_fw/partitions/protected_storage/crypto/ps_crypto_interface.h`

The PS service cryptographic operations are implemented in
`secure_fw/partitions/protected_storage/crypto/ps_crypto_interface.c`, using
calls to the TF-M Crypto service.


### PS Service Build Definitions

The PS service uses a set of C definitions to compile in/out certain features,
as well as to configure certain service parameters. When using the TF-M build
system, these definitions are controlled by build flags of the same name. The
`config/config_base.cmake` file sets the default values of those flags, but
they can be overwritten based on platform capabilities by setting them in
`platform/ext/target/<TARGET_NAME>/config.cmake`. The list of PS service build
definitions is:

- `PS_ENCRYPTION`- this flag allows to enable/disable encryption
  option to encrypt the protected storage data.

- `PS_CRYPTO_AEAD_ALG` - this flag indicates the AEAD algorithm to use for
  authenticated encryption in Protected Storage.

For GCM/CCM it is essential that IV doesn't get repeated. If this flag is
set to `PSA_ALG_GCM` or `PSA_ALG_CCM`, `PS_ROLLBACK_PROTECTION` must
be enabled to protect against IV rollback.
- `PS_CREATE_FLASH_LAYOUT`- this flag indicates that it is required
  to create a PS flash layout. If this flag is set, PS service will
  generate an empty and valid PS flash layout to store assets. It will
  erase all data located in the assigned PS memory area before generating
  the PS layout.  This flag is required to be set if the PS memory area
  is located in a non-persistent memory.  This flag can be set if the PS
  memory area is located in a persistent memory without a valid PS flash
  layout in it. That is the case when it is the first time in the device
  life that the PS service is executed.
- `PS_VALIDATE_METADATA_FROM_FLASH`- this flag allows to
  enable/disable the validation mechanism to check the metadata store in flash
  every time the flash data is read from flash. This validation is required
  if the flash is not hardware protected against malicious writes. In case
  the flash is protected against malicious writes (i.e embedded flash, etc),
  this validation can be disabled in order to reduce the validation overhead.
- `PS_ROLLBACK_PROTECTION`- this flag allows to enable/disable
  rollback protection in protected storage service. This flag takes effect only
  if the target has non-volatile counters and `PS_ENCRYPTION` flag is on.
- `PS_AES_KEY_USAGE_LIMIT` - setting this to a value other than zero limits
  the number of AES blocks that will be encrypted/decrypted using any one key.
  When the limit is reached for a given object, a new key will be derived and
  the data will be encrypted with the new key before being stored.
  Note that setting this limit too low may reduce the maximum asset size
  because PS will reject objects that are too large to be encrypted and
  decrypted without hitting this limit.
- `PS_RAM_FS`- setting this flag to `ON` enables the use of RAM instead of
  the persistent storage device to store the FS in the Protected Storage
  service. This flag is `OFF` by default. The PS regression tests write/erase
  storage multiple time, so enabling this flag can increase the life of flash
  memory when testing.
  If this flag is set to `ON`, PS_RAM_FS_SIZE must also be provided. This
  specifies the size of the block of RAM to be used to simulate the flash.

If this flag is disabled when running the regression tests, then it is
recommended that the persistent storage area is erased before running the
tests to ensure that all tests can run to completion. The type of persistent
storage area is platform specific (eFlash, MRAM, etc.) and it is described
in corresponding flash_layout.h
- `PS_MAX_ASSET_SIZE` - Defines the maximum asset size to be stored in the
  PS area. This size is used to define the temporary buffers used by PS to
  read/write the asset content from/to flash. The memory used by the temporary
  buffers is allocated statically as PS does not use dynamic memory allocation.
- `PS_NUM_ASSETS` - Defines the maximum number of assets to be stored in the
  PS area. This number is used to dimension statically the object table size in
  RAM (fast access) and flash (persistent storage). The memory used by the
  object table is allocated statically as PS does not use dynamic memory
  allocation.
- `PS_TEST_NV_COUNTERS`- this flag enables the virtual implementation of the
  PS NV counters interface in `test/secure_fw/suites/ps/secure/nv_counters` of
  the `tf-m-tests` repo, which emulates NV counters in
  RAM, and disables the hardware implementation of NV counters provided by
  the secure service. This flag is enabled by default, but has no effect when
  the secure regression test is disabled. This flag can be
  overridden to `OFF` when building the regression tests. In this case,
  the PS rollback protection test suite will not be built, as it relies
  on extra functionality provided by the virtual NV counters to simulate
  different rollback scenarios. The remainder of the PS test suites will
  run using the hardware NV counters. Please note that running the tests in
  this configuration will quickly increase the hardware NV counter values,
  which cannot be decreased again.
  Overriding this flag from its default value of `OFF` when not
  building the regression tests is not currently supported.
- `PS_STACK_SIZE`- Defines the stack size of the Protected Storage Secure
  Partition. This value mainly depends on the build type(debug, release and
  minisizerel) and compiler.

--------------

*Copyright (c) 2018-2024, Arm Limited. All rights reserved.*
*Copyright (c) 2020, Cypress Semiconductor Corporation. All rights reserved.*
