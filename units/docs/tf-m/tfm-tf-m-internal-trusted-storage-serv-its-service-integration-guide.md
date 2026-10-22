---
id: "tfm-tf-m-internal-trusted-storage-serv-its-service-integration-guide"
type: "concept"
domain: "security"
title: "TF-M Internal Trusted Storage Service Integration Guide: ITS Service Integration Guide"
summary: "This section describes mandatory (i.e. must implement) or optional (i.e. may implement) interfaces which the system integrator has to take in to account in order to integrate the internal trusted storage service in a new platform."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_its_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_its_integration_guide.html#its-service-integration-guide"
license: "BSD-3-Clause"
mode: "V"
---

This section describes mandatory (i.e. **must** implement) or optional
(i.e. **may** implement) interfaces which the system integrator has to take in
to account in order to integrate the internal trusted storage service in a new
platform.


### Flash Interface

For ITS service operations, a contiguous set of blocks must be earmarked for
the internal trusted storage area. The design requires either 2 blocks, or any
number of blocks greater than or equal to 4. Total number of blocks can not be
0, 1 or 3. This is a design choice limitation to provide power failure safe
update operations.


### Maximum Asset Size

An asset is stored in a contiguous space in a logical filesystem block. The
maximum size of an asset can be up-to the size of the data block. Typically,
each logical block corresponds to one physical flash erase sector (the smallest
unit that can erased), but the `TFM_HAL_ITS_SECTORS_PER_BLOCK` configuration
below allows a number of contiguous erase sectors to form one logical block.


### Internal Trusted Storage Service HAL

The ITS service requires the platform to implement the ITS HAL, defined in
`platform/include/tfm_hal_its.h`.

The following C definitions in the HAL are mandatory, and must be defined by the
platform in a header named `flash_layout.h`:

- `TFM_HAL_ITS_FLASH_DRIVER` - Defines the identifier of the CMSIS Flash
  ARM_DRIVER_FLASH object to use for ITS. It must have been allocated by the
  platform and will be declared extern in the HAL header.

- `TFM_HAL_ITS_PROGRAM_UNIT` - Defines the size of the ITS flash device's
  physical program unit (the smallest unit of data that can be individually
  programmed to flash). It must be equal to
  `TFM_HAL_ITS_FLASH_DRIVER.GetInfo()->program_unit`, but made available at
  compile time so that filesystem structures can be statically sized. Valid
  values are powers of two between 1 and the flash sector size, inclusive.

The following C definitions in the HAL may optionally be defined by the platform
in the `flash_layout.h` header:

- `TFM_HAL_ITS_FLASH_AREA_ADDR` - Defines the base address of the dedicated
  flash area for ITS.

- `TFM_HAL_ITS_FLASH_AREA_SIZE` - Defines the size of the dedicated flash area
  for ITS in bytes.

- `TFM_HAL_ITS_SECTORS_PER_BLOCK` - Defines the number of contiguous physical
  flash erase sectors that form a logical erase block in the filesystem. The
  typical value is `1`, but it may be increased so that the maximum required
  asset size will fit in one logical block.

If any of the above definitions are not provided by the platform, then the
`tfm_hal_its_fs_info()` HAL API must be implemented instead. This function is
documented in `tfm_hal_its.h`.

The sectors reserved to be used for Internal Trusted Storage **must** be
contiguous.


### Internal Trusted Storage Service Optional Platform Definitions

The following optional platform definitions may be defined in
`flash_layout.h`:

- `ITS_RAM_FS_SIZE` - Defines the size of the RAM FS buffer when using the
  RAM FS emulated flash implementation. The buffer must be at least as large as
  the area earmarked for the filesystem by the HAL.
- `ITS_FLASH_NAND_BUF_SIZE` - Defines the size of the write buffer when using
  the NAND flash implementation. The buffer must be at least as large as a
  logical filesystem block.
- `ITS_MAX_BLOCK_DATA_COPY` - Defines the buffer size used when copying data
  between blocks, in bytes. If not provided, defaults to 256. Increasing this
  value will increase the memory footprint of the service.

More information about the `flash_layout.h` content, not ITS related, is
available in platform_ext_folder along with other
platform information.


### ITS Service Build Definitions

The ITS service uses a set of C definitions to compile in/out certain features,
as well as to configure certain service parameters. When using the TF-M build
system, these definitions are controlled by build flags of the same name. The
`config/config_base.cmake` file sets the default values of those flags, but
they can be overwritten based on platform capabilities by setting them in
`platform/ext/target/<TARGET_NAME>/config.cmake`. The list of ITS service
build definitions is:

- `ITS_CREATE_FLASH_LAYOUT`- this flag indicates that it is required
  to create an ITS flash layout. If this flag is set, ITS service will
  generate an empty and valid ITS flash layout to store assets. It will
  erase all data located in the assigned ITS memory area before generating
  the ITS layout. This flag is required to be set if the ITS memory area
  is located in a non-persistent memory. This flag can be set if the ITS
  memory area is located in a persistent memory without a valid ITS flash
  layout in it. That is the case when it is the first time in the device
  life that the ITS service is executed.
- `ITS_VALIDATE_METADATA_FROM_FLASH`- this flag allows to
  enable/disable the validation mechanism to check the metadata store in flash
  every time the flash data is read from flash. This validation is required
  if the flash is not hardware protected against data corruption.
- `ITS_RAM_FS`- setting this flag to `ON` enables the use of RAM instead of
  the persistent storage device to store the FS in the Internal Trusted Storage
  service. This flag is `OFF` by default. The ITS regression tests write/erase
  storage multiple time, so enabling this flag can increase the life of flash
  memory when testing.
  If this flag is set to `ON`, ITS_RAM_FS_SIZE must also be provided. This
  specifies the size of the block of RAM to be used to simulate the flash.

If this flag is disabled when running the regression tests, then it is
recommended that the persistent storage area is erased before running the
tests to ensure that all tests can run to completion. The type of persistent
storage area is platform specific (eFlash, MRAM, etc.) and it is described
in corresponding flash_layout.h
- `ITS_MAX_ASSET_SIZE` - Defines the maximum asset size to be stored in the
  ITS area. This size is used to define the temporary buffers used by ITS to
  read/write the asset content from/to flash. The memory used by the temporary
  buffers is allocated statically as ITS does not use dynamic memory allocation.
- `ITS_NUM_ASSETS` - Defines the maximum number of assets to be stored in the
  ITS area. This number is used to dimension statically the filesystem metadata
  tables in RAM (fast access) and flash (persistent storage). The memory used by
  the filesystem metadata tables is allocated statically as ITS does not use
  dynamic memory allocation.
- `ITS_BUF_SIZE`- Defines the size of the partition's internal data transfer
  buffer. If not provided, then `ITS_MAX_ASSET_SIZE` is used to allow asset
  data to be copied between the client and the filesystem in one iteration.
  Reducing the buffer size will decrease the RAM usage of the partition at the
  expense of latency, as data will be copied in multiple iterations. *Note:*
  when data is copied in multiple iterations, the atomicity property of the
  filesystem is lost in the case of an asynchronous power failure.
- `ITS_STACK_SIZE`- Defines the stack size of the Internal Trusted Storage
  Secure Partition. This value mainly depends on the platform specific flash
  drivers, the build type (Debug, Release and MinSizeRel) and compiler.

--------------

*Copyright (c) 2019-2022, Arm Limited. All rights reserved.*
*Copyright (c) 2020, Cypress Semiconductor Corporation. All rights reserved.*
