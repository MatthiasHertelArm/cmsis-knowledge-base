---
id: "core-device-header-file-device-h"
type: "concept"
domain: "core"
title: "Device Header File `<Device.h>`"
summary: "The Device Header File contains the following functionalities that are device-specific: - interrupt_number_sec provides interrupt numbers (IRQn) for all exceptions and interrupts of the device. - core_config_sect reflect the features of the device."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_device_h.md"
license: "Apache-2.0"
mode: "V"
---

The Device Header File contains the following functionalities that are device-specific:
 - interrupt_number_sec provides interrupt numbers (IRQn) for all exceptions and interrupts of the device.
 - core_config_sect reflect the features of the device.
 - device_access provides definitions for the peripheral_gr to all device peripherals. It contains all data structures and the address mapping for device-specific peripherals.
 - **Access Functions for Peripherals (optional)** provide additional helper functions for peripherals that are useful for programming of these peripherals. Access Functions may be provided as inline functions or can be extern references to a device-specific library provided by the silicon vendor.

[API Reference](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/modules.html) describes the standard features and functions of the device_h_pg in details.
