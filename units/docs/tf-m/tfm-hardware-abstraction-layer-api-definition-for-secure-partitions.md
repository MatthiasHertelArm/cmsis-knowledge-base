---
id: "tfm-hardware-abstraction-layer-api-definition-for-secure-partitions"
type: "concept"
domain: "security"
title: "Hardware Abstraction Layer: API Definition for Secure Partitions"
summary: "The Secure Partition (SP) HAL mainly focuses on two parts:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/hardware_abstraction_layer.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/hardware_abstraction_layer.html#api-definition-for-secure-partitions"
license: "BSD-3-Clause"
mode: "V"
---

The Secure Partition (SP) `HAL` mainly focuses on two parts:

  - Peripheral devices. The peripherals accessed by the `TF-M` default
    Secure Partitions.
  - Secure Partition abstraction support. The Secure Partition data that must be
    provided by the platform.

The Secure Partition abstraction support will be introduced in the peripheral
API definition.


### ITS and PS flash API

There are two kinds of flash:

  - Internal flash. Accessed by the PSA Internal Trusted Storage (ITS) service.
  - External flash. Accessed by the PSA Protected Storage (PS) service.

The ITS HAL for the internal flash device is defined in the `tfm_hal_its.h`
header and the PS HAL in the `tfm_hal_ps.h` header.


##### Macros


###### Internal Trusted Storage


###### TFM_HAL_ITS_FLASH_DRIVER

Defines the identifier of the CMSIS Flash ARM_DRIVER_FLASH object to use for
ITS. It must have been allocated by the platform and will be declared extern in
the HAL header.


###### TFM_HAL_ITS_PROGRAM_UNIT

Defines the size of the ITS flash device's physical program unit (the smallest
unit of data that can be individually programmed to flash). It must be equal to
TFM_HAL_ITS_FLASH_DRIVER.GetInfo()->program_unit, but made available at compile
time so that filesystem structures can be statically sized.


###### TFM_HAL_ITS_FLASH_AREA_ADDR

Defines the base address of the dedicated flash area for ITS.


###### TFM_HAL_ITS_FLASH_AREA_SIZE

Defines the size of the dedicated flash area for ITS in bytes.


###### TFM_HAL_ITS_SECTORS_PER_BLOCK

Defines the number of contiguous physical flash erase sectors that form a
logical filesystem erase block.


###### Protected Storage


###### TFM_HAL_PS_FLASH_DRIVER

Defines the identifier of the CMSIS Flash ARM_DRIVER_FLASH object to use for
PS. It must have been allocated by the platform and will be declared extern in
the HAL header.


###### TFM_HAL_PS_PROGRAM_UNIT

Defines the size of the PS flash device's physical program unit (the smallest
unit of data that can be individually programmed to flash). It must be equal to
TFM_HAL_PS_FLASH_DRIVER.GetInfo()->program_unit, but made available at compile
time so that filesystem structures can be statically sized.


###### TFM_HAL_PS_FLASH_AREA_ADDR

Defines the base address of the dedicated flash area for PS.


###### TFM_HAL_PS_FLASH_AREA_SIZE

Defines the size of the dedicated flash area for PS in bytes.


###### TFM_HAL_PS_SECTORS_PER_BLOCK

Defines the number of contiguous physical flash erase sectors that form a
logical filesystem erase block.


##### Optional definitions

The `TFM_HAL_ITS_FLASH_AREA_ADDR`, `TFM_HAL_ITS_FLASH_AREA_SIZE` and
`TFM_HAL_ITS_SECTORS_PER_BLOCK` definitions are optional. If not defined, the
platform must implement `tfm_hal_its_fs_info()` instead.

Equivalently, `tfm_hal_its_ps_info()` must be implemented by the platform if
`TFM_HAL_ITS_FLASH_AREA_ADDR`, `TFM_HAL_ITS_FLASH_AREA_SIZE` or
`TFM_HAL_ITS_SECTORS_PER_BLOCK` is not defined.


##### Objects


###### ARM_DRIVER_FLASH

The ITS and PS HAL headers each expose a CMSIS Flash Driver instance.

```c

extern ARM_DRIVER_FLASH TFM_HAL_ITS_FLASH_DRIVER

extern ARM_DRIVER_FLASH TFM_HAL_PS_FLASH_DRIVER
```
The CMSIS Flash Driver provides the flash primitives ReadData(), ProgramData()
and EraseSector() as well as GetInfo() to access flash device properties such
as the sector size.


##### Types


###### tfm_hal_its_fs_info_t

Struct containing information required from the platform at runtime to configure
the ITS filesystem.

```c

struct tfm_hal_its_fs_info_t {
    uint32_t flash_area_addr;
    size_t flash_area_size;
    uint8_t sectors_per_block;
};
```
Each attribute is described below:

  - `flash_area_addr` - Location of the block of flash to use for ITS
  - `flash_area_size` - Number of bytes of flash to use for ITS
  - `sectors_per_block` - Number of erase sectors per logical FS block


###### tfm_hal_ps_fs_info_t

Struct containing information required from the platform at runtime to configure
the PS filesystem.

```c

struct tfm_hal_ps_fs_info_t {
    uint32_t flash_area_addr;
    size_t flash_area_size;
    uint8_t sectors_per_block;
};
```
Each attribute is described below:

  - `flash_area_addr` - Location of the block of flash to use for PS
  - `flash_area_size` - Number of bytes of flash to use for PS
  - `sectors_per_block` - Number of erase sectors per logical FS block


##### Functions


###### tfm_hal_its_fs_info()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_its_fs_info(struct tfm_hal_its_fs_info_t *fs_info);
```
**Description**

Retrieves the filesystem configuration parameters for ITS.

**Parameter**

- `fs_info` - Filesystem config information

**Return values**

- `TFM_HAL_SUCCESS` - The operation completed successfully
- `TFM_HAL_ERROR_INVALID_INPUT` - Invalid parameter

**Note**

This function should ensure that the values returned do not result in a security
compromise. The block of flash supplied must meet the security requirements of
Internal Trusted Storage.


###### tfm_hal_ps_fs_info()

**Prototype**

```c

enum tfm_hal_status_t tfm_hal_ps_fs_info(struct tfm_hal_ps_fs_info_t *fs_info);
```
**Description**

Retrieves the filesystem configuration parameters for PS.

**Parameter**

- `fs_info` - Filesystem config information

**Return values**

- `TFM_HAL_SUCCESS` - The operation completed successfully
- `TFM_HAL_ERROR_INVALID_INPUT` - Invalid parameter

**Note**

This function should ensure that the values returned do not result in a security
compromise.

--------------

*Copyright (c) 2020-2024, Arm Limited. All rights reserved.*
*Copyright (c) 2022 Cypress Semiconductor Corporation (an Infineon company)
or an affiliate of Cypress Semiconductor Corporation. All rights reserved.*
