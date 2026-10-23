---
id: "drv-mci-control-codes"
type: "concept"
domain: "drivers"
title: "MCI Control Codes"
summary: "Configure and control the MCI using the ARM_MCI_Control."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Configure and control the MCI using the ARM_MCI_Control.

Many parameters of the MCI driver are configured using the ARM_MCI_Control function.

The various MCI control codes define:
  - mci_mode_ctrls configures and controls the MCI interface
  - mci_bus_speed_ctrls specifies the bus speed mode
  - mci_bus_data_width_ctrls specifies the data bus width
  - mci_cmd_line_ctrls specifies the CMD line mode
  - mci_driver_strength_ctrls specifies the driver strength

Refer to the function ARM_MCI_Control for further details.
******************************************************************************************************************
