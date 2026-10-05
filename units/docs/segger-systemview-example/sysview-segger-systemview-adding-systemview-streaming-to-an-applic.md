---
id: "sysview-segger-systemview-adding-systemview-streaming-to-an-applic"
type: "concept"
domain: "trace"
title: "SEGGER-SystemView: Adding SystemView Streaming to an Application"
summary: "3. Solution and Project Configuration - In the csolution.yml file, add the following rtt: node under the debugger: node:"
status: "draft"
collection: "segger-systemview-example"
source: "Arm-Examples/SEGGER-SystemView@9be0601:README.md"
doc_source: "https://github.com/Arm-Examples/SEGGER-SystemView/blob/9be0601/README.md#adding-systemview-streaming-to-an-application"
license: "Apache-2.0"
mode: "V"
---

1. In the [Software Components view](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution#software-components-view), enable the following:
  - `Segger -> RTT`
  - `Segger -> SystemView`, `FreeRTOS` variant
2. Add the following code to your application:
  - At the end of `FreeRTOSConfig.h` add:
    ```
    #include "SEGGER_SYSVIEW_FreeRTOS.h"
    ```
  - Include the required header files:
    ```
    #include "FreeRTOSConfig.h"
    ```
  - Start streaming before the RTOS initialization:
    ```
    traceSTART();
    ```
  - Send messages to the SystemView application:
    ```
    SEGGER_SYSVIEW_PrintfHost("Button pressed %d times", count);
    ```
3. Solution and Project Configuration
  - In the `csolution.yml` file, add the following [`rtt:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#rtt) node under the [`debugger:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#debugger) node:
    ```
           rtt:
             - channel:
                 - number: 1
                   mode: systemview
    ```

#### Optional configurations
1. Instead of streaming to a file, it is also possible to stream directly to the SystemView application via a network connection.  To test this mode, change **Target Set** from **systemview-file** to **systemview-server** in the  [Manage Solution view](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution#manage-solution-view) dialog.
