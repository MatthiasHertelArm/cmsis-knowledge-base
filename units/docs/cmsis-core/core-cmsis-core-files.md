---
id: "core-cmsis-core-files"
type: "concept"
domain: "core"
title: "CMSIS-Core Files"
summary: "CMSIS-Core files can be differentiated in two main groups:"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_std_files.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_std_files.md"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core files can be differentiated in two main groups:

 1. cmsis_standard_files are provided by Arm for supported CPU cores as part of the CMSIS-Core software component. These files typically do not require any modifications and are expected to be included via CMSIS-Core device files.
 2. cmsis_device_files are specified in CMSIS-Core methodology, and are typically provided by CPU device vendors to correctly cover their specific functionalities. Some of them may expect additional application-specific changes.

The detailed file structure of the CMSIS-Core files is shown in the following picture.

(figure: CMSIS-Core File Structure)

cmsis_files_dfps explains how cmsis_core_files can be distributed in CMSIS-Pack format.
