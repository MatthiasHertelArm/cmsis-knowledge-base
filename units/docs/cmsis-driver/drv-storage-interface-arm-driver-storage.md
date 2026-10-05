---
id: "drv-storage-interface-arm-driver-storage"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_DRIVER_STORAGE"
summary: "This is the set of operations constituting the Storage driver. Their implementation is platform-specific, and needs to be supplied by the porting effort. The functions of the Storage driver are accessed by function pointers exposed by this structure."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_STORAGE
```


This is the set of operations constituting the Storage driver. Their
implementation is platform-specific, and needs to be supplied by the porting
effort. The functions of the Storage driver are accessed by function pointers
exposed by this structure. Refer to StorageDriverFunctions for overview
information.

Each instance of a Storage interface provides such an access structure.
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_Storage0** is the name of the access struct of the first instance (no. 0).
 - **Driver_Storage1** is the name of the access struct of the second instance (no. 1).

A middleware configuration setting allows connecting the middleware to a specific driver instance **%Driver_Flash_n_.**
The default is `0`, which connects a middleware to the first instance of a driver.
******************************************************************************************************************
