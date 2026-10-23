---
id: "core-using-trustzone-for-armv8-m-cmsis-files-for-trustzone"
type: "concept"
domain: "core"
title: "Using TrustZone for Armv8-M: CMSIS Files for TrustZone"
summary: "The CMSIS-Core files are extended by the header files partition_h_pg and partition_gen_h_pg :"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/using_tz.md#cmsis-files-for-trustzone"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Core files are extended by the header files partition_h_pg and partition_gen_h_pg :

 - The file partition_<Device>.h defines the initial system configuration and during SystemInit in Secure state.
 - The file partition_gen.h is optional and contains SAU region and interrupt target assignments. This file may be generated using CMSIS-Zone.

> **Note**
> - Refer to using_pg for a general description of the CMSIS-Core (Cortex-M) files.

(figure: CMSIS with extensions for TrustZone)
