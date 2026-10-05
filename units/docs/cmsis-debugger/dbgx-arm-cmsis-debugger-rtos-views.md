---
id: "dbgx-arm-cmsis-debugger-rtos-views"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / RTOS Views"
summary: "For RTOS awareness, the RTOS Views extension needs to be added to VS Code. This extension supports a wide range of real-time operating systems, such as FreeRTOS, Zephyr, embOS,and Keil RTX5."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#rtos-views"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

For RTOS awareness, the [RTOS Views](https://marketplace.visualstudio.com/items?itemName=mcu-debug.rtos-views)
extension needs to be added to VS Code. This extension supports a wide range of real-time operating systems, such as
FreeRTOS, Zephyr, embOS,and Keil RTX5.

(figure: RTOS Views with FreeRTOS)

> 📝 **Note:**
>
> - This is not a live view. It only gets updated when the program execution is stopped.
> - To enable the view, you need to go to the debug view and press Ctrl/Cmd - Shift - P. Select
>   **RTOS Views: Toggle RTOS Panel**. Afterwards, start your debug session.
> - The view is located in the Terminal panel at the bottom and is called **XRTOS**.
> - If it does not show values after entering a debug session and running the application, press Ctrl/Cmd - Shift - P
>   again and select **RTOS Views: Refresh**.
