---
id: "dbgx-arm-cmsis-debugger-trace-and-live-view"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / Trace and Live view"
summary: "The Trace and Live View (figure: Trace and Live view) (available from the VS Code Activity Bar) currently contains the LIVE WATCH, the COMPONENT VIEWER, and the CORE PERIPHERALS views."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#trace-and-live-view"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

The **Trace and Live View**
(figure: Trace and Live view)
(available from the VS Code Activity Bar) currently contains the [**LIVE WATCH**](#live-watch), the
[**COMPONENT VIEWER**](#component-viewer), and the [**CORE PERIPHERALS**](#core-peripherals) views.

The CMSIS Debugger stores dynamic view state per debug configuration in the `vscode-cmsis-debugger.viewState` VS Code workspace setting. The stored state includes view-specific configurations, e.g. the last filter text and periodic update options for the [**COMPONENT VIEWER**](#component-viewer), and the `enabled`/`disabled` state of the [CPU Time](#cpu-time) display.

When you start the same debug configuration again, its previous state is restored automatically. To clear the stored state, run the **CMSIS Debugger: Reset All Dynamic View States** command from the Command Palette.

#### LIVE WATCH

You can add expressions to this view that are updated while the application is running on your target by:

1. Pressing the `+` sign and entering an expression.
2. Using the context menu item **Add to Live Watch** in the editor or the the **Run and Debug** view.

(figure: Displaying a variable in the LIVE WATCH)

> 📝 **Notes:**
>
> Live Watch may stop updating when the processor enters a low-power state, for example after executing `WFI`, because
> some devices make SRAM inaccessible to the debugger while sleeping. If continuous updates are required, configure the
> application to avoid sleep states while debugging. This is particularly relevant for RTOS applications such as
> Zephyr, which typically execute `WFI` from the idle thread.

#### COMPONENT VIEWER

This view shows detailed information to help analyze the operation of software components. The required
infrastructure can be easily added to user applications.

Refer to the [Component Viewer documentation](https://arm-software.github.io/CMSIS-View/latest/cmp_viewer.html) for
detailed advice on how to show information from user software using an SCVD file.

The Component Viewer shows information about:

- Information from software components that is provided in memory for example by static variables or structures.
- Objects that are addressed by handles or dynamic arrays.

(figure: Showing software component properties in the COMPONENT VIEWER)

The **Component Viewer toolbar** offers the following action buttons:

(figure: Component Viewer Buttons)

| Button | Description |
| -------- | ------------- |
| Filter | Filter the displayed components and their entries |
| Clear Filter | Remove component filtering |
| Disable Periodic Update | Components are not updated while the target is running |
| Expand All | Show all components at once |
| Collapse All | Only show  top-level component name |

The **Disable Periodic Update** button stops updates for all components. If you wish to lock a single component, use
the component's (figure: Lock Component Display) button to disable periodic updates.

#### CORE PERIPHERALS

The **CORE PERIPHERALS** view gives insight into the programming of CPU specific core peripherals.

The Core Peripherals view shows information about the following components if implemented by the CPU:

- Memory Protection Unit
- Nested Vectored Interrupt Controller
- System Config and Control
- System Tick Timer
- Fault Reports

(figure: Showing core peripheral contents in the COMPONENT PERIPHERALS view)

#### Trace Generation

CMSIS Debugger supports capturing [trace](#using-trace) information from Cortex-M processors using Serial Wire Output
(SWO). You can configure which trace information the processor generates, capture the resulting trace without stopping
program execution, and inspect the decoded trace data directly in Visual Studio Code.

(figure: Trace Generation)

In the debug toolbar, use the
(figure: Show captured trace)
button to open the generated `.csv` trace file in the [**Trace Data** view](#review-captured-trace-data).

For further details on how to configure and inspect trace, refer to [Using trace](#using-trace).
