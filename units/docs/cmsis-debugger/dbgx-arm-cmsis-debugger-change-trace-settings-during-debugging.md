---
id: "dbgx-arm-cmsis-debugger-change-trace-settings-during-debugging"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Using Trace / Change trace settings during debugging"
summary: "You can modify trace source settings while a debug session is active."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#change-trace-settings-during-debugging"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using Trace_

You can modify trace source settings while a debug session is active.

Changes that have not yet been saved are indicated in the **Trace Generation** view. The view also indicates unsaved changes when the affected configuration section is collapsed.

Press (figure: Save button) to store the updated configuration.

The new configuration is used once execution is resumed.

#### Handle trace overflow

An **overflow** record indicates that trace information was lost because the generated trace exceeded the available
trace bandwidth.

When overflow occurs, consider reducing the amount of enabled trace information or adjusting the trace configuration to
reduce bandwidth consumption. For example, changing timestamp or ITM-related settings can reduce the amount of
generated trace data.

> 📝 **Note:**
>
> A capture file containing overflow records indicates gaps in the trace. Take this into account when analyzing the captured
> data.

#### Consider hardware resource limitations

Cortex-M trace functionality uses hardware resources that vary between processors. The number and capabilities of DWT
comparators, trace sources, and supported trace combinations therefore depend on the selected target.

In particular, DWT data trace shares comparator resources with data access breakpoints. Advanced data trace
configurations, such as value-dependent trace points, can consume additional hardware resources.

CMSIS Debugger validates the configuration and reports combinations that are not supported by the selected processor.

When configuring several trace sources, enable only the information required for the current investigation. This
preserves both target trace resources and available SWO bandwidth.

> 📝 **Note:**
>
> Trace-related DWT configuration is performed before GDB configures data access breakpoints. As a result, DWT
> resources allocated for trace may prevent GDB from setting previously functional data access breakpoints.
>
> Note that GDB installs data access breakpoints immediately before execution resumes and removes them when execution
> stops.
