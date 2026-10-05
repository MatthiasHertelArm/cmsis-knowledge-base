---
id: "drv-can-status-error-codes"
type: "concept"
domain: "drivers"
title: "CAN Status Error Codes"
summary: "The following callback notification unit events are generated:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

Status codes of the CAN driver.


The following callback notification unit events are generated:

### ARM_CAN_UNIT_STATE_INACTIVE

```c
ARM_CAN_UNIT_STATE_INACTIVE
```


### ARM_CAN_UNIT_STATE_ACTIVE

```c
ARM_CAN_UNIT_STATE_ACTIVE
```


### ARM_CAN_UNIT_STATE_PASSIVE

```c
ARM_CAN_UNIT_STATE_PASSIVE
```


### ARM_CAN_UNIT_STATE_BUS_OFF

```c
ARM_CAN_UNIT_STATE_BUS_OFF
```


### ARM_CAN_LEC_NO_ERROR

```c
ARM_CAN_LEC_NO_ERROR
```


### ARM_CAN_LEC_BIT_ERROR

```c
ARM_CAN_LEC_BIT_ERROR
```


### ARM_CAN_LEC_STUFF_ERROR

```c
ARM_CAN_LEC_STUFF_ERROR
```


### ARM_CAN_LEC_CRC_ERROR

```c
ARM_CAN_LEC_CRC_ERROR
```


### ARM_CAN_LEC_FORM_ERROR

```c
ARM_CAN_LEC_FORM_ERROR
```


### ARM_CAN_LEC_ACK_ERROR

```c
ARM_CAN_LEC_ACK_ERROR
```

******************************************************************************************************************
