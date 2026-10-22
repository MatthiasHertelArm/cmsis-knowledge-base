---
id: "devt-ctrace-message-system-design-operational-messages-and-foreign-detail"
type: "concept"
domain: "trace"
title: "ctrace message-system design: Operational messages and foreign detail"
summary: "DiagnosticMessages provides typed adapters for CLI argument checks, trace-run discovery, YAML field validation, source locations, processor/route binding, deferred metadata errors, path/IO failures, backend lifecycle failures and run summaries. Each adapter selects an entry in the central catalog."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/message-system-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/message-system-design.md#operational-messages-and-foreign-detail"
license: "Apache-2.0"
mode: "V"
---

`DiagnosticMessages` provides typed adapters for CLI argument checks, trace-run discovery, YAML field validation,
source locations, processor/route binding, deferred metadata errors, path/IO failures, backend lifecycle failures
and run summaries. Each adapter selects an entry in the central catalog. Messages are formatted at their existing
call sites because only the CLI consumes them; they do not become `TraceIssueEvent` values. Actionable file/field
identity and causes remain available in normal output. Selected configuration, metadata, timestamp prescalers and
processing summaries are marked `Visibility::Verbose`; byte-skip Info remains normally visible.

Examples include `configFieldMessage(field, ConfigFieldProblem::UnsignedRange)`,
`pathDiagnosticMessage(PathDiagnosticCode::CsvOpen, path)`, and `decodeSummaryMessage(bytes, seconds, records)`.
Fixed messages need no adapter and call `formatMessage` directly. Owned wrappers around foreign text, such as YAML
source locations or backend failure context, also use catalog templates.

Reference/pyTS messages, native YAML/cxxopts/OpenCSD text, OS errors and unexpected exception text retain their
passthrough behavior for operational diagnostics: they are not parsed or truncated to make them shorter.
`TraceOpaqueMessage` retains foreign or caller-supplied trace descriptions: verbose CLI preserves them,
while normal CLI and CSV use the semantic issue category as their compact fallback. Opaque abort causes do not pretend
to supply a structured explanation. Severity and failure impact remain at their existing call sites.
