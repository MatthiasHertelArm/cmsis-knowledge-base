---
id: "dbgx-arm-cmsis-debugger-cpu-time"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / CPU Time"
summary: "Most Arm Cortex-M processors (except Cortex-M0/M0+/M23) include a DWT->CYCCNT register that counts CPU states."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#cpu-time"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

Most Arm Cortex-M processors (except Cortex-M0/M0+/M23) include a `DWT->CYCCNT` register that counts CPU states. In combination with the CMSIS variable [`SystemCoreClock`](https://arm-software.github.io/CMSIS_6/latest/Core/group__system__init__gr.html) the CMSIS Debugger calculates execution time and displays it along with the selected processor core in the CPU Time Status bar.  A click on the CPU Time Status bar opens the related [VS Code command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

|Command        | Description  |
|:--------------|:-------------|
|CPU Time       | Print CPU execution time and history of past program stops. |
|Reset CPU Time | Reset CPU execution time and history. Set new reference time (zero point). |

(figure: CPU Time)

> 📝 **Notes:**
>
> - The first program stop (typically at function `main`) is the initial reference time (zero point).
> - `DWT->CYCCNT` is a 32-bit register incremented with [`SystemCoreClock`](https://arm-software.github.io/CMSIS_6/latest/Core/group__system__init__gr.html) frequency. The time calculation copes with one overflow between program stops. Multiple overflows between program stops deliver wrong time information.
> - Each processor in a multi-processor system has and independent `DWT->CYCCNT` register.
