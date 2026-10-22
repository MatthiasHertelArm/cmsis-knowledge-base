---
id: "view-component-viewer-overview"
type: "concept"
domain: "trace"
title: "Component Viewer: Overview"
summary: "The \\cviewer reads specific memory locations from the target hardware using a standard debug unit that is connected via JTAG or SWD to the CoreSight Debug Access Port (DAP)."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/cmp_viewer.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/cmp_viewer.md#overview"
license: "Apache-2.0"
mode: "V"
---

The \cviewer reads specific memory locations from the target hardware using a standard debug unit that is connected via JTAG or SWD to the CoreSight Debug Access Port (DAP). The address of these memory locations is typically defined by symbols that represent variables, arrays, or starting point of linked lists. The *.SCVD file specifies these symbols and customizes the formatting in the \cviewer window of the debugger.

(figure: Component Viewer displays status variables)

cv_use provides instructions on how to enable Component Viewer in a project.

**Benefits of the Component Viewer:**

 - Visibility to the static user relevant information of an software component or application program with no additional software overhead in the target application.
 - The information is obtained via debug symbols from target memory using simple read commands via JTAG or SWD connectivity to a debug adapter.
 - Debug adapters that support hot plugging allow to show the current status of the application software in case of failures.
