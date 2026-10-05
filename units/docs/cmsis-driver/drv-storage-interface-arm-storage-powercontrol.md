---
id: "drv-storage-interface-arm-storage-powercontrol"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_PowerControl"
summary: "The function ARM_Storage_PowerControl operates the power modes of the Storage interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_PowerControl (ARM_POWER_STATE state)
```


The function **ARM_Storage_PowerControl** operates the power modes of the Storage interface.

To start working with a peripheral the functions Initialize and PowerControl need to be called in this order:
```
   drv->Initialize (...);                 // Allocate I/O pins
   drv->PowerControl (ARM_POWER_FULL);    // Power up peripheral, setup IRQ/DMA
```

- ARM_Storage_Initialize() typically allocates the I/O resources (pins) for the
 peripheral. The function can be called multiple times; if the I/O resources
 are already initialized it performs no operation and just returns with
 ARM_DRIVER_OK.

- PowerControl (ARM_POWER_FULL) sets the peripheral registers including
 interrupt (NVIC) and optionally DMA. The function can be called multiple
 times; if the registers are already set it performs no operation and just
 returns with ARM_DRIVER_OK.

To stop working with a peripheral the functions PowerControl and Uninitialize need to be called in this order:
```
   drv->PowerControl (ARM_POWER_OFF);     // Terminate any pending transfers, reset IRQ/DMA, power off peripheral
   drv->Uninitialize (...);               // Release I/O pins
```

The functions ARM_Storage_PowerControl and ARM_Storage_Uninitialize always execute and can be used
to put the peripheral into a Safe State, for example after any data
transmission errors. To restart the peripheral in an error condition,
you should first execute the Stop Sequence and then the Start Sequence.

The parameter **state** can have the following values:
  - ARM_POWER_FULL : set-up the Storage device for data transfers, enable interrupts (NVIC) and optionally DMA. Can be called multiple times.
                          If the device is already in this mode, then the function performs no operation and returns with ARM_DRIVER_OK.
  - ARM_POWER_LOW : may use power saving. Returns ARM_DRIVER_ERROR_UNSUPPORTED when not implemented.
  - ARM_POWER_OFF : terminates any pending data transfers, disables peripheral, disables related interrupts and DMA.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.
******************************************************************************************************************
