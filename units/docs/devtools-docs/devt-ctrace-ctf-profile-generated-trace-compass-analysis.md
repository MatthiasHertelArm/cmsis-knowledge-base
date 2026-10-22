---
id: "devt-ctrace-ctf-profile-generated-trace-compass-analysis"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Generated Trace Compass analysis"
summary: "Trace Compass provides its standard CTF event table for every encoded event; ctrace does not duplicate these point events as generated XML tables. The companion XML contains only graphical views backed by data actually emitted:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md#generated-trace-compass-analysis"
license: "Apache-2.0"
mode: "V"
---

Trace Compass provides its standard CTF event table for every encoded event; ctrace does not duplicate these point
events as generated XML tables. The companion XML contains only graphical views backed by data actually emitted:

- XY views for DWT values and data-address fragments.
- Time graphs for DWT matches, DWT and PMU counter pulses, decoded exception activity, and processor sleep.

ITM values, trace-status records, Global Timestamps, ordinary PC samples, and trace-prohibited markers stay in the
standard event table because they do not establish a duration. Each contributing route receives a separate graphical
view. Its visible suffix is the input channel followed by the resolved processor name, if available; numeric Trace Bus
IDs are omitted from visible labels but remain in the
public CTF event context and internally in provider IDs and state queries. Routes and topics without corresponding
emitted data do not add graphical views. When no graphical topic remains, ctrace omits the XML entirely and removes
any stale target file; importing only the CTF bundle still provides the event table.

The production output planner conservatively assigns each formatted route a distinct clock domain and UUID, even
when configured frequencies match. After lazy stream projection, a completed bundle contributes XML views only if
it retains at least one stream and exactly one referenced domain; with current planning, this normally means one
retained formatted route. Multiple retained domains exclude that bundle and produce one warning, since the supported
reader cannot establish a combined event order within it. Separate single-clock CTF bundles can contribute to the
same target XML without correlating clocks or rebasing timestamps.

Every state path begins with `hostId` (the reader's sole clock UUID for that bundle), then
`context.cmsis_trace_bus_id`, then the topic. View entries select the concrete `<clock-uuid>/<trace-bus-id>/<topic>`
path. This includes legacy ID `0` and separates captures that reuse formatted ID `1` or the same processor label.
View queries accept only that concrete UUID, either bare or quoted, because supported readers can expose the TSDL
quotes as part of `hostId`; they do not wildcard the capture identity.
Separate bundles must not reuse a clock UUID: if future inputs establish shared clocks across captures, this
capture-identity contract must be revised explicitly.
Only metadata from successfully finalized bundles in the current run contributes: a preserved old bundle after an
input preflight failure is not eligible. Completed output after recoverable decoding errors remains eligible.

The state-provider version is a deterministic hash of the generated XML contents. A semantic XML change therefore
changes the version automatically and prevents a Trace Compass server from reusing stale analysis state.

Analysis and view identifiers share a deterministic namespace derived from the contributing clock identities.
Random clock UUIDs distinguish independent captures; the namespace prevents XML definitions for different targets
from colliding in one viewer. Display labels are not used as identity. Preparing or writing the target XML cannot
delete completed CSV/CTF output, and it never removes historical per-channel XML files.
