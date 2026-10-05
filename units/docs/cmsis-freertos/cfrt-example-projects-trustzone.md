---
id: "cfrt-example-projects-trustzone"
type: "concept"
domain: "rtos"
title: "Example Projects: TrustZone"
summary: "The TrustZone application explains how to setup projects for booting and execution from TrustZone secure to non-secure domain and vice versa."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/example_projects.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/example_projects.md#trustzone"
license: "Apache-2.0"
mode: "V"
---

The **TrustZone** application explains how to setup projects for booting and execution from TrustZone secure to non-secure domain and vice versa.

The application shows:

- how to boot from the secure domain and switch the execution to the non-secure domain
- how to create the interface functions between secure and non-secure domain
- how to use the secure/non-secure interface functions

#### Build via command line

TrustZone example must always be built in two steps:

1. Build secure side project for Cortex-M55
   ```shell
   cbuild Examples.csolution.yml --context TZ_Secure.Debug+CM55 --update-rte
   ```

2. Build non-secure side project for Cortex-M55
   ```shell
   cbuild Examples.csolution.yml --context TZ_NonSecure.Debug+CM55 --update-rte
   ```

#### Execute via command line

To execute simulation model and run TrustZone project executable for Cortex-M55 use the following command:

```shell
  FVP_Corstone_SSE-300 -f ./Board/CM55/fvp_config.txt -a ./out/TZ_NonSecure/CM55/Debug/TZ_NonSecure.axf -a ./out/TZ_Secure/CM55/Debug/TZ_Secure.axf --simlimit 25
```

When executed, application outputs the following to the serial terminal:

(figure: TrustZone Output)
(Press Ctrl + C to stop the simulation model.)
