---
id: "txmw-chapter-1-introduction-to-tracex-tracex-constraints"
type: "concept"
domain: "trace"
title: "Chapter 1 - Introduction to TraceX: TraceX Constraints"
summary: "Chapter 1 - Introduction to TraceX: TraceX Constraints"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter1.md#tracex-constraints"
license: "MIT"
mode: "V"
---

TraceX has the following constraints:

- TraceX files are limited to a maximum of 32,768 events (roughly 1 MB ).
- The time-stamp source must have reasonable resolution. If the resolution is too low, the events will overlap. If the resolution is too high, there is potential for long gaps between events.
- TraceX cannot accurately measure intervals between events greater than the timer period.
