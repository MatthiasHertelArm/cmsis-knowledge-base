---
id: "dv-resource-requirements-cmsis-rtos2"
type: "concept"
domain: "drivers"
title: "Resource Requirements: CMSIS-RTOS2"
summary: "The thread requirements need to be reflected in the CMSIS-RTOS2 configuration. Refer to the CMSIS-RTOS2 documentation for further details."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DriverValidation.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/resource_requirements.html"
license: "Apache-2.0"
mode: "V"
---

The thread requirements need to be reflected in the CMSIS-RTOS2 configuration.
Refer to the [**CMSIS-RTOS2 documentation**](https://arm-software.github.io/CMSIS-RTX/latest/index.html) for further details.

For **CMSIS-RTOS2 RTX5**, thread requirements are configured in the
[**RTX_Config.h**](https://arm-software.github.io/CMSIS-RTX/latest/config_rtx5.html) file :

| Option                                                            | Value                              |
| :---------------------------------------------------------------- | :--------------------------------: |
| System Configuration: Global Dynamic Memory size [bytes] (Note 1) | 16384                              |
| Thread Configuration: Default Thread Stack size [bytes]           | 3072                               |

**Note:** Note 1: This setting is only necessary for WiFi driver testing, for other driver testing value of 4096 bytes is sufficient.
