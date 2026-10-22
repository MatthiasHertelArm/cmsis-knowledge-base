---
id: "devt-ctrace-message-system-design"
type: "concept"
domain: "trace"
title: "ctrace message-system design"
summary: "All ctrace-owned diagnostic templates live in one [message catalog][catalog] in ctrace::model. Each entry has a MessageId, detailed text for verbose CLI, and compact text shared by CSV and normal CLI."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/message-system-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/message-system-design.md"
license: "Apache-2.0"
mode: "V"
---

All ctrace-owned diagnostic templates live in one [message catalog][catalog] in `ctrace::model`. Each entry has a
`MessageId`, detailed text for verbose CLI, and compact text shared by CSV and normal CLI. The enum is generated from
the same table, so there is no separate list of IDs to keep synchronized. Foreign descriptions remain opaque values
supplied to owned templates.

| Component | Responsibility |
| --- | --- |
| [MessageCatalog.inc][catalog] | IDs and adjacent detailed/compact templates. |
| [Messages.h][messages-header] / [Messages.cpp][messages-source] | Argument values, template validation and rendering. |
| [TraceMessages][trace-header] | Typed trace records and adapters that select catalog IDs and arguments. |
| [DiagnosticMessages][diagnostic-header] | Typed adapters for operational message families. |

The adapters retain decisions about protocol categories, optional fields, hexadecimal values, and numeric precision.
They do not own a second table of diagnostic wording. Fixed CLI-only messages call `formatMessage(MessageId::...)`
directly. Parameterized CLI-only messages use an appropriate typed adapter or pass explicit catalog arguments.
The implementation requires C++17 and no external formatting dependency.
