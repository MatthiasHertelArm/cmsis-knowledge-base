---
id: "cfrt-cmsis-freertos-examples-build-via-command-line"
type: "concept"
domain: "rtos"
title: "CMSIS-FreeRTOS Examples: Build via command line"
summary: "To build the project via command line one can use the following command syntax:"
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:CMSIS/RTOS2/FreeRTOS/Examples/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/CMSIS/RTOS2/FreeRTOS/Examples/README.md#build-via-command-line"
license: "Apache-2.0"
mode: "V"
---

> - See [CMSIS-Toolbox documentation](https://open-cmsis-pack.github.io/cmsis-toolbox/)
>   to learn more about CMSIS Solution project build and management tools.

To build the project via command line one can use the following command syntax:

`cbuild Examples.csolution.yml --context <project-name>.<build-type>+<target-type>`

To list the available context execute the following command:

```sh
cbuild list contexts Examples.csolution.yml
```

### Hello World example

- Build example project for Cortex-M3

  ```sh
  cbuild Examples.csolution.yml --context Hello.Debug+CM3
  ```

### TrustZone example (for ArmV8-M with TrustZone)

TrustZone example must always be build in two steps:

1. Build secure side project for Cortex-M55
   ```sh
   cbuild Examples.csolution.yml --context TZ_Secure.Debug+CM55
   ```
2. Build non-secure side project for Cortex-M55
   ```sh
   cbuild Examples.csolution.yml --context TZ_NonSecure.Debug+CM55
   ```
