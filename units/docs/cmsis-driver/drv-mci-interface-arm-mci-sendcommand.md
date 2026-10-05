---
id: "drv-mci-interface-arm-mci-sendcommand"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_SendCommand"
summary: "The function ARMMCISendCommand - sends commands to the memory card - retrieve the response from the card - optionally, start the data transfer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_SendCommand (uint32_t cmd, uint32_t arg, uint32_t flags, uint32_t *response)
```


The function **ARM_MCI_SendCommand** 
 - sends commands to the memory card 
 - retrieve the response from the card 
 - optionally, start the data transfer.

The parameter **cmd** is the command sent to the card. \n
The parameter **arg** contains arguments for the command **cmd.** \n
The parameter **flags** controls the behavior of the operation and takes predefined values listed in the table below. \n
The parameter **response** is a pointer to receive data.

The parameter **flags** can have the following values:

Parameter **flags**                   | Description
:-------------------------------------|:------------
ARM_MCI_RESPONSE_NONE            | No response expected (default)
ARM_MCI_RESPONSE_SHORT           | Short response (`48`-bit) expected
ARM_MCI_RESPONSE_SHORT_BUSY      | Short response with busy signal (`48`-bit) expected
ARM_MCI_RESPONSE_LONG            | Long response (`136`-bit) expected
ARM_MCI_RESPONSE_INDEX           | Check command index in response
ARM_MCI_RESPONSE_CRC             | Check CRC in response
ARM_MCI_WAIT_BUSY                | Wait until busy before sending the command
ARM_MCI_TRANSFER_DATA            | Activate Data transfer
ARM_MCI_CARD_INITIALIZE          | Execute Memory Card initialization sequence
ARM_MCI_INTERRUPT_COMMAND        | Send Interrupt command (CMD40 - MMC only)
ARM_MCI_INTERRUPT_RESPONSE       | Send Interrupt response (CMD40 - MMC only)
ARM_MCI_BOOT_OPERATION           | Execute Boot operation (MMC only)
ARM_MCI_BOOT_ALTERNATIVE         | Execute Alternative Boot operation (MMC only)
ARM_MCI_BOOT_ACK                 | Expect Boot Acknowledge (MMC only)
ARM_MCI_CCSD                     | Send Command Completion Signal Disable (CCSD) for CE-ATA device
ARM_MCI_CCS                      | Expect Command Completion Signal (CCS) for CE-ATA device

Calling the function **ARM_MCI_SendCommand** only starts the operation.
The function is non-blocking and returns as soon as the driver has started the operation.
It is not allowed to call this function again until the operation is in progress.

After the command is sent the response is retrieved if specified with **ARM_MCI_RESPONSE_xxx** flags.
When the command completes successfully (requested response is received without errors) the ARM_MCI_EVENT_COMMAND_COMPLETE event is generated.
In case that response is requested but not received the ARM_MCI_EVENT_COMMAND_TIMEOUT event is generated instead.
In case of invalid response (or CRC error) the ARM_MCI_EVENT_COMMAND_ERROR event is generated instead.
Progress of command operation can be monitored by calling the ARM_MCI_GetStatus and checking the **command_active** flag.

After the command operation the data transfer operation is started if specified with **ARM_MCI_TRANSFER_DATA** flag.
The data transfer needs to be configured before that by calling the ARM_MCI_SetupTransfer.
When the data transfer completes successfully the ARM_MCI_EVENT_TRANSFER_COMPLETE event is generated.
In case that data transfer is not completed in-time (specified by ARM_MCI_DATA_TIMEOUT) the ARM_MCI_EVENT_TRANSFER_TIMEOUT event is generated instead.
In case of CRC errors the ARM_MCI_EVENT_TRANSFER_ERROR event is generated instead.
Progress of data transfer operation can be monitored by calling the ARM_MCI_GetStatus and checking the **transfer_active** flag.

**See also:**
 - ARM_MCI_SignalEvent
******************************************************************************************************************
