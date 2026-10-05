---
id: "core-cmsis-core-device-files-device-template-files"
type: "concept"
domain: "core"
title: "CMSIS-Core Device Files: Device Template Files"
summary: "CMSIS-Core includes the template files that simplify the creation of CMSIS-Core Device Files for a specific device variant."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_device_files.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_device_files.md#device-template-files"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core includes the template files that simplify the creation of CMSIS-Core Device Files for a specific device variant.

Silicon vendors typically need to add to these template files the following information:
 - **Device Peripheral Access Layer** that provides definitions for device-specific peripherals.
 - **Access Functions for Peripherals** (optional) that provides additional helper functions to access device-specific peripherals.
 - **Interrupt vectors** in the startup file that are device specific.

Template File                       | Description
:-----------------------------------|:----------------------------------------
📂 CMSIS/Core/Template/Device_M     | Folder with CMSIS-Core device file templates ([See on GitHub](https://github.com/ARM-software/CMSIS_6/tree/main/CMSIS/Core/Template/Device_M/))
 ┣ 📂 Config                        | Template configuration files
 &emsp;  ┣ 📄 Device_ac6.sct   | linker_sct_pg template
 &emsp;  ┣ 📄 Device_gcc.ld    | Linker description file for GNU GCC Arm Embedded Compiler
 &emsp;  ┗ 📄 partition_Device.h |partition_h_pg template
 ┣ 📂 Include                       | Template header files
 &emsp;  ┣ 📄 Device.h         | device_h_pg template
 &emsp;  ┗ 📄 system_Device.h  | system_Device_sec
 ┗ 📂 Source                        | Template C files
 &emsp;  ┣ 📄 startup_Device.c | startup_c_pg template
 &emsp;  ┗ 📄 system_Device.c  | system_Device_sec

**Adapt Template Files to a Device**

Each template file contains comments that start with **ToDo:** and describe required modifications.

The templates contain several placeholders that need to be replaced when creating CMSIS-Core device files:

Placeholder                | To be replaced with
:--------------------------|:----------------------------------------
`<Device>`                 | The specific device name or device family name, for example `LPC17xx`
`<DeviceInterrupt>`        | The specific interrupt name of the device, for example `TIM1` for Timer 1 interrupt
`<DeviceAbbreviation>`     | Short name or abbreviation of the device family, for example `LPC`
`Cortex-M#`                | The specific Cortex-M processor name, for example `Cortex-M3`

Device files for the device_examples can be also a good reference point for implementing CMSIS-Core support for specific devices.
