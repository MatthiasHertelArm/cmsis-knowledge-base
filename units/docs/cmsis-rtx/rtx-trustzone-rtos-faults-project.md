---
id: "rtx-trustzone-rtos-faults-project"
type: "concept"
domain: "rtos"
title: "TrustZone RTOS_Faults Project"
summary: "This ARM Cortex-M33 Security Test example project shows how the ARMv8-M architecture reacts to potential security attacks. It uses CMSIS-Core and CMSIS-RTOS2 (Keil RTX5)."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/TrustZoneV8M/RTOS_Faults/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/TrustZoneV8M/RTOS_Faults/README.md"
license: "Apache-2.0"
mode: "V"
---

This ARM Cortex-M33 Security Test example project shows how the ARMv8-M architecture reacts
to potential security attacks. It uses CMSIS-Core and CMSIS-RTOS2 (Keil RTX5).

To execute a test case, change the variable TestCase:

> TestCase = n

where `n` is a test case number (0..4).

After a test case has been executed, the security attack gets recorded in the IncidentLog
and the application is reset. The struct IncidentLogCopy can be viewed in a watch window
and shows the past four recorded incidents.
