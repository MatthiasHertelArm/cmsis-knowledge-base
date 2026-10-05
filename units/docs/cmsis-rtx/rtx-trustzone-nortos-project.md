---
id: "rtx-trustzone-nortos-project"
type: "concept"
domain: "rtos"
title: "TrustZone NoRTOS Project"
summary: "This ARM Cortex-M33 secure/non-secure example project that shows the setup for TrustZone for ARMv8-M applications. The application uses CMSIS and can be executed on a Fixed Virtual Platform (FVP) simulation model."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/TrustZoneV8M/NoRTOS/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/TrustZoneV8M/NoRTOS/README.md"
license: "Apache-2.0"
mode: "V"
---

This ARM Cortex-M33 secure/non-secure example project that shows the setup
for TrustZone for ARMv8-M applications. The application uses CMSIS and can
be executed on a Fixed Virtual Platform (FVP) simulation model.

The application demonstrates function calls between secure and non-secure state.

Secure application:

- Setup code and start non-secure application.

Non-secure application:

- Calls a secure function from non-secure state.
- Calls a secure function that call back to a non-secure function.

Output: Variables used in this application can be viewed in the Debugger Watch window.
