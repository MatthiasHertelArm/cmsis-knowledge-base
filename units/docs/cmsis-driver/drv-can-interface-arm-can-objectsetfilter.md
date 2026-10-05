---
id: "drv-can-interface-arm-can-objectsetfilter"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_ObjectSetFilter"
summary: "The function ARM_CAN_ObjectSetFilter sets or removes the filter for message reception. Refer to can_filtering for details on filtering."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_ObjectSetFilter (uint32_t obj_idx, ARM_CAN_FILTER_OPERATION operation, uint32_t id, uint32_t arg)
```


The function **ARM_CAN_ObjectSetFilter** sets or removes the filter for message reception. Refer to can_filtering for details on filtering. 

The parameter **obj_idx** is the message object index. \n
The parameter **operation** is the operation on the filter as listed in the table below and 
which are defined in the structure ARM_CAN_FILTER_OPERATION.

Parameter **operation**                 |  Operation on Filter          | supported when ARM_CAN_OBJ_CAPABILITIES data field
:---------------------------------------|:------------------------------|:------------------------------------------
ARM_CAN_FILTER_ID_EXACT_ADD        | Add    exact ID filter        | **exact_filtering** = `1`
ARM_CAN_FILTER_ID_EXACT_REMOVE     | Remove exact ID filter        | **exact_filtering** = `1`
ARM_CAN_FILTER_ID_RANGE_ADD        | Add    range ID filter        | **range_filtering** = `1`
ARM_CAN_FILTER_ID_RANGE_REMOVE     | Remove range ID filter        | **range_filtering** = `1`
ARM_CAN_FILTER_ID_MASKABLE_ADD     | Add    maskable ID filter     | **mask_filtering** = `1`
ARM_CAN_FILTER_ID_MASKABLE_REMOVE  | Remove maskable ID filter     | **mask_filtering** = `1`

The parameter **id** is the identifier of the filter or defines the start of the filter range (depends on the filter operation). \n
The parameter **arg** is the mask of the filter or defines the end of the filter range (depends on the filter operation).

\sa ARM_CAN_ObjectConfigure 
*************************************************************************************************************************
