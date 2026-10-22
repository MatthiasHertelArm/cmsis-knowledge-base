---
id: "devt-ctrace-multi-source-design-decisions-revised-after-the-migration"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Decisions revised after the migration"
summary: "The following changes supersede assumptions in the original plan:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/multi-source-design.md#decisions-revised-after-the-migration"
license: "Apache-2.0"
mode: "V"
---

The following changes supersede assumptions in the original plan:

- Discovery initially expanded eligibility to SWO, TB, and named-TB while retaining the one-input limit. It now
  processes all matching supported inputs independently and sequentially. Each input is normalized separately:
  absent or null format defaults by channel, with SWO unformatted and TB formatted; an explicit override applies
  to every input in the trace-run. Originally, omission selected only the legacy SWO path.
- Input failures contribute to command failure while remaining inputs and solution sets continue. Each file has
  independent decoder state and outputs, with only one OpenCSD tree live at a time. `--target` still selects a
  solution set, including all its supported inputs.
- CTF bundles now always use `<solution-set>.<channel>.ctf`, also for single-input runs. CSV retains its
  channel-qualified path. Existing `<solution-set>.ctf` bundles are not migrated or removed; the published CTF path
  still needs alignment as recorded in the [CTF profile](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md#files-and-common-structure).
- Formatter skips and initial unsynchronized ITM bytes now produce non-failing byte-count Info annotations. They
  carry no invented route or time; a route receiving payload without a committed hardware sync reports an Error.
- A fatal decoder abort retains committed CSV rows with an unfiltered input-wide abort record. Incomplete CTF
  is still removed and excluded from XML. This replaces the original all-output cleanup policy for a healthy CSV writer.
- Trace Compass XML now creates graphical views only for topics observed in completed output, refining the original
  eager legacy XML compatibility rule.
- One `<solution-set>.traceanalysis.xml` now collects eligible, freshly completed CTF bundles for the target. Its
  lifecycle is independent of CSV/CTF, and old per-channel XML files are not migrated or deleted. Each contributing
  bundle has one clock domain; multi-clock bundles are excluded with a warning. XML paths use clock UUID plus public
  Trace Bus ID, not processor labels or private `ctrace_route` context. Clock-derived namespaces prevent view-ID
  collisions across targets. Legacy `swo_clock` also gets a UUID without a binary layout change; independent captures
  are neither synchronized nor rebased.
- CSV uses the published `address` column. The plan's outstanding rename from `offset` is no longer applicable.

These are current contracts, not deferred phases of the migration. Detailed behavior and output-selection exceptions
remain in the linked live documents.
