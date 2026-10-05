---
id: "core-trustzone-setup-partition-device-h"
type: "concept"
domain: "core"
title: "TrustZone setup: partition_<Device>.h"
summary: "The TrustZone header file contains the initial setup of the TrustZone hardware in an Armv8-M system."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_partition_device_h.md"
license: "Apache-2.0"
mode: "V"
---

The TrustZone header file contains the initial setup of the TrustZone hardware in an Armv8-M system.

This file implements the function TZ_SAU_Setup that is called from SystemInit. It uses settings in these files:

 - partition_<Device>.h that defines the initial system configuration and during SystemInit in Secure state.
 - partition_gen.h that contains SAU region and interrupt target assignments. This file may be generated using [CMSIS-Zone](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/../Zone/index.html).

> **Note**
> - partition_gen.h is optional and can be generated using [CMSIS-Zone](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/../Zone/index.html). In previous versions of CMSIS-Core(M) this settings were part of partition_<Device>.h.

The partition_<Device>.h file contains the following configuration settings for:

 - sau_ctrlregister_sec provides settings for the SAU CTRL register.
 - sau_sleepexception_sec provides device-specific deep-sleep and exception settings.
 - sau_fpu_sec defines the usage of the Floating Point Unit in secure and non-secure state.

The partition_<Device>.h file includes the partition_gen.h file with configuration settings for:

 - sau_regions_sect provides configuration of the SAU Address Regions.
 - sau_interrupttarget_sec provides device-specific interrupt target settings.
