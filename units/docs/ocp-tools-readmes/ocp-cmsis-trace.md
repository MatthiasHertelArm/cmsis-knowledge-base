---
id: "ocp-cmsis-trace"
type: "concept"
domain: "trace"
title: "CMSIS Trace"
summary: "VS Code extension for capturing CMSIS SWO/ITM trace from pyOCD using the cmsis-trace-decoder command line tool."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/cmsis-trace-extension@1aebf86:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-trace-extension/blob/1aebf86/README.md"
license: "Apache-2.0"
mode: "V"
---

VS Code extension for capturing CMSIS SWO/ITM trace from pyOCD using the
[`cmsis-trace-decoder`](https://github.com/Open-CMSIS-Pack/cmsis-trace-extension/blob/1aebf86/../cmsis-trace-decoder) command line tool.

The activity bar contains a **CMSIS Trace** sidebar. The Capture view shows a
single button:

- **Capture trace (write RAW Trace + Meta)** — starts `cmsis-trace-decoder` with
  the configured raw trace path, defaulting to
  `.trace/<active CMSIS target-set>/SWO.raw`. If no active CMSIS target-set is
  available, the fallback folder is `.trace/default`. The decoder connects to
  the pyOCD raw SWO TCP server, retries quietly until pyOCD is available, writes
  the raw SWO bytes and trace metadata (`SWO.tracemeta.yml`) next to it, and
  opens the decoded event TCP listener used by CMSIS System Analyzer live views.
  While capturing, the button turns into **Stop capture**; stopping sends `q` to
  the decoder so it flushes the raw file and writes the trace metadata.

pyOCD must already be running and exposing its raw SWO TCP port. The extension
only starts and stops the decoder; it never writes trace files itself.

Status and error logs from the decoder are shown in the **CMSIS Trace** output
channel (Output panel dropdown).

During CMSIS debug sessions the extension starts capture automatically on debug
start. The running decoder writes each incoming TCP chunk directly to `SWO.raw`.
When the debug adapter reports **Pause**, the extension starts a second one-shot
decoder process to convert the current raw file to CTF/XML, and loads the
default artefacts into the TSP server. The live decoder keeps running and
remains connected to pyOCD, so debug continue does not need to restart capture.
Debug termination stops the live decoder and runs the same final convert/load
workflow.

The **Convert Trace (CTF / TC XML)** command converts the last/default raw file
to CTF and Trace Compass XML. CTF is written to the active trace folder's `ctf`
subdirectory; the XML is written next to the raw file. **Convert Trace (CSV)**
writes a compact CSV as `<raw-base>.csv`; **Convert Trace (CSV Filtered)** asks
for packet filters and writes compact CSV via repeated decoder flags such as
`--filter DWT0 --filter ITM0`; **Convert Trace (CSV Full)** writes the full
decoder dump as `<raw-base>.full.csv`. The Trace Server commands can start or
reuse a running TSP server, clear its current experiments/traces/XML
configurations, and reload `SWO.traceanalysis.xml` plus `ctf` from the active
trace folder when present.
