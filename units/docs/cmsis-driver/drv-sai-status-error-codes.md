---
id: "drv-sai-status-error-codes"
type: "concept"
domain: "drivers"
title: "SAI Status Error Codes"
summary: "Negative values indicate errors (SAI has specific codes in addition to common executionstatus)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

Negative values indicate errors (SAI has specific codes in addition to common execution_status). 
 
The SAI driver has additional status error codes that are listed below.
**Note:**
- In case multiple errors exist, only the first encountered error will be reported.
- errors ARM_SAI_ERROR_BIT_ORDER, ARM_SAI_ERROR_FRAME_SYNC_xxx, ARM_SAI_ERROR_SLOT_xxx will only be reported in Driver_SAI_User mode.
- The SAI driver also returns the common execution_status.
