---
id: "drv-storage-interface-arm-storage-callback-t"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_Callback_t"
summary: "Provides the typedef for the callback function ARM_Storage_Callback_t."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_Storage_Callback_t
```


Provides the typedef for the callback function ARM_Storage_Callback_t.

\param [in] status
              A code to indicate the status of the completed operation. For data
              transfer operations, the status field is overloaded in case of
              success to return the count of bytes successfully transferred; this
              can be done safely because error codes are negative values.

\param [in] operation
              The command op-code. This value isn't essential, but it is expected that
              this information could be a quick and useful filter for the handler.

**Parameter for:**
  - ARM_Storage_Initialize
******************************************************************************************************************
