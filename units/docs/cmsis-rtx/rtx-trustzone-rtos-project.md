---
id: "rtx-trustzone-rtos-project"
type: "concept"
domain: "rtos"
title: "TrustZone RTOS Project"
summary: "This ARM Cortex-M33 secure/non-secure example project that shows the setup of the CMSIS-RTOS2 RTX for TrustZone for ARMv8-M applications."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Examples/TrustZoneV8M/RTOS/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Examples/TrustZoneV8M/RTOS/README.md"
license: "Apache-2.0"
mode: "V"
---

This ARM Cortex-M33 secure/non-secure example project that shows the setup
of the CMSIS-RTOS2 RTX for TrustZone for ARMv8-M applications.

The application uses CMSIS and can be executed on a Fixed Virtual Platform (FVP)
simulation model. The application demonstrates three RTOS threads.

Secure application:

- Setup code and start non-secure application.

Non-secure application:

- Calls a secure function from non-secure state.
- Calls a secure function that call back to a non-secure function.

Output: Variables used in this application can be viewed in the Debugger Watch window.
