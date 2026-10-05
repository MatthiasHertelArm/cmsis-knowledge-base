---
id: "drv-use-of-storage-apis"
type: "concept"
domain: "drivers"
title: "Use of Storage APIs"
summary: "Function pointers within ARM_DRIVER_STORAGE form the set of operations constituting the Storage driver. Their implementation is platform-specific, and needs to be supplied by the porting effort."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

Function pointers within ARM_DRIVER_STORAGE form the set of operations
constituting the Storage driver. Their implementation is platform-specific, and
needs to be supplied by the porting effort.

Some of these APIs will always operate synchronously:
- ARM_Storage_GetVersion
- ARM_Storage_GetCapabilities
- ARM_Storage_GetStatus
- ARM_Storage_GetInfo
- ARM_Storage_ResolveAddress
- ARM_Storage_GetNextBlock and
- ARM_Storage_GetBlock.

This means that control returns to the caller with a relevant status code only after the completion of the operation (or
the discovery of a failure condition).

The remainder of the APIs:
- ARM_Storage_Initialize
- ARM_Storage_Uninitialize
- ARM_Storage_PowerControl
- ARM_Storage_ReadData
- ARM_Storage_ProgramData
- ARM_Storage_Erase and
- ARM_Storage_EraseAll

can function asynchronously if the underlying controller supports it; that is if ARM_STORAGE_CAPABILITIES::asynchronous_ops
is set. In the case of asynchronous operation, the invocation returns early (with ARM_DRIVER_OK) and results in a completion
callback later. If ARM_STORAGE_CAPABILITIES::asynchronous_ops is not set, then all such APIs execute synchronously, and
control returns to the caller with a status code only after the completion of the operation (or the discovery of a failure
condition).

If ARM_STORAGE_CAPABILITIES::asynchronous_ops is set, a storage driver may
still choose to execute asynchronous operations in a synchronous manner. If
so, the driver returns a positive value to indicate successful synchronous
completion (or an error code in case of failure) and no further invocation of
completion callback should be expected. The expected return value for
synchronous completion of such asynchronous operations varies depending on
the operation. For operations involving data access, it often equals the
amount of data transferred or affected. For non data-transfer operations,
such as EraseAll or Initialize, it is usually 1.

Here's a code snippet to suggest how asynchronous APIs might be used by
callers to handle both synchronous and asynchronous execution by the
underlying storage driver:
```
    ASSERT(ARM_DRIVER_OK == 0); // this is a precondition; it doesn't need to be put in code
    
    int32_t returnValue = drv->asynchronousAPI(...);
         
    if (returnValue < ARM_DRIVER_OK) {
        // handle error.
        
    } else if (returnValue == ARM_DRIVER_OK) {
        ASSERT(drv->GetCapabilities().asynchronous_ops == 1);
        // handle early return from asynchronous execution; remainder of the work is done in the callback handler.
        
    } else {
        ASSERT(returnValue == EXPECTED_RETURN_VALUE_FOR_SYNCHRONOUS_COMPLETION);
        // handle synchronous completion.
    }
```

This example is mixing synchronous and asynchronous APIs: SampleUseOfStorageDriver
******************************************************************************************************************
