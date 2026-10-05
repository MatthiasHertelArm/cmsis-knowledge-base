---
id: "drv-mci-interface-arm-mci-setuptransfer"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_SetupTransfer"
summary: "The function ARM_MCI_SetupTransfer prepares the data transfer operation that is initiated by calling the function ARM_MCI_SendCommand with the parameter flags = ARM_MCI_TRANSFER_DATA."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_SetupTransfer (uint8_t  *data, uint32_t block_count, uint32_t block_size, uint32_t mode)
```


The function **ARM_MCI_SetupTransfer** prepares the data transfer operation that is initiated 
by calling the function ARM_MCI_SendCommand with the parameter **flags** = ARM_MCI_TRANSFER_DATA.

The parameter **data** is a pointer to the data to transfer. \n
The parameter **block_count** is the number of blocks to transfer. \n
The parameter **block_size** is the size of a block. \n
The parameter **mode** sets the transfer mode and can have the values liste in the table below:

Transfer Directions                   | Description
:-------------------------------------|:------------
ARM_MCI_TRANSFER_READ            | Read data from MCI
ARM_MCI_TRANSFER_WRITE           | Write data to MCI
ARM_MCI_TRANSFER_BLOCK (default) | Block Data transfer 
ARM_MCI_TRANSFER_STREAM          | Stream Data transfer (MMC only)
                                    
******************************************************************************************************************
