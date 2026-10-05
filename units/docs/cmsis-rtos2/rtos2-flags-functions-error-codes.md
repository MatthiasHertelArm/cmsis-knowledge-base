---
id: "rtos2-flags-functions-error-codes"
type: "concept"
domain: "rtos"
title: "Flags Functions Error Codes"
summary: "Constants used by CMSIS_RTOS_ThreadFlagsMgmt and CMSIS_RTOS_EventFlags to return error codes. In case of an error, flags functions (CMSIS_RTOS_ThreadFlagsMgmt and CMSIS_RTOS_EventFlags) return error codes. To indicate that an error has occurred, the highest bit of the return value is be set."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
license: "Apache-2.0"
mode: "V"
---

Constants used by CMSIS_RTOS_ThreadFlagsMgmt and CMSIS_RTOS_EventFlags to return error codes.
 In case of an error, flags functions (CMSIS_RTOS_ThreadFlagsMgmt and
CMSIS_RTOS_EventFlags) return error codes. To indicate that an error has occurred, the highest bit of
the return value is be set. You can check the exact error using the codes shown below.
