---
id: "dbgx-arm-cmsis-debugger-review-captured-trace-data"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Using Trace / Review captured trace data"
summary: "In the debug toolbar, use the (figure: Show captured trace) button to open the generated .csv trace file in Visual Studio Code."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#review-captured-trace-data"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using Trace_

In the debug toolbar, use the (figure: Show captured trace) button to open the generated `.csv`
trace file in Visual Studio Code.

(figure: Trace Data View)

The trace viewer displays the decoded trace records in a table and supports filtering, sorting, keyboard and mouse
navigation, selecting records, and copying trace data.

Use the column controls to sort the trace. Successive selections cycle through ascending, descending, and the original
trace order.

Use filtering to locate specific records or values within the captured trace.

The meaning of **index** and **value** depends on the trace source that generated the record:

- For DWT data trace, **value** contains the **value** captured when the configured memory location was accessed.
- For exception trace, **index** identifies the exception number and **value** identifies the corresponding exception
  event.

Timestamp information is incorporated into the cycle information rather than being displayed as separate timestamp
records.

#### Locate the source of a trace record

You can correlate a captured trace record with the configuration that generated it.

Hold **Ctrl/⌘** and select a trace record in the CSV viewer. CMSIS Debugger highlights the corresponding
configuration in the **Trace Generation** view.

For example, selecting a DWT data trace record identifies the DWT data trace point that generated the record.
