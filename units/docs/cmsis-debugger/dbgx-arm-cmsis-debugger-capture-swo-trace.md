---
id: "dbgx-arm-cmsis-debugger-capture-swo-trace"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Using Trace / Capture SWO trace"
summary: "After configuring and saving the trace settings:"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#capture-swo-trace"
license: "Apache-2.0"
mode: "V"
---

_Part of: Using Trace_

After configuring and saving the trace settings:

- Build the application if not done already.
- Start a debug session.
- Run the application.
- Stop execution after the period that you want to analyze.

With [`mode: file`](#configure-swo-trace-in-the-cmsis-solution), the SWO trace stream is captured and the decoded trace
is automatically made available as a CSV file.

> ⚠ **Important:**
>
> Newly captured SWO trace is appended during a debug session until trace source settings change. Copy or rename a CSV
> file before you start the next capture if you need to preserve previous trace.
