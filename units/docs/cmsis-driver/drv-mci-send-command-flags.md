---
id: "drv-mci-send-command-flags"
type: "concept"
domain: "drivers"
title: "MCI Send Command Flags"
summary: "Specify various options for sending commands to the card and the expected response."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Specify various options for sending commands to the card and the expected response.

**ARM_MCI_xxx** flags are sent with the function ARM_MCI_SendCommand as the parameter **flag.** 
It controls the behavior of the command sent to the card and provides information about the expected response from the card.

The following codes are defined:

### ARM_MCI_RESPONSE_NONE

```c
ARM_MCI_RESPONSE_NONE
```


### ARM_MCI_RESPONSE_SHORT

```c
ARM_MCI_RESPONSE_SHORT
```


### ARM_MCI_RESPONSE_SHORT_BUSY

```c
ARM_MCI_RESPONSE_SHORT_BUSY
```


### ARM_MCI_RESPONSE_LONG

```c
ARM_MCI_RESPONSE_LONG
```


### ARM_MCI_RESPONSE_INDEX

```c
ARM_MCI_RESPONSE_INDEX
```


### ARM_MCI_RESPONSE_CRC

```c
ARM_MCI_RESPONSE_CRC
```


### ARM_MCI_WAIT_BUSY

```c
ARM_MCI_WAIT_BUSY
```


### ARM_MCI_TRANSFER_DATA

```c
ARM_MCI_TRANSFER_DATA
```


### ARM_MCI_CARD_INITIALIZE

```c
ARM_MCI_CARD_INITIALIZE
```


### ARM_MCI_INTERRUPT_COMMAND

```c
ARM_MCI_INTERRUPT_COMMAND
```


### ARM_MCI_INTERRUPT_RESPONSE

```c
ARM_MCI_INTERRUPT_RESPONSE
```


### ARM_MCI_BOOT_OPERATION

```c
ARM_MCI_BOOT_OPERATION
```


### ARM_MCI_BOOT_ALTERNATIVE

```c
ARM_MCI_BOOT_ALTERNATIVE
```


### ARM_MCI_BOOT_ACK

```c
ARM_MCI_BOOT_ACK
```


### ARM_MCI_CCSD

```c
ARM_MCI_CCSD
```


### ARM_MCI_CCS

```c
ARM_MCI_CCS
```

******************************************************************************************************************
