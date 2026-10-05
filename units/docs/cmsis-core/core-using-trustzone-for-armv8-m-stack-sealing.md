---
id: "core-using-trustzone-for-armv8-m-stack-sealing"
type: "concept"
domain: "core"
title: "Using TrustZone for Armv8-M: Stack Sealing"
summary: "CMSIS-Core stacksealing_support_trustzone_functions provide standard interface for implementing the Secure Stack Sealing technique recommended for mitigating some security vulnerabilities on Armv8-M systems with TrustZone."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/using_tz.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/using_tz.md#stack-sealing"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Core stacksealing_support_trustzone_functions provide standard interface for implementing the [Secure Stack Sealing technique](https://developer.arm.com/Arm%20Security%20Center/Armv8-M%20Stack%20Sealing%20Vulnerability) recommended for mitigating some security vulnerabilities on Armv8-M systems with TrustZone.

startup_c_sec demonstrates how this functionality can be used in a device startup file.

Stack Sealing also requires an application project to have a linker script that explicitly reserves 8 bytes for the stack seal on top of the secure main stack. Linker files provided with device_examples for Armv8-M cores demonstrate how this can be implemented. For example see .\\Device\\ARM\\ARMCM33\\Source\\ARM\\ARMCM33_ac6.sct.

To learn more about the stack sealing implementation in CMSIS projects for Armv8-M devices, refer to **Application Note 335**.
