---
id: "drv-can-control-codes"
type: "concept"
domain: "drivers"
title: "CAN Control Codes"
summary: "CAN Control Codes"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

Codes to configure the CAN driver.

The various CAN control codes define:

  - can_identifer_ctrls          specify CAN identifier. Refer to ARM_CAN_ObjectConfigure.
  - can_mode_ctrls               control CAN interface operation. Refer to ARM_CAN_Control.
  - can_timeseg_ctrls            specify CAN bit rate and timing. Refer to ARM_CAN_SetBitrate.
  - can_bus_mode_ctrls           specify CAN bus operating mode. Refer to ARM_CAN_SetMode.
  - can_filter_operation_ctrls   specify CAN filter operations.  Refer to ARM_CAN_ObjectSetFilter.
  - can_obj_config_ctrls         specify CAN object configuration modes. Refer to ARM_CAN_ObjectConfigure.
****************************************************************************************************************
