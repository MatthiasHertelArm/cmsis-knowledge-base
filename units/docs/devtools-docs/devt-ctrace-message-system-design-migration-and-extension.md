---
id: "devt-ctrace-message-system-design-migration-and-extension"
type: "concept"
domain: "trace"
title: "ctrace message-system design: Migration and extension"
summary: "CSV notes and default CLI diagnostic text intentionally become compact. Technical informational output now requires --verbose. Consumers that compare complete messages must update their expectations. Columns, event types, filters, route attribution and CSV escaping are unchanged."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/message-system-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/message-system-design.md#migration-and-extension"
license: "Apache-2.0"
mode: "V"
---

CSV notes and default CLI diagnostic text intentionally become compact. Technical informational output now requires
`--verbose`. Consumers that compare complete messages must update their expectations. Columns, event types, filters,
route attribution and CSV escaping are unchanged. Use `type` and `stream` for selection, and `--verbose` when
investigating native errors or packet bytes. Internal message IDs are not an additional interchange format.

When adding or changing a message:

1. Add its `MessageId` and adjacent detailed/compact templates to `MessageCatalog.inc`. Use `nullptr` for a CLI-only
   compact template and preserve the existing detailed wording when migrating a caller.
2. For a shared trace diagnostic, add or reuse a typed record and adapt it to catalog arguments at the output
   boundary. Preserve semantic issue mapping and transport the record through every intermediate API.
3. For a CLI-only message, call `formatMessage` directly or extend an appropriate typed adapter. Preserve exception
   type, context, severity and failure impact. Keep foreign text opaque. Mark technical-only context or informational
   events explicitly; do not infer their visibility from strings or field names.
4. Test the catalog arguments and both output styles. Verify the producer/consumer path when parameters, optional
   context, filtering, ordering or output lifecycle can change.

Catalog tests cover placeholder validation, argument ownership and substitution, omitted compact parameters,
64-bit values, decimal/hex rendering, native categories/codes, packet previews, timestamp ranges and abort phases.
Decoder, CSV, diagnostics and integration tests cover transport, callback ordering, route attribution, event filters,
recovery, overflow summaries and terminal-abort lifecycle. Verbosity tests compare normal and verbose stderr, shared
compact CLI/CSV text, unchanged CSV/CTF output and exit status, and forwarding of optional details. CSV reference
changes are confined to diagnostic notes; other columns and the CTF/XML fixtures retain their contents.

[catalog]: ../src/model/MessageCatalog.inc
[messages-header]: ../src/model/Messages.h
[messages-source]: ../src/model/Messages.cpp
[trace-header]: ../src/model/TraceMessages.h
[diagnostic-header]: ../src/model/DiagnosticMessages.h
[error-controller]: ../src/decode/OpenCsdErrorController.cpp
[csv-mapper]: ../src/output/csv/CsvRowMapper.cpp
