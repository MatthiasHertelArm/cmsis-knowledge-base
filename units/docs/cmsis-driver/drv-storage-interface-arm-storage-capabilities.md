---
id: "drv-storage-interface-arm-storage-capabilities"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_STORAGE_CAPABILITIES"
summary: "A Storage driver can be implemented with different capabilities. The data fields of this struct encode the API capabilities implemented by this driver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_STORAGE_CAPABILITIES
```


A Storage driver can be implemented with different capabilities. The data fields
of this struct encode the API capabilities implemented by this driver.

The element **asynchronous_ops** indicates if APIs like initialize, read, erase,
program, etc. can operate in asynchronous mode. Having this bit set to 1 means
that the driver is capable of launching asynchronous operations; command
completion for asynchronous operations is signaled by the invocation of a
completion callback. If set to 1, drivers may still complete asynchronous
operations synchronously as necessary--in which case they return a positive
error code to indicate synchronous completion.  If **asynchronous_ops** is not
set, then all such APIs execute synchronously, and control returns to the caller
with a status code only after the completion of the operation (or the discovery
of a failure condition).

The element **erase_all** specifies that the ARM_Storage_EraseAll function
is supported. Typically full chip erase is much faster than erasing the whole
device using **ARM_Storage_Erase.**

**Returned by:**
  - ARM_Storage_GetCapabilities

**Note:**
This data structure is designed to fit within a single word so that it can be
fetched cheaply using a call to driver->GetCapabilities().
******************************************************************************************************************
