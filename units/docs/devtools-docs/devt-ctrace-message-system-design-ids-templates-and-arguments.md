---
id: "devt-ctrace-message-system-design-ids-templates-and-arguments"
type: "concept"
domain: "trace"
title: "ctrace message-system design: IDs, templates and arguments"
summary: "A catalog row uses CTRACE_MESSAGE(Id, detailed, compact). Templates accept positional placeholders such as {0} and {1}. Braces in templates must form positional placeholders. Argument values are copied as text and are never interpreted as nested templates."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/message-system-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/message-system-design.md#ids-templates-and-arguments"
license: "Apache-2.0"
mode: "V"
---

The central API is:

```cpp
std::string formatMessage(
    MessageId id,
    MessageStyle style = MessageStyle::Detailed,
    std::initializer_list<MessageArgument> arguments = {});
```

A catalog row uses `CTRACE_MESSAGE(Id, detailed, compact)`. Templates accept positional placeholders such as `{0}`
and `{1}`. Braces in templates must form positional placeholders. Argument values are copied as text and are never
interpreted as nested templates. There are no named placeholders or format specifiers.

```cpp
CTRACE_MESSAGE(TraceSkipMissingSync,
               "{0} bytes skipped due to missing SYNC; first formatter group at raw offset {1}",
               "{0} bytes skipped: no SYNC")

formatMessage(MessageId::TraceSkipMissingSync, MessageStyle::Compact, {24U, 128U});
// 24 bytes skipped: no SYNC
```

`MessageArgument` owns its value. It accepts strings, string views, non-null C strings, and integral values rendered
in decimal. Typed adapters format hexadecimal payloads and floating-point precision before passing those values.
Counts and offsets remain 64-bit throughout trace transport; formatting does not narrow them.

Detailed and compact templates share one argument list, but either template may omit positions it does not display.
For example, the detailed skipped-byte message can use a count, source ID and formatter offset, while its compact
version uses only the count. Both styles receive all three arguments. The table is checked at compile time for valid
placeholder syntax and a contiguous union of argument positions starting at zero. At runtime, an invalid ID, invalid
style or wrong argument count is rejected rather than producing partial text.

A `nullptr` compact template reuses the detailed template. This is the normal declaration for CLI-only messages;
it does not cause a new CSV record to be emitted. An empty string is an intentionally empty template, not a request
for fallback. Message IDs are internal identifiers; they are not serialized as new CSV fields or CTF attributes.
