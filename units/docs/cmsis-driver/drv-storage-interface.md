---
id: "drv-storage-interface"
type: "concept"
domain: "drivers"
title: "Storage Interface"
summary: "Driver API for Storage Device Interface (%DriverStorage.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for Storage Device Interface (%Driver_Storage.h)

This is an abstraction for a storage controller. It offers an interface to
access an address space of storage locations, comprising APIs for
initialization, erase, access, program, and status-fetch operations. It also
offers APIs to iterate over the available Storage Blocks (\ref
ARM_STORAGE_BLOCK), allowing the discovery of block attributes such as
write/erase granularities. Using the Storage abstraction, it becomes possible to
write generic algorithms, such as block copy, to operate on any conforming
storage device.

**Note:** The storage abstraction layer is not responsible for storage management.
Algorithms such as block-allocation, wear-leveling, erase-before-write and other
storage-management policies are the responsibility of modules external to the
storage abstraction layer. In essence, the storage interface is the lowest
abstraction upon which block management policies can be implemented.

Here's a picture to help locate the storage abstraction in the software stack.
The part below the box labeled 'Storage abstraction layer' is implemented by a
storage driver.



**Storage API**

The following header files define the Application Programming Interface (API) for the Flash interface:
  - **%Driver_Storage.h** : Driver API for Storage Device Interface


**Driver Functions**

The driver functions are published in the access struct as explained in StorageDriverFunctions
  - ARM_DRIVER_STORAGE : access struct for Storage driver functions

A sample use for the driver can be found at: SampleUseOfStorageDriver
******************************************************************************************************************
