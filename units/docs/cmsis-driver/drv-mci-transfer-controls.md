---
id: "drv-mci-transfer-controls"
type: "concept"
domain: "drivers"
title: "MCI Transfer Controls"
summary: "Data transfer codes specifies the transfer direction and type and are used with the function ARM_MCI_SetupTransfer as the parameter mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Specify data transfer mode.

Data transfer codes specifies the transfer direction and type and are used with the function ARM_MCI_SetupTransfer as the parameter **mode.**

The following codes are defined:

### ARM_MCI_TRANSFER_READ

```c
ARM_MCI_TRANSFER_READ
```


### ARM_MCI_TRANSFER_WRITE

```c
ARM_MCI_TRANSFER_WRITE
```


### ARM_MCI_TRANSFER_BLOCK

```c
ARM_MCI_TRANSFER_BLOCK
```


### ARM_MCI_TRANSFER_STREAM

```c
ARM_MCI_TRANSFER_STREAM
```

******************************************************************************************************************
