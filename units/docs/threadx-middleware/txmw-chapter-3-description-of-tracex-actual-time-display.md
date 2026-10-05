---
id: "txmw-chapter-3-description-of-tracex-actual-time-display"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Actual Time Display"
summary: "When enabled, TraceX displays the actual time in microseconds in Time View and for the various delta time information displayed by TraceX. By default, the actual time display is disabled."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#actual-time-display"
license: "MIT"
mode: "V"
---

When enabled, TraceX displays the actual time in microseconds in ***Time View*** and for the various delta time information displayed by TraceX. By default, the actual time display is disabled. To enable the actual time display, the number of ticks per microsecond must be entered via the ***Options -> Ticks per Microsecond*** menu selection (the value to enter is determined by the hardware timer source used for the TraceX event logging on the target).
