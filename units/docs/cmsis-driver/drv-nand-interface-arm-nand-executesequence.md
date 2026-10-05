---
id: "drv-nand-interface-arm-nand-executesequence"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_ExecuteSequence"
summary: "The function ARM_NAND_ExecuteSequence executes a sequence of operations for a NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_ExecuteSequence (uint32_t dev_num, uint32_t code, uint32_t cmd, uint32_t addr_col, uint32_t addr_row, void *data, uint32_t data_cnt, uint8_t *status, uint32_t *count)
```


The function **ARM_NAND_ExecuteSequence** executes a sequence of operations for a NAND device.

The parameter **dev_num** is the device number. \n
The parameter **code** is the sequence encoding as defined in the table **Sequence execution Code**. \n
The parameter **cmd** is the command or a series of commands. \n
The parameter **addr_col** is the column address. \n
The parameter **addr_row** is the row address. \n
The parameter **data** is a pointer to the buffer that stores the data to or loads the data from. \n
The parameter **data_cnt** is the number of data items to read or write in one iteration. \n
The parameter **status** is a pointer to the buffer that stores the status read. \n
The parameter **count** is a pointer to the number of iterations. \n

**ARM_NAND_CODE_xxx** specifies sequence execution codes.

Sequence Execution Code            | Description
:----------------------------------|:--------------------------------------------
ARM_NAND_CODE_SEND_CMD1       | Send Command 1 (cmd[7..0])
ARM_NAND_CODE_SEND_ADDR_COL1  | Send Column Address 1 (addr_col[7..0])
ARM_NAND_CODE_SEND_ADDR_COL2  | Send Column Address 2 (addr_col[15..8])
ARM_NAND_CODE_SEND_ADDR_ROW1  | Send Row Address 1 (addr_row[7..0])
ARM_NAND_CODE_SEND_ADDR_ROW2  | Send Row Address 2 (addr_row[15..8])
ARM_NAND_CODE_SEND_ADDR_ROW3  | Send Row Address 3 (addr_row[23..16])
ARM_NAND_CODE_INC_ADDR_ROW    | Auto-increment Row Address
ARM_NAND_CODE_WRITE_DATA      | Write Data
ARM_NAND_CODE_SEND_CMD2       | Send Command 2 (cmd[15..8])
ARM_NAND_CODE_WAIT_BUSY       | Wait while R/Bn busy
ARM_NAND_CODE_READ_DATA       | Read Data
ARM_NAND_CODE_SEND_CMD3       | Send Command 3 (cmd[23..16])
ARM_NAND_CODE_READ_STATUS     | Read Status byte and check FAIL bit (bit 0)
ARM_NAND_ECC(n)               | Select ECC
ARM_NAND_ECC0                 | Use ECC0 of selected ECC
ARM_NAND_ECC1                 | Use ECC1 of selected ECC
ARM_NAND_DRIVER_DONE_EVENT    | Generate ARM_NAND_EVENT_DRIVER_DONE

The data item size is defined by the data type, which depends on the configured data bus width.

Data type is:
 - **uint8_t** for 8-bit data bus
 - **uint16_t** for 16-bit data bus

The function is non-blocking and returns as soon as the driver has started executing the specified sequence.
When the operation is completed, the ARM_NAND_EVENT_DRIVER_DONE event is generated (if enabled by **ARM_NAND_DRIVER_DONE_EVENT).**
Progress of the operation can also be monitored by calling the ARM_NAND_GetStatus function and checking the **busy** data field.

Driver executes the number of specified iterations where in each iteration 
items specified by **ARM_NAND_CODE_xxx** are executed in the order as listed in the table **Sequence execution Code**.
The parameter **count** is holding the current number of iterations left.

Execution is automatically aborted and ARM_NAND_EVENT_DRIVER_DONE event is generated (if enabled by **ARM_NAND_DRIVER_DONE_EVENT):**
 - if Read Status is enabled and the FAIL bit (bit 0) is set
 - if ECC is used and ECC fails (also sets ARM_NAND_EVENT_ECC_ERROR event)

**Note:**
ARM_NAND_CODE_WAIT_BUSY can only be specified if the Device Ready event can be generated (reported by **event_device_ready** in ARM_NAND_CAPABILITIES).
The event ARM_NAND_EVENT_DEVICE_READY is not generated during sequence execution but rather used internally by the driver.
******************************************************************************************************************
