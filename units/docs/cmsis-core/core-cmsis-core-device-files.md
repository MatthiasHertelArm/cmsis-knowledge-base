---
id: "core-cmsis-core-device-files"
type: "concept"
domain: "core"
title: "CMSIS-Core Device Files"
summary: "The CMSIS-Core Device Files implement CMSIS-Core support for a specific microcontroller device or family of devices. These files are typically provided by the device vendor and use cmsisstandardfiles via \\#include directives."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_device_files.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_device_files.md"
license: "Apache-2.0"
mode: "V"
---

The **CMSIS-Core Device Files** implement CMSIS-Core support for a specific microcontroller device or family of devices. These files are typically provided by the device vendor and use cmsis_standard_files via \#include directives.

CMSIS-Core specifies the organization of CMSIS-Core Device Files, defines their functionalities, and provides unified naming conventions. This brings   following benefits:
 - Simplified device support for vendors with fast scaling for device families and variants on all Arm Cortex-M cores.
 - Uniform workflows and experience for application developers.

Following CMSIS-Core Device Files are defined:
 - system_c_pg
 - device_h_pg
 - startup_c_pg
 - linker_sct_pg
\if ARMv8M
 - partition_h_pg
 - partition_gen_h_pg
\endif

cmsis_files_dfps explains how to distribute cmsis_device_files in CMSIS-Pack format.
