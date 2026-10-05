---
id: "drv-sai-configuration"
type: "concept"
domain: "drivers"
title: "SAI Configuration"
summary: "Specify Transmitter/Receiver configuration."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

Specify Transmitter/Receiver configuration.

Configuration is specified by ORing **ARM_SAI_CONFIGURE__x_** with the following parameters:
 - sai_mode_control
 - sai_sync_control
 - sai_protocol_control
 - sai_data_bits_control
 - sai_bit_order_control
 - sai_mono_control
 - sai_clock_pol_control
 - sai_companding_control
 - sai_mclk_pin_control

Additional configuration specified by **arg1:**
 - sai_frame_control
 - sai_slot_control

Additional configuration specified by **arg2:**
 - **Audio Frequency** (Master only)
 - sai_mclk_pres_control

 Defines Transmitter/Receiver mode.
