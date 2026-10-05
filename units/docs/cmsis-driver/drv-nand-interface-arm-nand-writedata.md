---
id: "drv-nand-interface-arm-nand-writedata"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_WriteData"
summary: "The function ARMNANDWriteData writes data to a NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_WriteData (uint32_t dev_num, const void *data, uint32_t cnt, uint32_t mode)
```


The function **ARM_NAND_WriteData** writes data to a NAND device.

The parameter **dev_num** is the device number. \n
The parameter **data** is a pointer to the buffer with data to write. \n
The parameter **cnt** is the number of data items to write. \n
The parameter **mode** defines the operation mode as listed in the table below.

Write Data Mode                    | Description
:----------------------------------|:--------------------------------------------
ARM_NAND_ECC(n)               | Select ECC
ARM_NAND_ECC0                 | Use ECC0 of selected ECC
ARM_NAND_ECC1                 | Use ECC1 of selected ECC
ARM_NAND_DRIVER_DONE_EVENT    | Generate ARM_NAND_EVENT_DRIVER_DONE

The data item size is defined by the data type, which depends on the configured data bus width.

Data type is:
 - **uint8_t** for 8-bit data bus
 - **uint16_t** for 16-bit data bus

The function executes in the following ways:
 - When the operation is blocking (typical for devices connected to memory bus when not using DMA), 
   then the function returns after all data is written and returns the number of data items written.
 - When the operation is non-blocking (typical for NAND controllers), then the function only starts the operation 
   and returns with zero number of data items written. After the operation is completed, 
   the ARM_NAND_EVENT_DRIVER_DONE event is generated (if enabled by **ARM_NAND_DRIVER_DONE_EVENT).**
   Progress of the operation can also be monitored by calling the ARM_NAND_GetStatus function and checking the **busy** data field.
   Operation is automatically aborted if ECC is used and ECC generation fails, 
   which generates the ARM_NAND_EVENT_ECC_ERROR event (together with ARM_NAND_DRIVER_DONE_EVENT if enabled).
******************************************************************************************************************
