---
id: "cfrt-example-projects-hello-world"
type: "concept"
domain: "rtos"
title: "Example Projects: Hello World"
summary: "The Hello World application can be used as a starting point when developing a new application. Using it, one can verify initial system setup and configuration."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/example_projects.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/example_projects.md#hello-world"
license: "Apache-2.0"
mode: "V"
---

The **Hello World** application can be used as a starting point when developing a new application. Using it, one can verify initial system setup and configuration.

The application is simple and shows how to use CMSIS-RTOS2:

- how to initialize and start the RTOS kernel
- how to create a new thread
- how to retarget stdout

#### Build via command line

The following cbuild command may be used to build Hello World example project for Cortex-M3:

```shell
  cbuild Examples.csolution.yml --context Hello.Debug+CM3 --update-rte
```

#### Execute via command line

To execute simulation model and run Hello World project executable for Cortex-M3 use the following command:

```shell
  FVP_MPS2_Cortex-M3 -f ./Board/CM3/fvp_config.txt ./out/Hello/CM3/Debug/Hello.axf --simlimit 25
```

When executed, application outputs the following to the serial terminal:

(figure: Hello Output)
(Press Ctrl + C to stop the simulation model.)
