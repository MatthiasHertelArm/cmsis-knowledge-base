---
id: "drv-storage-interface-arm-storage-initialize"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_Initialize"
summary: "The function ARMStorageInitialize is called when the middleware component starts operation. In addition to bringing the controller to a ready state, Initialize() receives a callback handler to be invoked upon completion of asynchronous operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_Initialize (ARM_Storage_Callback_t callback)
```


The function **ARM_Storage_Initialize** is called when the middleware component starts
operation. In addition to bringing the controller to a ready state,
Initialize() receives a callback handler to be invoked upon completion of
asynchronous operations.

ARM_Storage_Initialize() needs to be called explicitly before
powering the peripheral using ARM_Storage_PowerControl(), and before initiating other
accesses to the storage controller.

The function performs the following operations:
 - Initializes the resources needed for the Storage interface.
 - Registers the ARM_Storage_Callback_t callback function.

To start working with a peripheral the functions ARM_Storage_Initialize and ARM_Storage_PowerControl() need to be called in this order:
```
   drv->Initialize (...);              // Allocate I/O pins
   drv->PowerControl (ARM_POWER_FULL); // Power up peripheral, setup IRQ/DMA
```

- ARM_Storage_Initialize() typically allocates the I/O resources (pins) for the
 peripheral. The function can be called multiple times; if the I/O resources
 are already initialized it performs no operation and just returns with
 ARM_DRIVER_OK.

- ARM_Storage_PowerControl (ARM_POWER_FULL) sets the peripheral registers including
 interrupt (NVIC) and optionally DMA. The function can be called multiple
 times; if the registers are already set it performs no operation and just
 returns with ARM_DRIVER_OK.

To stop working with a peripheral the functions ARM_Storage_PowerControl() and ARM_Storage_Uninitialize() need to be called in this order:
```
   drv->PowerControl (ARM_POWER_OFF); // Terminate any pending transfers, reset IRQ/DMA, power off peripheral
   drv->Uninitialize (...);           // Release I/O pins
```

The functions ARM_Storage_PowerControl() and ARM_Storage_Uninitialize() always execute and can be used
to put the peripheral into a Safe State, for example after any data
transmission errors. To restart the peripheral in an error condition,
you should first execute the Stop Sequence and then the Start Sequence.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.
******************************************************************************************************************
