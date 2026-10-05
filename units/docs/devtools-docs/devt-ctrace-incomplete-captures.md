---
id: "devt-ctrace-incomplete-captures"
type: "concept"
domain: "trace"
title: "ctrace: Incomplete captures"
summary: "Formatted input accounts for payload skipped because its source ID is missing, NULL, reserved, or unconfigured, and for initial protocol bytes skipped while seeking hardware synchronization."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/README.md#incomplete-captures"
license: "Apache-2.0"
mode: "V"
---

Formatted input accounts for payload skipped because its source ID is missing, NULL, reserved, or unconfigured,
and for initial protocol bytes skipped while seeking hardware synchronization. Each accounting record is CLI Info and a
CSV `info` row, retained regardless of type or stream filters. `info` is an input annotation, not a new `--type`
selector. The row has no time; `stream` contains the observed formatter ID, including `0` or `127`, or is empty when
no ID is known. These observations do not create decoded routes.

The note counts **deformatted payload bytes**, not formatter control bytes or differences between raw offsets.
CSV and normal CLI use `N bytes skipped: reason`; `--verbose` also reports the first formatter output group's raw offset.
No raw bytes are rewritten and no synchronization is invented.
Before synchronization, the skipped bytes cannot be classified as ITM software packets or DWT hardware packets
(including exception trace), so the CSV note uses `N bytes skipped: no SYNC`.
This accounting covers formatter skips and initial ITM synchronization, not every possible decoder-recovery loss.

If a configured formatted route receives bytes but never reaches a real ITM hardware synchronization, ctrace reports
an Error at end of input and exits non-zero. Completed diagnostic and decoded outputs are retained, including data
from healthy routes. Continuing past an unassigned prefix therefore does not guarantee decodable payload.

A fatal OpenCSD error, including a framing error, aborts decoding and returns a non-zero status. A CSV output that
has already started retains the previously committed rows and ends with a global `type=error` row. Its `note` starts
with `Decode aborted; trace incomplete` and adds a compact structured cause when available;
all other fields are empty. Normal CLI uses the same message; `--verbose` adds the processed-byte count and detailed
abort reason. This final record describes the entire input,
so it bypasses both `--type` and `--stream`. The incomplete CTF bundle is removed
and contributes no views to the target XML; completed bundles from other inputs remain eligible. A failure before
CSV starts creates no CSV, and a CSV write or close failure still
removes the unreliable file. Preserving partial CSV with this global marker is an explicit ctrace contract; the
published CSV specification does not define fatal-abort handling.
