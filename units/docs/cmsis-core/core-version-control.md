---
id: "core-version-control"
type: "concept"
domain: "core"
title: "Version Control"
summary: "Version \\#define symbols for CMSIS release specific C/C++ source code"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_version_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_version_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

Version \#define symbols for CMSIS release specific C/C++ source code


cmsis_processor_files contain macros __CORTEX_M , __CORTEX_SC or __STAR_MC that identify the processor core variant described in the file.

Additionally each processor header file includes the **cmsis_version.h** file with __CM_CMSIS_VERSION define that identifies the CMSIS version used.

This allows application code and middleware components to verify the target processor and the CMSIS version that CMSIS-Core component implies.
